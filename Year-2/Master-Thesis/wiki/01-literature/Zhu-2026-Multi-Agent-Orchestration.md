---
type: literature
title: "LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns"
status: ai-draft
updated: 2026-11-12
authors:
  - Yiwen Zhu
  - Lihe Liu
  - Jiaqian Yu
  - Di Zhang
year: 2026
doi: 10.3390/fi18060326
citation_key: zhu2026orchestration
source_id: SRC-002
source_url: https://doi.org/10.3390/fi18060326
source_pdf: raw/papers/futureinternet-18-00326-v2.pdf
topics:
  - orchestration
  - interoperability
  - shared memory
  - self-evolution
  - evaluation
pdf_pages: 61
reading_status: unread
---

# Overview

Zhu, Liu, Yu, and Zhang present a structured narrative survey of orchestration, framework abstractions, communication protocols and evaluation. They separate coordination topology from runtime adaptivity and distinguish workflow execution from changes to the agent organization itself. The paper also reports a reanalysis of public annotated execution traces (Study A) and a small live measurement-harness illustration using synthetic stand-in tasks (Study B). [@zhu2026orchestration, PDF pp. 5–8, 10–11, 37–40, 54–56]

**Evidence scope:** all 61 pages of the local v2 PDF were read, including appendices and references. Page numbers are one-based PDF positions and match the printed “x of 61” numbering. Stable source ID: `SRC-002`. Results below are attributed to this paper; external datasets, code and cited studies have not been independently reproduced. See [[Evidence-and-Uncertainties]].

# Research Problem

The survey treats orchestration as task allocation, communication/context sharing, state persistence, control flow, and error recovery. It argues that assessing individual-model output misses failures of delegation, consistency and termination at the collective level. Its discussion distinguishes routing a workflow from deciding which agents and roles should constitute the collective. [@zhu2026orchestration, PDF pp. 2, 5, §§1, 2.3–2.4]

# Research Objectives

The objectives are to classify orchestration structures, compare framework design choices, explain protocol boundaries, organize deployment concerns, and define process-sensitive evaluation dimensions. The paper also explores learned coordination and tasks that persist across sessions. [@zhu2026orchestration, PDF pp. 3, 11, 34–38, 47–49]

# Methodology

The authors describe a single-reviewer structured narrative search across Scopus, Web of Science, IEEE Xplore, ACM Digital Library, arXiv and Google Scholar, supplemented by citation snowballing. The search window is January 2022–March 2026, while the stated topical survey coverage is 2023–early 2026. Approximate screening counts are 1,200 retrieved, 400 after filtering, 200 for full-text review, 120 passing full-text criteria, and about 80 primary references; the reduction from 120 to 80 is not fully explained in the main text. The authors state that revision expanded the bibliography to 104 entries, but the local PDF ends at reference 106. Later additions include May 2026 preprints and a dataset snapshot accessed on 25 May. Preserve the March cutoff as the declared core search boundary, with later revision material recorded separately. [@zhu2026orchestration, PDF pp. 3, 5–7, 37, 49, 51, 61]

The survey distinguishes peer-reviewed sources, preprints, vendor reports, industry surveys, regulatory materials and standards. This is its attribution scheme; peer review is not equivalent to independent reproduction. [@zhu2026orchestration, PDF pp. 6–7, §3.1]

**Study A:** the authors analyze a public MAST-Data snapshot reported to contain 1,242 traces, across nine framework–benchmark cells, and a five-cell subset of 30 unique-task traces each (150 total). The larger source-paper corpus of 1,642 includes traces unavailable in the public release. Success is defined as all 14 failure flags being zero. Role-tag and retry-word densities are textual proxies, not direct measurements of coordination utility or successful recovery. [@zhu2026orchestration, PDF pp. 37–40, 52–54]

**Study B:** 108 live CrewAI runs, 54 per backend, use six self-contained GAIA-shaped stand-ins, not the gated GAIA benchmark. Per backend, 18 runs vary agent count over 1, 2 and 4; another 36 use two agents with three tool-failure probabilities and two seeds. This is a portability illustration with a strong ceiling effect, not a unified validation of all six metrics or a framework benchmark. [@zhu2026orchestration, PDF pp. 54–56]

# Proposed Architecture or Approach

The topology dimension comprises centralized, decentralized and hierarchical control. Adaptivity is an independent axis with routing changes, membership changes and learned coordination as submodes. A long task may use any topology; runtime adaptation does not itself imply persistent learning. Hybrid configurations may occupy several cells. [@zhu2026orchestration, PDF pp. 8–13, Definitions 1–3]

Frameworks are compared through their dominant organizing abstractions: explicit graph state, roles and tasks, conversations, handoffs, structured artifacts, and compiled pipelines. These are the survey’s historical descriptions, not verified current software specifications. Default-cell assignments are inconsistent in places; compare the discussion of CrewAI peer delegation on p. 15 with Table 1 on p. 11. Use the abstract axes, then classify a concrete configuration from its actual behavior. [@zhu2026orchestration, PDF pp. 11, 14–22]

The protocol analysis distinguishes tool integration (MCP), agent task delegation (A2A), and decentralized discovery (ANP). It discusses identity, capability advertisement, state lifecycles and trust-boundary translation as distinct concerns. Standardized messaging does not establish interoperable memory semantics or validate a learned routing policy. [@zhu2026orchestration, PDF pp. 22–28, 44, §§6–7.1.1, 10.1]

The six evaluation dimensions are task performance, coordination efficiency, scalability, robustness, cost efficiency and emergent behavior. The formulas measure, respectively, success fraction, useful-message token fraction, token growth with agent count, perturbed/baseline success ratio, cost per attempted task, and off-plan message fraction. Study A substitutes format-dependent textual proxies for two dimensions. These are different constructs and must not be treated as interchangeable. [@zhu2026orchestration, PDF pp. 35–39, Eqs. 1–6]

# Key Contributions

- A topology/adaptivity taxonomy joining workflow and organization-level coordination. [@zhu2026orchestration, PDF pp. 5, 8–13]
- An attributed comparison of framework state models, protocol responsibilities, and recovery concerns. [@zhu2026orchestration, PDF pp. 14–31]
- Process-oriented evaluation definitions, a public-trace reanalysis, and a limited live portability illustration. [@zhu2026orchestration, PDF pp. 35–40, 52–56]
- A research agenda emphasizing protocol translation, learned coordination, long-horizon memory, and safeguard transfer. [@zhu2026orchestration, PDF pp. 44–49]

# Results and Findings

Study A Table 8 reports all-zero-failure-flag rates of 28.5% for ChatDev × ProgramDev (n=130), 25.2% for MetaGPT × ProgramDev (n=230), and 22.1% for Magentic-One × GAIA (n=195). These are descriptive statistics from a deliberately failure-biased archived corpus, not deployment success probabilities or evidence of a causal framework ranking. The 150-trace subset is separate: Table A2 reports 6/30, 10/30 and 4/30 successful traces for those three cells. [@zhu2026orchestration, PDF pp. 37–40, 54, Tables 8, A2]

The coordination proxy equals zero when the expected role markers are absent. A zero for MetaGPT therefore does not mean it communicates more efficiently than ChatDev. Retry density counts words per line rather than task attempts; 24 of 30 AG2 × GSM subset traces have one line, limiting interpretation of its normalization. [@zhu2026orchestration, PDF pp. 38–40, 54]

Study B reports robustness ratios of 1.000 on both backends because all baseline and perturbed tasks succeeded. The authors explicitly attribute this to simple tasks that can be solved while bypassing failed tools. Reported token slopes are 9,493.7 and 6,447.4 tokens per added agent, and mean costs are $0.001833 and $0.005619 per attempt. These are historical author-reported measurements on the stand-ins, not current pricing or generally expected operating costs. The costs and token totals require reconciliation before numerical reuse; see `Z-U7`. [@zhu2026orchestration, PDF pp. 55–56, Table A3]

The authors identify unresolved cross-session resumption, state/policy drift and cross-topology safeguard evaluation. These are survey-bounded research opportunities, qualified by their own discussion of emerging transfer and continual-topology methods. [@zhu2026orchestration, PDF pp. 28, 35, 47–49]

# Limitations

**Author-stated:** approximate screening counts, one reviewer, a rapidly changing ecosystem, non-comparable framework benchmarks, failure-biased trace selection, format-sensitive proxies, simple stand-in tasks, and no unified single-system validation of all six dimensions. [@zhu2026orchestration, PDF pp. 6, 14, 34, 37–40, 56]

**Analyst assessment:** the text contains unresolved inconsistencies in cutoff dates, reference counts, taxonomy placements and proxy coverage descriptions. A comparison of buggy-file identification with issue-resolution scores cannot quantify the fraction of end-to-end performance attributable to memorization. Figure 7 combines historical results and human baselines without enough per-point provenance to use as a contemporary leaderboard. Security assertions about subtree containment and protocol permissions require implementation-specific validation. These concerns are documented in [[Evidence-and-Uncertainties]], rather than silently corrected in the source. [@zhu2026orchestration, PDF pp. 11–15, 30–33, 40, 49, 53, 61]

# Relevance to My Master's Thesis

| Thesis dimension | Evidence and interpretation |
| --- | --- |
| Heterogeneous autonomous agents | Protocol and framework comparisons motivate an adapter contract; common transport alone does not establish shared task semantics (pp. 22–27, 44). |
| Multi-agent orchestration | Topology/adaptivity axes separate control authority from routing, recruitment and learning (pp. 8–13). |
| Organizational and shared memory | State persistence, roster/policy persistence and memory–coordination interplay motivate an organizational memory service (pp. 27–28, 47–48). This service is a thesis proposal. |
| Controlled self-improvement | Existing self-evolving methods establish prior work; the thesis must investigate validation and controlled promotion, rather than claim invention of self-evolution (pp. 20, 47–49). |
| Reliability and evaluation | Failure taxonomy proxies and long-horizon omissions motivate trace completeness, resumption fidelity and failure-injection evaluation (pp. 29–31, 35–40, 52–56). |

These are analyst mappings, not demonstrated properties of the proposed thesis system. [@zhu2026orchestration, PDF pp. 8–13, 20, 22–31, 35–40, 44–56]

# Important Evidence

| ID | Claim or finding | Supporting PDF location | Evidence type | Verification |
| --- | --- | --- | --- | --- |
| Z01 | Structured narrative survey; approximate flow and one reviewer | pp. 5–7, §3 | Authors’ methodology | Text verified; logs not audited |
| Z02 | Topology and adaptivity are independent axes | pp. 8–13, Definitions 1–3, Figs. 2–3 | Authors’ taxonomy | Text and figures verified; assignments disputed |
| Z03 | Workflow and organization-level coordination differ in what changes | pp. 5, 11, 20 | Conceptual distinction | Text verified |
| Z04 | Protocols address different integration responsibilities | pp. 22–27, Figs. 5–6, Tables 4–5 | Specification synthesis | Text/figures checked; specifications not independently reviewed |
| Z05 | Long-lived execution may require state, roster and policy persistence | pp. 27–28, 47–48 | Authors’ synthesis | Text verified |
| Z06 | Six metric definitions; different proxies used in Study A | pp. 35–39, Eqs. 1–6 | Proposed metrics | Equations visually checked |
| Z07 | 1,242 public traces; 150-trace stratified subset | pp. 37–40, 51, 54 | Authors’ trace reanalysis | Text/tables checked; not reproduced |
| Z08 | 28.5% and 25.2% all-zero-flag rates for two ProgramDev cells | p. 39, Table 8 | Descriptive corpus statistics | Visually verified; no causal ranking |
| Z09 | Zero role-tag proxy can mean unobserved formatting | pp. 38–40, 54 | Measurement limitation | Text/tables verified |
| Z10 | 108 live runs on six stand-ins, robustness ceiling | pp. 54–56, Table A3 | Authors’ small experiment | Text/table checked; not reproduced |
| Z11 | Self-evolving methods and emerging transfer/continual methods exist | pp. 20, 47–49 | Secondary literature synthesis | Review text verified; primary methods unread |
| Z12 | Cross-topology safeguard transfer remains untested in their located literature | p. 49, §10.8 | Survey-bounded gap claim | Text verified; broader novelty unverified |

# Related Concepts

[[Autonomous-AI-Agents]], [[Multi-Agent-Systems]], [[Agent-Orchestration]], [[Agent-Coordination]], [[Agent-Communication]], [[Agent-Memory]], [[Organizational-Memory]], [[Shared-Memory]], [[Agent-Interoperability]], [[Controlled-Self-Improvement]], [[Agent-Evaluation]], [[Reliability-and-Fault-Tolerance]]. Compare [[Alaanzy-2026-Autonomous-Agents-Review]] in [[Multi-Agent-Research-Comparison]].

# Open Research Questions

**Analyst hypotheses:** Can task contracts preserve progress across two runtimes and process restarts? Can controlled memory and policy updates preserve prior-task performance under a changing workload? Can provenance-aware traces distinguish state corruption from policy drift? See [[Research-Gaps]] for proposed tests and the further literature needed. These extend pp. 28, 35, 47–49 rather than establish field-wide novelty.

# Bibliographic Reference

Yiwen Zhu, Lihe Liu, Jiaqian Yu, and Di Zhang. 2026. *LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns*. Future Internet 18(6), article 326. DOI: [10.3390/fi18060326](https://doi.org/10.3390/fi18060326). Citation key: `zhu2026orchestration`.

Source PDF: [futureinternet-18-00326-v2.pdf](../../raw/papers/futureinternet-18-00326-v2.pdf). Thesis-root-relative path: `raw/papers/futureinternet-18-00326-v2.pdf`.

Metadata was checked against PDF p. 1 and the [publisher record](https://www.mdpi.com/1999-5903/18/6/326), accessed 2026-11-12. Publication date: 2026-06-15. `326` is an article number, not the start of a page range. Supplementary artifacts are identified on p. 51 by concept DOI `10.5281/zenodo.19774439` and version DOI `10.5281/zenodo.20469702`; those artifacts were not reviewed here and are not added as analyzed bibliography entries.
