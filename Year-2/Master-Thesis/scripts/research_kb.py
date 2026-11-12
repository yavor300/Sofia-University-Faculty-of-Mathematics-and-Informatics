#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf==1.28.2", "PyYAML==6.0.3", "bibtexparser==2.1.0"]
# ///
"""Read-only source discovery/integrity checks and hash-keyed PDF extraction.

Never writes raw/, articles, bibliography, or the reviewed-source manifest.
Extraction is a processing aid, not automatic scientific analysis.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path('references/source-manifest.json')


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_manifest(root):
    path = root / MANIFEST
    return json.loads(path.read_text()) if path.exists() else {'schema_version': 1, 'sources': []}


def inventory(root, manifest):
    known = {s['source_pdf']: s for s in manifest['sources']}
    paths = sorted(p for p in (root / 'raw/papers').rglob('*') if p.is_file() and p.suffix.lower() == '.pdf')
    rows = []
    for p in paths:
        rel = p.relative_to(root).as_posix()
        digest = sha256(p)
        previous = known.pop(rel, None)
        state = 'new' if previous is None else ('unchanged' if digest == previous['sha256'] else 'modified')
        rows.append({'source_pdf': rel, 'sha256': digest, 'state': state,
                     'source_id': previous['source_id'] if previous else None})
    rows.extend({'source_pdf': p, 'source_id': s['source_id'], 'state': 'missing'} for p, s in sorted(known.items()))
    return rows


def extract(root, manifest, selected):
    import pymupdf
    rows = inventory(root, manifest)
    if selected:
        requested = set(selected)
        unknown = requested - {r['source_pdf'] for r in rows if r['state'] != 'missing'}
        if unknown:
            raise ValueError(f'Unknown/missing source paths: {sorted(unknown)}')
        rows = [r for r in rows if r['source_pdf'] in requested]
    else:
        rows = [r for r in rows if r['state'] in ('new', 'modified')]
    out = root / 'references/extracted'
    out.mkdir(parents=True, exist_ok=True)
    for r in rows:
        target = out / f"{r['sha256']}.json"
        if target.exists():
            print(f"CACHED {target.relative_to(root)}")
            continue
        with pymupdf.open(root / r['source_pdf']) as doc:
            pages = [{'pdf_page': i + 1, 'text': p.get_text(sort=True)} for i, p in enumerate(doc)]
            record = dict(source_pdf=r['source_pdf'], sha256=r['sha256'], extractor='PyMuPDF',
                          extractor_version=pymupdf.VersionBind, metadata=doc.metadata, pages=pages,
                          warnings=[f"Page {p['pdf_page']}: little extractable text; inspect visually or use OCR"
                                    for p in pages if len(p['text'].strip()) < 40])
        # Exclusive creation preserves any existing extraction and all source files.
        with target.open('x', encoding='utf-8') as f:
            json.dump(record, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f"EXTRACTED {r['source_pdf']}: {len(pages)} pages -> {target.relative_to(root)}")
        for warning in record['warnings']:
            print(f'REVIEW {warning}')


def frontmatter(path):
    import yaml
    text = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError('missing YAML frontmatter')
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError('frontmatter must be a mapping')
    return data, text[match.end():]


def prose(text):
    """Exclude literal examples from citation/link validation."""
    text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)
    return re.sub(r'`[^`\n]*`', '', text)


def check(root, manifest):
    import bibtexparser
    import pymupdf
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    rows = inventory(root, manifest)
    for r in rows:
        require(r['state'] == 'unchanged', f"Source {r['state']}: {r['source_pdf']}")
    sources = manifest['sources']
    for field in ('source_id', 'source_pdf', 'citation_key', 'doi', 'sha256', 'literature_note'):
        vals = [s.get(field) for s in sources]
        require(all(vals), f'Manifest has missing {field}')
        require(len(vals) == len(set(vals)), f'Manifest has duplicate {field}')
    bib = bibtexparser.parse_file(str(root / 'references/library.bib'))
    require(not bib.failed_blocks, f'BibTeX parse failures: {len(bib.failed_blocks)}')
    entries = {e.key: e for e in bib.entries}
    require(len(entries) == len(bib.entries), 'Duplicate BibTeX keys')
    require(set(entries) == {s['citation_key'] for s in sources}, 'Bibliography/source coverage mismatch')
    articles = {}
    names = defaultdict(list)
    for p in sorted((root / 'wiki').rglob('*.md')):
        rel = p.relative_to(root).as_posix()
        try:
            meta, body = frontmatter(p)
        except Exception as e:
            errors.append(f'{rel}: {e}')
            continue
        articles[p] = (meta, body)
        names[p.stem].append(p)
        for field in ('type', 'title', 'status'):
            require(bool(meta.get(field)), f'{rel}: missing {field}')
        for key in re.findall(r'(?<!\w)@([A-Za-z][A-Za-z0-9_:-]*)', prose(body)):
            require(key in entries, f'{rel}: unknown citation key {key}')
        for key in meta.get('citation_keys', []):
            require(key in entries, f'{rel}: unknown metadata citation key {key}')
        for source_id in meta.get('source_ids', []):
            require(source_id in {s['source_id'] for s in sources}, f'{rel}: unknown source ID {source_id}')
    for name, paths in names.items():
        require(len(paths) == 1, f'Ambiguous/duplicate article basename: {name}')
    titles = Counter(meta['title'].casefold() for meta, _ in articles.values() if meta.get('type') == 'concept')
    for title, count in titles.items():
        require(count == 1, f'Duplicate concept title: {title}')
    link_count = 0
    for p, (meta, body) in articles.items():
        rel = p.relative_to(root)
        for match in re.finditer(r'\[\[([^\]]+)\]\]', prose(body)):
            dest = match[1].split('|')[0]
            target, _, heading = dest.partition('#')
            if not target:
                continue
            link_count += 1
            linked = None
            if '/' in target:
                q = root / 'wiki' / target
                if not q.suffix:
                    q = q.with_suffix('.md')
                require(q in articles, f'{rel}: unresolved wiki target {target}')
                linked = q if q in articles else None
            else:
                require(len(names.get(target.removesuffix('.md'), [])) == 1, f'{rel}: unresolved/ambiguous wikilink {target}')
                matches = names.get(target.removesuffix('.md'), [])
                linked = matches[0] if len(matches) == 1 else None
            if linked and heading:
                headings = re.findall(r'^#{1,6}\s+(.+?)\s*$', articles[linked][1], re.M)
                require(heading in headings, f'{rel}: missing heading {target}#{heading}')
        for dest in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)', prose(body)):
            parsed = urlsplit(dest)
            if parsed.scheme or dest.startswith('#'):
                continue
            require((p.parent / unquote(parsed.path)).exists(), f'{rel}: missing local Markdown target {dest}')
    literature = {p: data for p, data in articles.items() if data[0].get('type') == 'literature'}
    require(len(literature) == len(sources), 'Literature/source count mismatch')
    required_sections = ['Overview', 'Research Problem', 'Research Objectives', 'Methodology',
                         'Proposed Architecture or Approach', 'Key Contributions', 'Results and Findings',
                         'Limitations', "Relevance to My Master's Thesis", 'Important Evidence',
                         'Related Concepts', 'Open Research Questions', 'Bibliographic Reference']
    for s in sources:
        p = root / s['literature_note']
        require(p in literature, f"Missing literature note: {s['literature_note']}")
        if p not in literature:
            continue
        meta, body = literature[p]
        for field in ('authors', 'year', 'doi', 'citation_key', 'source_url', 'source_pdf', 'topics', 'source_id'):
            require(bool(meta.get(field)), f'{p.name}: missing {field}')
        for field in ('source_id', 'source_pdf', 'citation_key', 'doi'):
            require(meta.get(field) == s[field], f'{p.name}: manifest mismatch in {field}')
        for heading in required_sections:
            require(f'# {heading}\n' in body, f'{p.name}: missing section {heading}')
        require('PDF p' in body and '| Evidence type |' in body, f'{p.name}: missing page-referenced evidence table')
        entry = entries.get(s['citation_key'])
        if entry:
            fields = {f.key: f.value for f in entry.fields}
            for field in ('author', 'title', 'journal', 'year', 'doi', 'url', 'file'):
                require(bool(fields.get(field)), f'{entry.key}: missing BibTeX {field}')
            require(fields.get('doi') == s['doi'], f'{entry.key}: DOI mismatch')
            require(fields.get('file') == s['source_pdf'], f'{entry.key}: source path mismatch')
            require(fields.get('year') == str(meta['year']), f'{entry.key}: year mismatch')
        pdf = root / s['source_pdf']
        if pdf.exists():
            with pymupdf.open(pdf) as doc:
                require(len(doc) == s['pdf_pages'] == meta.get('pdf_pages'), f'{p.name}: page-count mismatch')
                require(s.get('text_reviewed_pages') == list(range(1, len(doc) + 1)), f'{p.name}: incomplete recorded text coverage')
                require(all(1 <= n <= len(doc) for n in s.get('visually_reviewed_pages', [])), f'{p.name}: invalid visual page')
    result = dict(result='FAIL' if errors else 'PASS', source_pdfs=len(sources),
                  literature_notes=len(literature), markdown_articles=len(articles),
                  bibliography_entries=len(entries), wikilinks_checked=link_count, errors=errors,
                  limitation='Structural checks do not validate scientific truth; all articles require human review.')
    print(json.dumps(result, indent=2))
    return bool(errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Thesis root; defaults to parent of scripts/')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('scan', help='Report new, modified, unchanged and missing PDFs without writing')
    ext = sub.add_parser('extract', help='Extract new/modified PDFs; never marks a paper analyzed')
    ext.add_argument('--source', action='append', help='Explicit thesis-relative PDF path; repeatable')
    sub.add_parser('check', help='Read-only wiki, bibliography and source-integrity validation')
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = load_manifest(root)
    if args.command == 'scan':
        print(json.dumps(inventory(root, manifest), indent=2))
    elif args.command == 'extract':
        extract(root, manifest, args.source)
    else:
        return check(root, manifest)
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
