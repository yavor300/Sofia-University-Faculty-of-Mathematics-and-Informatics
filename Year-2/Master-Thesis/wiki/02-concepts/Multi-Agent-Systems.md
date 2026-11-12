---
type: concept
title: Multi-Agent Systems
status: ai-draft
updated: 2026-11-12
source_ids:
  - SRC-001
  - SRC-002
citation_keys:
  - alaanzy2026autonomous
  - zhu2026orchestration
definition_status: source-grounded-synthesis
reading_status: unread
---

# Definition

A collective of agents whose interactions contribute to a shared or negotiated task. In this corpus, collaboration entails decisions about authority, roles, information exchange and failure recovery. [@alaanzy2026autonomous, PDF pp. 15–17, 20, 22, §§4.5, 5.2, 6.4, 7.1; A03, A05] [@zhu2026orchestration, PDF pp. 4–5, 20, 45, §§2, 5.7, 10.2; Z03]

# Technical Explanation

Agent specialization can distribute work, but the collective also needs dependency and consistency management. A collection of independent model calls is not evidence that useful collaboration has occurred. [@alaanzy2026autonomous, PDF pp. 15–17, 20, 22, §§4.5, 5.2, 6.4, 7.1; A03, A05] [@zhu2026orchestration, PDF pp. 4–5, 20, 45, §§2, 5.7, 10.2; Z03]

# Relevant Architectures and Mechanisms

The reviews discuss centralized, decentralized and hierarchical or hybrid organization, as well as role-specialized planning, execution and reflection. [@alaanzy2026autonomous, PDF pp. 15–17, 20, 22, §§4.5, 5.2, 6.4, 7.1; A03, A05] [@zhu2026orchestration, PDF pp. 4–5, 20, 45, §§2, 5.7, 10.2; Z03]

# Evidence from the Analyzed Papers

- [[Alaanzy-2026-Autonomous-Agents-Review]]: [@alaanzy2026autonomous, PDF pp. 15–17, 20, 22, §§4.5, 5.2, 6.4, 7.1; A03, A05]
- [[Zhu-2026-Multi-Agent-Orchestration]]: [@zhu2026orchestration, PDF pp. 4–5, 20, 45, §§2, 5.7, 10.2; Z03]

These are review-level accounts. Cited primary studies were not independently reviewed here. Proposed mechanisms in this article are analyst synthesis, not reported experimental results.

# Differences in Interpretation

Ala’anzy compares collaboration across domains; Zhu distinguishes workflow routing from changing the membership or structure of the collective. Their reported performance evidence does not demonstrate that adding agents is universally beneficial. [@alaanzy2026autonomous, PDF pp. 15–17, 20, 22, §§4.5, 5.2, 6.4, 7.1; A03, A05] [@zhu2026orchestration, PDF pp. 4–5, 20, 45, §§2, 5.7, 10.2; Z03]

# Relevance to the Thesis

**Analyst synthesis / proposed design:** Describe heterogeneity separately for models, tools, roles, frameworks and trust domains. Compare against a single-agent baseline before attributing gains to the collective.

# Related Concepts

[[Autonomous-AI-Agents]], [[Agent-Coordination]], [[Agent-Orchestration]]. See [[Multi-Agent-Research-Comparison]] and [[Evidence-and-Uncertainties]].

# Open Questions

**Research hypothesis requiring validation:** Under matched budgets, which tasks benefit from specialization, and when do coordination costs outweigh those benefits?

# Source Citations

[@alaanzy2026autonomous, PDF pp. 15–17, 20, 22, §§4.5, 5.2, 6.4, 7.1; A03, A05]

[@zhu2026orchestration, PDF pp. 4–5, 20, 45, §§2, 5.7, 10.2; Z03]

Full bibliographic metadata and local PDF links are in the two literature notes. The scope is the supplied PDF versions, not current framework documentation.
