---
type: comparison
title: Multi-Agent Research Comparison
status: ai-draft
updated: 2026-11-12
source_ids:
  - SRC-001
  - SRC-002
reading_status: unread
---

# Scope and Evidence Boundary

This comparison covers [[Alaanzy-2026-Autonomous-Agents-Review]] (`SRC-001`, A) and [[Zhu-2026-Multi-Agent-Orchestration]] (`SRC-002`, Z). They are not independent replications of the same system. “Not evaluated” below means not demonstrated in these supplied papers, not an absent capability of the underlying technology. See [[Evidence-and-Uncertainties]] for conflicts and extraction qualifications.

# Comparison Matrix

| Dimension | Ala’anzy et al. | Zhu et al. | Thesis interpretation |
| --- | --- | --- | --- |
| Research scope | Cross-domain architecture, capabilities and evaluation; reported 107 original studies plus contextual sources (pp. 9–11, 16–18). | Structured narrative orchestration survey with public-trace reanalysis and a small live illustration (pp. 5–7, 37–40, 54–56). | Use A for component vocabulary and Z for operational distinctions; do not pool their corpora as disjoint evidence. |
| Agent architecture | Profile, memory, planning, action and security are conceptual responsibilities (pp. 6, 13, 16). | Stateful graphs, roles, conversations, handoffs, artifacts and compiled pipelines are organizing abstractions (pp. 14–22). | Map each runtime’s responsibilities before designing adapters. |
| Orchestration approaches | Centralized, decentralized and hybrid authority (pp. 14–15). | Centralized, decentralized and hierarchical topology, independently static/adaptive (pp. 8–13). | Hybrid and adaptive are different properties. |
| Coordination strategies | Role specialization, negotiation, semantic and structured coordination (pp. 15, 20). | Task allocation, dependencies, recruitment and learned connectivity (pp. 5, 20, 28–29, 47–49). | Separate workflow execution from changes to the organization. |
| Memory management | Implicit, explicit and cross-episode agentic memory; update-validation concerns (pp. 19–20). | Shared/private state, checkpoints, sessions, roster/policy persistence and memory–coordination coupling (pp. 27–28, 47–48). | Distinguish task state from organizational knowledge and policy versions. |
| Communication protocols | General discussion of structured coordination and tool integration (pp. 15, 19–20). | Detailed historical MCP/A2A/ANP comparison and bridging discussion (pp. 22–27, 44). | Protocol scope helps design interfaces; verify current versions before implementation. |
| Agent interoperability | Notes inconsistent integration across frameworks (p. 19). | Examines capability discovery, task lifecycles and trust-boundary translation (pp. 23–28, 44). | Test semantics and recovery, not only transport exchange. |
| Reliability and fault tolerance | Compound uncertainty, distribution shift, limited deployment validation (pp. 28–31). | Failure layers, recovery controls, side-effect limits and small perturbation experiment (pp. 21, 29–31, 55–56). | A checkpoint and a retry do not by themselves provide exactly-once external effects. |
| Controlled self-improvement | Memory revision and learning; stability after repeated updates is underexamined (pp. 19–20). | Existing prompt/topology evolution, recruitment, transfer and continual learning methods (pp. 20, 47–49). | Investigate admission criteria, regression checks and rollback; self-evolution itself is prior work. |
| Evaluation | Six conceptual dimensions; no independent validation of the synthesis (pp. 17–18, 29–30). | Six different process/resource dimensions, three text-derived measures and three live telemetry measures across separate studies (pp. 35–40, 54–56). | Combine dimensions only through explicit definitions and a new evaluation protocol. |
| Research limitations | Search terminology, English/indexing, manual selection and secondary unreplicated results (pp. 29–30). | Approximate selection flow, single reviewer, proxy bias, heterogeneous benchmarks and simple tasks (pp. 6, 14, 38–40, 56). | Treat both as maps to primary literature, not proof of global novelty. |

Source attribution for all A cells: [@alaanzy2026autonomous, PDF §§3–10, pages specified in cells]. Source attribution for all Z cells: [@zhu2026orchestration, PDF §§3–10, Appendix B, pages specified in cells]. The last column is analyst synthesis.

# Evaluation Framework Crosswalk

| Evaluation concern | A: Table 8, pp. 17–18 | Z: Eqs. 1–6, pp. 35–36 | Interpretation |
| --- | --- | --- | --- |
| Task outcome | Task performance | Task performance | Requires matched tasks and success definitions. |
| Resource use | Efficiency | Coordination efficiency, scalability, cost efficiency | Z separates several mechanisms; cost/attempt is not cost/success. |
| Output quality | Quality | Partly represented in task scoring | No one-to-one correspondence. |
| Failure response | Robustness | Perturbed/baseline success | A conceptual label and a particular ratio are not equivalent protocols. |
| Safety | Explicit dimension | Discussed in threat analysis; not a separate metric in the six | Off-plan behavior cannot stand in for safety violations. |
| Interpretability | Explicit dimension | Process traces and emergent-behavior discussion | Trace availability is not a demonstration of causal explanation. |
| Emergent interaction | Discussed in collaboration | Off-plan message fraction, with retry density used as a proxy | Planned-edge violations and retry words measure different constructs. |

[@alaanzy2026autonomous, PDF pp. 17–18, 20, 29; A06, A08; @zhu2026orchestration, PDF pp. 29–31, 35–40; Z06, Z09]

# Shared Support and Differences

**Both support, at review level:** explicit attention to coordination, persistent information, evaluation beyond raw accuracy, and limits to comparing heterogeneous benchmark results. Agreement between two reviews is not independent experimental confirmation because their underlying literature may overlap. [@alaanzy2026autonomous, PDF pp. 19–20, 28–31; @zhu2026orchestration, PDF pp. 27–35]

**Detailed in only one of these texts:** A supplies a ten-domain capability map and an explicit security responsibility in its five-module architecture. Z supplies a layered protocol comparison, topology-by-adaptivity definitions, public-trace proxies, and a live perturbation harness. This is a difference of coverage, not proof that either framework cannot represent the other’s concerns. [@alaanzy2026autonomous, PDF pp. 13, 16–18; @zhu2026orchestration, PDF pp. 8–13, 22–27, 37–40, 54–56]

**Tension requiring preservation:** A emphasizes a lack of cross-domain benchmarks, while Z discusses limited cross-domain transfer evaluations and continual topology adaptation. These statements concern different scopes: existence of particular transfer experiments does not establish a widely adopted benchmark suite. Likewise Z’s §10.6 concerns six selected self-evolving systems, while §10.8 discusses additional systems. Avoid flattening either into “no transfer research exists.” [@alaanzy2026autonomous, PDF pp. 17–18, 28; @zhu2026orchestration, PDF pp. 47–49]

# What Has Not Been Demonstrated Here

Neither paper reports an end-to-end experiment combining heterogeneous runtimes, governed organizational knowledge, controlled policy promotion and reliable cross-session recovery in one implementation. A explicitly leaves its synthesis unvalidated; Z explicitly separates its trace and telemetry studies and defers cross-session tests. This corpus-bounded observation motivates [[Research-Gaps]]; it is not a field-wide novelty claim. [@alaanzy2026autonomous, PDF pp. 29–30; @zhu2026orchestration, PDF pp. 35, 37–38, 47–48]

# Implications for the Thesis

**Proposed synthesis:** begin with a fixed orchestrator, two different agent runtimes and versioned task/artifact contracts. Add organizational knowledge as a separately governed resource. Test one form of controlled update only after basic handoff and restart behavior is measurable. This provides separable experimental factors rather than attributing every improvement to a complete architecture.

Related: [[Agent-Orchestration]], [[Organizational-Memory]], [[Agent-Interoperability]], [[Controlled-Self-Improvement]], [[Agent-Evaluation]], [[Research-Gaps]].
