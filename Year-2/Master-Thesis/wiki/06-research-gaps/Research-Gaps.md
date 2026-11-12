---
type: research-gaps
title: Research Gaps and Testable Thesis Questions
status: ai-draft
updated: 2026-11-12
source_ids:
  - SRC-001
  - SRC-002
gap_status: hypotheses-requiring-literature-validation
reading_status: unread
---

# Status and Scope

These are **candidate gaps in the supplied two-paper evidence base**, not established absences across the field. Each research question and experiment below is analyst synthesis. Existing self-evolving and transfer methods discussed by Zhu et al. must be reviewed before making novelty claims. See [[Multi-Agent-Research-Comparison]] and [[Evidence-and-Uncertainties]].

# G1 — Cross-Framework Orchestration Semantics

**Problem and evidence:** Zhu distinguishes protocol integration layers but describes unresolved translation and resumption concerns; Ala’anzy notes inconsistent framework interoperability. Interface compatibility is therefore an insufficient outcome for the proposed system. [@zhu2026orchestration, PDF pp. 23–28, 44; Z04, Z05; @alaanzy2026autonomous, PDF p. 19]

**Why it matters:** a thesis about heterogeneous agents needs an explicit definition of what survives a runtime boundary.

**Research question:** Can a versioned task-and-artifact contract preserve completion, cancellation and failure semantics across two independently implemented agent runtimes?

**Proposed test:** compare direct custom integration with contract-based adapters on identical tasks; inject duplicate messages, incompatible artifact versions and worker restarts. Measure task completion, invalid state transitions, integration effort and recovery delay.

**Further review:** current versioned protocol specifications, conformance tests, workflow interchange, distributed task queues and cross-framework empirical studies. Refresh post-cutoff literature before declaring the bridge novel.

Related: [[Agent-Interoperability]], [[Agent-Orchestration]].

# G2 — Persistent Organizational Memory

**Problem and evidence:** agentic memory validation is weakly specified in A; Z describes persistent state/rosters/policies and entanglement between retrieval and coordination. Neither supplied paper evaluates a unified governance mechanism for reusable organizational knowledge. [@alaanzy2026autonomous, PDF p. 19; A04; @zhu2026orchestration, PDF pp. 27–28, 47–48; Z05]

**Why it matters:** retained information must remain interpretable after the original agent or session ends.

**Research question:** Does provenance-aware, versioned memory improve continuity across agent replacement without increasing harmful reuse of stale knowledge?

**Proposed test:** compare no cross-task memory, an unrestricted shared store, and governed memory. Change selected facts and replace workers between task episodes. Measure successful reuse, stale-answer rate, provenance completeness, retrieval cost and correction propagation.

**Further review:** organizational learning and organizational memory theory; continual/episodic agent memory; knowledge revision, temporal databases and retrieval evaluation. The working definition in [[Organizational-Memory]] must be reconciled with this broader literature.

# G3 — Knowledge Sharing Between Heterogeneous Agents

**Problem and evidence:** shared/private state and role-filtered messaging address access and context pressure, but do not establish that differently implemented agents interpret reusable knowledge equivalently. This is an inference from the described mechanisms. [@zhu2026orchestration, PDF pp. 21, 27–28; @alaanzy2026autonomous, PDF pp. 16, 19]

**Why it matters:** a common store can distribute contradictory or unusable artifacts as easily as useful ones.

**Research question:** Do typed, evidence-linked knowledge records reduce semantic loss and conflicting updates compared with free-text handoffs?

**Proposed test:** hold model budget constant and compare free text with structured records; introduce contradictory facts, inaccessible evidence and simultaneous edits. Measure receiver accuracy, unresolved conflicts, unauthorized disclosure and added latency.

**Further review:** ontology alignment, semantic interoperability, collaborative knowledge bases, access-control-aware retrieval and distributed consistency. These established fields may already provide appropriate mechanisms.

Related: [[Shared-Memory]], [[Agent-Communication]].

# G4 — Controlled Evolution of Agent Capabilities

**Problem and evidence:** A questions how self-revising memory is validated; Z surveys concrete self-evolving systems and reports limited evidence on stability, user-intent preservation and safeguard transfer. Existing recruitment and topology optimization must be treated as prior work. [@alaanzy2026autonomous, PDF pp. 19–20; A04; @zhu2026orchestration, PDF pp. 20, 47–49; Z11, Z12]

**Why it matters:** improvement on a local objective may coincide with regressions on earlier tasks or authority constraints.

**Research question:** Can an evaluation-and-promotion gate preserve prior-task performance and policy constraints while admitting useful prompt, skill or memory updates?

**Proposed test:** compare a frozen baseline, ungated updates and gated updates under a changing task stream. Separate development tasks from held-out acceptance tests. Record accepted/rejected changes, prior-task regressions, cost, unauthorized behavior and rollback effectiveness. Select one update type first to keep the thesis tractable.

**Further review:** the primary self-evolution studies cited in Z, continual learning, topology forgetting, safe policy improvement, regression selection and evaluation gaming. Review evidence that may already close this candidate gap.

Related: [[Controlled-Self-Improvement]], [[Agent-Evaluation]].

# G5 — Reliable Task Handoffs and Resumption

**Problem and evidence:** Z distinguishes internal state from external effects and identifies limited cross-runtime resumption evaluation. A highlights compounding failures and the gap between benchmark success and deployed reliability. [@zhu2026orchestration, PDF pp. 21, 28–29, 35, 48; Z05; @alaanzy2026autonomous, PDF pp. 28–31]

**Why it matters:** completing most of a task before losing state can waste work or duplicate an external action.

**Research question:** Which handoff invariants preserve task progress and avoid duplicate side effects across worker failure and process restart?

**Proposed test:** interrupt before a side effect, after the side effect but before acknowledgement, and after checkpointing. Compare ordinary retry with explicit attempt identity and idempotency/compensation. Measure duplicate effects, lost artifacts, resumption fidelity, partial progress and time to recovery.

**Further review:** durable workflow execution, idempotency keys, sagas, transactional messaging and checkpoint/replay. These are candidate foundations; an agent-specific contribution must be demonstrated beyond reimplementing known distributed-systems methods.

Related: [[Reliability-and-Fault-Tolerance]], [[Agent-Interoperability]].

# G6 — Validation and Auditability Across Changing Teams

**Problem and evidence:** A separates safety and interpretability from task performance. Z’s format-sensitive trace proxies cannot compare coordination overhead across frameworks and its small experiment does not test cross-session operation. [@alaanzy2026autonomous, PDF pp. 17–18, 29; A06, A08; @zhu2026orchestration, PDF pp. 35–40, 53–56; Z06–Z10]

**Why it matters:** missing telemetry can appear as zero failure or overhead, undermining claims about reliable orchestration.

**Research question:** Can a common event schema distinguish state drift, policy drift, missing observations and harmful updates across heterogeneous agents?

**Proposed test:** log task/attempt identifiers, artifact and policy versions, causal parent events and authority decisions; compare measurements with manually audited traces. Inject missing events and changed policies. Report trace completeness, agreement with human annotations, failure localization accuracy, runtime overhead and explicit “unobservable” outcomes.

**Further review:** primary MAST work and dataset annotation rules, distributed tracing, causal provenance, process mining and long-horizon agent benchmarks. Validate the metric construct before computing framework rankings.

Related: [[Agent-Evaluation]], [[Controlled-Self-Improvement]].

# Recommended Research Sequence

1. Resolve the highest-impact source uncertainties and review primary work on memory, failure analysis and self-evolution. Keep unread references on a reading queue, outside the analyzed bibliography.
2. Choose one measurable contribution: G2 plus G5 is a coherent memory-and-continuity foundation; G4 can be limited to one controlled update mechanism.
3. Specify a fixed task suite, two runtimes, a single-agent baseline, matched budgets, repeated trials and held-out tests.
4. Implement the minimal experiment and record both failures and improvements. Make any novelty claim only after a broader, updated search.

This sequence is a proposed study design, not a forecast of positive results. No thesis chapters are changed by these knowledge-base notes.
