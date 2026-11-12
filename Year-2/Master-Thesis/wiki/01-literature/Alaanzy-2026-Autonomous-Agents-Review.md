---
type: literature
title: "Autonomous agents and multi-agent systems: a comprehensive review"
status: ai-draft
updated: 2026-11-12
authors:
  - Mohammed Alaa Ala’anzy
  - Meruyert Oshayeva
  - Yassine Himeur
year: 2026
doi: 10.1007/s10462-026-11731-2
citation_key: alaanzy2026autonomous
source_id: SRC-001
source_url: https://doi.org/10.1007/s10462-026-11731-2
source_pdf: raw/papers/s10462-026-11731-2_reference.pdf
topics:
  - agent architectures
  - memory
  - coordination
  - evaluation
pdf_pages: 40
reading_status: unread
---

# Overview

Ala’anzy, Oshayeva, and Himeur organize agent research through a five-module reference architecture, a capability map spanning ten application domains, and a six-dimensional evaluation framework. The contribution is a structured narrative synthesis, not a new implemented agent system or a controlled comparison of frameworks. Its strongest relevance to this thesis is the relationship between memory, coordination, oversight, and evaluation. [@alaanzy2026autonomous, PDF pp. 9–11, 16–18, 29–30]

**Evidence scope:** the entire 40-page local Article in Press was read, including its references. Page numbers below are one-based PDF positions; the repeated footer “1 3” is not pagination. References cited by the review are secondary evidence here, not independently reviewed sources. Stable source ID: `SRC-001`. See [[Evidence-and-Uncertainties]].

# Research Problem

The authors identify inconsistent architectural terminology, weak comparison across application domains, and heterogeneous evaluation practices. They argue that these problems prevent findings from accumulating into comparable design knowledge. This is the review’s diagnosis of its selected literature, not a verified statement about every agent publication. [@alaanzy2026autonomous, PDF pp. 3–5, 8–9, §§1.2–1.3, 2.3]

# Research Objectives

The review seeks to consolidate architectural responsibilities, compare reasoning/planning, tool use, memory/learning and collaboration across ten domains, and expose evaluation limitations. It also develops a research agenda covering technical, methodological and societal concerns. [@alaanzy2026autonomous, PDF pp. 4–6, 16–18, §§1.3, 5]

# Methodology

The search is PRISMA-informed and adapted to narrative synthesis. A March 2026 Scopus query returned 107 original-research records; 13 preliminary exclusions left 94, screening left 76 for full-text assessment, and 15 further exclusions left 61. Manual screening contributed 46 additional studies, yielding the reported 107 original studies. A separate review search returned 123 records, from which 31 reviews were selected. The reported overall corpus is 154 sources: 107 original studies, 31 reviews, eight foundational works, five industry reports, and three additional contextual works. The two database queries together yielded 230 raw records; this is distinct from the final corpus. [@alaanzy2026autonomous, PDF pp. 9–11, §3]

Extraction covers architecture, capabilities, domain/task, evaluation, results and limitations. Thematic analysis groups these observations; there is no common reimplementation or pooled effect-size meta-analysis. Manual venue screening is explicitly less reproducible than the database query. The criteria favor English, peer-reviewed work but explicitly permit some arXiv exceptions. Accordingly, “107 peer-reviewed studies” is the authors’ corpus description and requires study-level verification before reuse as an exact eligibility claim. [@alaanzy2026autonomous, PDF pp. 10–11, 29–30, §§3, 9.5]

# Proposed Architecture or Approach

The architecture allocates responsibilities to **profile** (identity and roles), **memory** (retained context and knowledge), **planning** (goal decomposition and action selection), **action** (tool and environment interaction), and **security** (policy, access and oversight). These are conceptual responsibilities, not five mandatory physical services. Figure 4 and Table 6 map the authors’ synthesis to earlier frameworks; those earlier frameworks have not been independently analyzed in this knowledge base. [@alaanzy2026autonomous, PDF pp. 6, 12–13, 16, Fig. 4, Table 6]

The review distinguishes implicit, explicit and agentic memory. Its account of agentic memory emphasizes knowledge accumulated and revised across episodes, while highlighting weak update validation and insufficient evidence about stability after repeated revisions. Coordination is classified as centralized, decentralized or hybrid. Human oversight and agent specialization are separate classification dimensions. [@alaanzy2026autonomous, PDF pp. 13–15, 19–20, §§4.3–4.5, 6.3]

The evaluation framework covers task performance, efficiency, quality, robustness, safety and interpretability. Its coverage gaps describe the authors’ surveyed corpus; they do not establish that no relevant benchmark exists outside it. [@alaanzy2026autonomous, PDF pp. 16–18, Table 8]

# Key Contributions

- A common component vocabulary and mapping across earlier architectural frameworks. [@alaanzy2026autonomous, PDF pp. 13, 16, §5.1]
- An illustrative domain-by-capability map, with domain knowledge integration and planner–executor–reflector specialization identified as recurring patterns. [@alaanzy2026autonomous, PDF pp. 16–17, §5.2, Table 7]
- An evaluation taxonomy and an explicit discussion of the difference between benchmark performance and deployment validation. [@alaanzy2026autonomous, PDF pp. 17–18, 26–29, §§5.3, 8–9]

# Results and Findings

The authors report that explicit domain knowledge integration and role specialization recur across domains. These are qualitative synthesis findings. Table 7 selects illustrative, strongly reported systems rather than representative domain averages; it does not establish causal effects or a universal best architecture. The authors explicitly warn that performance figures from different studies use different baselines and must not be aggregated into a scoreboard. [@alaanzy2026autonomous, PDF pp. 16–17, 27–28, §§5.2, 9.1–9.2]

They identify limited cross-domain validation for robustness, safety and interpretability and report frequent omission of an explicit security module. The main PDF does not supply a study-level numerical denominator for that omission claim; retain it as an attributed qualitative finding. [@alaanzy2026autonomous, PDF pp. 16–18, 28–29]

One illustrative secondary result is a sensitivity change from 0.91 to 0.62 under prevalence shift, attributed by the review to Tian et al. This is neither an experiment performed by these reviewers nor independently verified here. It motivates testing under changed conditions, not a general expected degradation for agent systems. [@alaanzy2026autonomous, PDF pp. 18, 27–28, 31]

# Limitations

**Author-stated:** English/indexing and terminology restrictions; a less reproducible manual search; no independent reproduction of cited results; no independent empirical validation of the proposed architecture, capability map or evaluation framework; and a March 2026 cutoff. [@alaanzy2026autonomous, PDF pp. 29–30, §9.5]

**Analyst assessment:** the qualitative corpus does not demonstrate that domain knowledge or additional agents will improve a particular implementation. The stated peer-review restriction has exceptions. Several author-year suffixes differ between the prose and reference list, so a page-level citation to this review is safer than copying its underlying citations without checking them. For example, radiotherapy is attributed to Wang et al. (2025a) on p. 22, whereas the corresponding reference is Wang et al. (2025b) on p. 39. See uncertainty records `A-U1`–`A-U4`. [@alaanzy2026autonomous, PDF pp. 11, 16–17, 22, 29, 39]

# Relevance to My Master's Thesis

| Thesis dimension | Evidence and interpretation |
| --- | --- |
| Heterogeneous autonomous agents | Profile, action and hybrid-model responsibilities supply a comparison vocabulary; they do not establish cross-framework compatibility (pp. 13, 19). |
| Multi-agent orchestration | Authority distribution and role specialization support decomposing the management layer from execution (pp. 15–16, 20). |
| Organizational and shared memory | Persistent agentic memory is a useful precursor; an organization-wide governance model is a thesis synthesis rather than this paper’s validated contribution (p. 19). |
| Controlled self-improvement | The discussion of unvalidated memory updates motivates explicit admission and regression checks; those checks are proposed thesis mechanisms (pp. 19–20). |
| Reliability and evaluation | The six dimensions and the oversight discussion justify measuring traceability and recovery alongside task success (pp. 17–18, 29–31). |

All five mappings are analyst interpretations grounded in the cited passages. [@alaanzy2026autonomous, PDF pp. 13–20, 29–31]

# Important Evidence

“Verified” means checked against this PDF, not replicated scientifically.

| ID | Claim or finding | Supporting PDF location | Evidence type | Verification |
| --- | --- | --- | --- | --- |
| A01 | 61 database-selected + 46 manually selected original studies; reported total corpus 154 | pp. 9–11, §3 | Authors’ methodology | Text verified; supplementary corpus not audited |
| A02 | Five conceptual responsibilities; not mandatory separate components | pp. 6, 13, 16, Fig. 4, Table 6 | Authors’ synthesis | Text and visual verified |
| A03 | Centralized, decentralized and hybrid coordination; separate oversight levels | pp. 14–15, Tables 3–4 | Taxonomy | Text and relevant figure verified |
| A04 | Memory updates across episodes lack clear validation/stability guidance in reviewed work | p. 19, §6.3 | Authors’ critical synthesis | Text verified; field-wide scope unverified |
| A05 | Recurrent domain grounding and role specialization | pp. 16–17, 27–28 | Qualitative cross-study synthesis | Table visually checked; no causal inference |
| A06 | Six evaluation dimensions and limited coverage | pp. 17–18, Table 8 | Proposed evaluation framework | Table visually checked; not independently validated |
| A07 | Sensitivity 0.91 → 0.62 under prevalence shift | pp. 18, 28, 31 | Secondary empirical claim | Review text verified; primary study unread |
| A08 | Meaningful human oversight requires observability and intervention ability | p. 29, §9.4 | Authors’ argument | Text verified |
| A09 | Reported gains are not directly cross-comparable | p. 28, §9.2 | Methodological qualification | Text verified |
| A10 | Frameworks remain conceptual and cited systems were not rerun | pp. 29–30, §9.5 | Author-stated limitation | Text verified |

# Related Concepts

[[Autonomous-AI-Agents]], [[Multi-Agent-Systems]], [[Agent-Orchestration]], [[Agent-Coordination]], [[Agent-Communication]], [[Agent-Memory]], [[Organizational-Memory]], [[Shared-Memory]], [[Agent-Interoperability]], [[Controlled-Self-Improvement]], [[Agent-Evaluation]], [[Reliability-and-Fault-Tolerance]]. Compare [[Zhu-2026-Multi-Agent-Orchestration]] in [[Multi-Agent-Research-Comparison]].

# Open Research Questions

**Analyst hypotheses:** Can memory updates be admitted only after provenance and regression checks? Can a common trace represent planning, action and oversight across heterogeneous runtimes? Does explicit recovery testing reveal failures that task-success-only evaluation misses? These extend the concerns on pp. 19, 29–31 and are developed in [[Research-Gaps]].

# Bibliographic Reference

Mohammed Alaa Ala’anzy, Meruyert Oshayeva, and Yassine Himeur. 2026. *Autonomous agents and multi-agent systems: a comprehensive review*. Artificial Intelligence Review, Article in Press. DOI: [10.1007/s10462-026-11731-2](https://doi.org/10.1007/s10462-026-11731-2). Citation key: `alaanzy2026autonomous`.

Source PDF: [s10462-026-11731-2_reference.pdf](../../raw/papers/s10462-026-11731-2_reference.pdf). Thesis-root-relative path: `raw/papers/s10462-026-11731-2_reference.pdf`.

Title, authors, journal, year and DOI were checked in the PDF. The [publisher record](https://link.springer.com/article/10.1007/s10462-026-11731-2), accessed 2026-11-12, supplies the online publication date 2026-10-16 and confirms Article in Press status. Volume, issue and final publication pages remain unfilled; PDF length is not a journal page range.
