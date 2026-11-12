---
type: quality-register
title: Evidence and Uncertainties
status: ai-draft
updated: 2026-11-12
source_ids:
  - SRC-001
  - SRC-002
reading_status: unread
---

# Evidence Policy

The primary evidence for this knowledge base is the exact pair of local PDFs identified in `references/source-manifest.json`. Source claims, analyst interpretations and research hypotheses are labeled separately. “Verified” means readable in the supplied PDF; it never implies that an experiment was rerun. Citation keys refer only to the two analyzed papers. Studies cited inside them remain secondary evidence.

Page references use one-based physical PDF positions. A’s repeated “1 3” footer is not a page number. Z’s printed page positions match the PDF. The extraction includes every page, including references. No OCR was needed; text order, equations and diagram-only labels require visual checks.

# Open Review Register

All entries remain open for human review; none is silently repaired in `raw/`.

| ID | Location | Observation and consequence | Required follow-up |
| --- | --- | --- | --- |
| A-U1 | A pp. 10–11, 36–37 | The corpus is described as peer-reviewed, but the exclusions explicitly permit some arXiv exceptions and the reference list contains them. | Audit the supplementary source categories before stating every included original study passed peer review. |
| A-U2 | A pp. 22, 39; also p. 13 versus p. 40 | Author-year suffixes are inconsistent: radiotherapy is Wang 2025a in prose but 2025b in references; unsuffixed Zhang 2026 can refer to distinct entries. | Identify primary works by full title/DOI, not copied suffixes. |
| A-U3 | A pp. 16, 28–29 | Frequent absence of a security module is asserted without a numerical study-level count in the main PDF. | Inspect the coding data; retain qualitative attribution meanwhile. |
| A-U4 | A p. 1 and publisher record | Article in Press; no verified volume, issue or final publication pagination. | Recheck the final version before thesis submission; preserve this version’s hash and page citations. |
| Z-U1 | Z pp. 3, 6, 37, 51, 61 | Declared March 2026 cutoff coexists with May snapshot access and May arXiv identifiers. The text says 104 references; the PDF numbers 106. | Separate core search from revision additions; inspect screening logs before quoting a final corpus count. |
| Z-U2 | Z pp. 6, 49 | About 120 papers pass full-text screening, but about 80 form the primary corpus; the main-text transition is underexplained. | Reconcile the flow from supplementary records. Do not present approximate counts as a reproducible systematic review. |
| Z-U3 | Z pp. 8, 11, 13, 15 | CrewAI peer delegation is in a static cell in Fig. 2/Table 1 but described as dynamic in §5.1; GPTSwarm/DyLAN appear hierarchical in Fig. 2 but decentralized in Fig. 3’s modifier examples. | Classify concrete configurations; do not reproduce example assignments as settled facts. |
| Z-U4 | Z pp. 32, 40 | Buggy-file identification and issue-resolution performance are different endpoints. The later text acknowledges this, but stronger memorization attribution appears earlier. | Review the primary study; do not interpret a 23-point localization difference as a measured fraction of resolution success due to memorization. |
| Z-U5 | Z pp. 35–40, 53–54 | Formal coordination usefulness/off-plan metrics differ from role-tag/retry proxies. Table A1 lists five coord-proxy rows, whereas its following text refers to seven of eight; “no single metric covers all 14” also conflicts with the explicitly defined binary all-flag aggregate unless “covers” means diagnostic coverage. | Audit extraction code and annotations; distinguish aggregate flag coverage from diagnostic identification. |
| Z-U6 | Z pp. 39–40, 54 | Table 8 reports full cell counts; Table A2 uses n=30 per selected cell. Some prose calls subset summaries inputs to headline statistics. | Keep full-corpus and subset results separate; inspect CSV provenance before statistical comparisons. |
| Z-U7 | Z pp. 55–56 | Reported costs, slopes and token totals depend on per-call delta accounting and historical backend/pricing assumptions. Raw telemetry was not reviewed here. | Recompute from deposited telemetry before using cost magnitudes; these are unreplicated figures, not an established arithmetic error. |
| Z-U8 | Z pp. 30–31, 44 | Containment and permission claims are architectural arguments; signed identity does not certify safe content, and a tree alone does not prove subtree isolation. | Check runtime enforcement and protocol versions; test authenticated malicious content and cross-level propagation. |
| Z-U9 | Z pp. 14, 33 | Fig. 4 is explicitly qualitative. Fig. 7 mixes historical benchmark results and human baselines, with insufficient per-point provenance for a current ranking. | Do not convert radar ratings into measurements or reuse Fig. 7 as a contemporary leaderboard. |
| X-U1 | A pp. 17–18, 28; Z pp. 47–49 | Broad benchmark-gap language coexists with cited transfer/continual-learning studies. The reviewed subsets and endpoints differ. | Preserve both accounts; narrow claims to particular benchmarks, systems and dates. |

Sources for the register: [@alaanzy2026autonomous, PDF pages listed above]; [@zhu2026orchestration, PDF pages listed above]. These observations are analyst critiques, not author-issued corrections. Supplementary artifacts and the underlying primary studies have not been reviewed in this pass.

# Visual Inspection Record

| Source | Items inspected as rendered PDF pages | Interpretation and reuse limits |
| --- | --- | --- |
| A | Fig. 4 (p. 6); Fig. 5 and Tables 2–3 (p. 14); Table 6 (p. 16); Tables 7–8 (p. 17); Figs. 6–7 (p. 21); Table 9 (p. 26); Fig. 8 (p. 30); Fig. 9 and Table 10 (p. 33) | Architecture/taxonomy labels are readable. Capability/domain/challenge links are qualitative, not measured graphs. The year histogram describes this selected corpus, not field-wide publication growth. |
| Z | Fig. 2 (p. 8); Table 2/Fig. 3 (p. 13); Fig. 4 (p. 14); Figs. 5–6 (p. 24); Fig. 7 (p. 33); Eqs. 1–6 (p. 35); Table 8 (p. 39); Tables A1–A3 (pp. 53–55) | Layout and key numbers checked. Taxonomy discrepancies and benchmark provenance remain open. Qualitative ratings, proxy counts and synthetic-task results are not interchangeable evidence. |

Other tables were read in the text extraction. A’s historical/market Figs. 1–3 and Z’s organizational Fig. 1 were not used as substantive thesis evidence. No unread graphical value is asserted. Figure 7 in Z requires manual source-to-point verification before numerical reuse even though its rendered labels are readable.

# Verification Boundary

Automated integrity checks validate file relationships, metadata, source hashes, citation keys, bibliography coverage and wiki links. They cannot prove scientific correctness, novelty or accurate interpretation. The evidence tables in both literature notes and this register provide the manual review trail. All articles remain `ai-draft` until reviewed.

Related: [[Home]], [[Research-Map]], [[Research-Workflow]], [[Processing-Report-2026-11-12]].
