# 11 — GPAI Model Technical Documentation Template (Annex XI / Annex XII)

**EU AI Act Reference:** Articles 53–55 | Annex XI | Annex XII | Article 51 (Systemic Risk)
**Applies to:** Providers of General-Purpose AI (GPAI) Models
**Retention Period:** Keep up to date throughout model lifecycle; available to EU AI Office on request
**Last Updated:** April 2026

---

## Purpose

Articles 53–55 impose a distinct set of obligations on providers of **General-Purpose AI (GPAI) models** — foundation models, large language models, and multimodal models that can be used for a wide range of downstream tasks. These obligations differ substantially from high-risk AI system requirements under Annex IV and require separate documentation under **Annex XI** (standard GPAI) and **Annex XII** (systemic risk GPAI).

This template covers both tiers. Complete Part A for all GPAI models. Complete Part B additionally if your model meets the systemic risk threshold (Article 51: >10²⁵ FLOPs training compute, or designated by EU AI Office).

---

## Document Control

| Field | Entry |
|---|---|
| Document Title | GPAI Technical Documentation — [Model Name] |
| Model ID | |
| Version / Release | |
| Classification | CONFIDENTIAL / RESTRICTED |
| Author | |
| Approved By | |
| Approval Date | |
| Review Date | |
| Document Status | Draft / Under Review / Approved / Superseded |
| Systemic Risk Designation | Yes (>10²⁵ FLOPs or EU AI Office designation) / No |

---

## PART A — Standard GPAI Model Documentation (Annex XI, all GPAI providers)

### A1 — General Description of the Model

#### A1.1 Model Identity

| Field | Detail |
|---|---|
| Model name and version | |
| Model family (if applicable) | |
| Provider name and address | |
| EU Authorised Representative (if non-EU provider) | |
| Model type | LLM / Multimodal / Diffusion / Other: |
| Modalities supported | Text / Image / Audio / Video / Code / Other: |
| Parameter count (approximate) | |
| Context window / input length | |
| Release date | |
| Deployment form | API / Open weights / Embedded / Other: |
| Open source? | Yes / No — Licence: |

#### A1.2 Intended Use and Downstream Applications

Describe the intended purposes for which the GPAI model is placed on the market, including the tasks it is designed to perform and the reasonably foreseeable downstream use cases:

[Describe general intended use — e.g. text generation, code completion, question answering, image generation, etc.]

**Reasonably foreseeable downstream high-risk use cases:**

| Downstream Use | Annex III Category | Risk Notes |
|---|---|---|
| | | |
| | | |

**Uses the provider explicitly prohibits (acceptable use policy reference):**

[List prohibited uses and reference to acceptable use policy document]

#### A1.3 Model Architecture

| Field | Detail |
|---|---|
| Architecture type | Transformer / Diffusion / MoE / Other: |
| Number of layers | |
| Attention heads | |
| Training objective | Autoregressive / Masked / RLHF / Other: |
| Fine-tuning applied? | Yes (describe) / No |
| Instruction tuning / RLHF / RLAIF applied? | Yes (describe) / No |
| Architecture diagram or reference | [Attach / Link] |

---

### A2 — Training Data (Annex XI, Section 2)

#### A2.1 Training Data Overview

| Field | Detail |
|---|---|
| Total training data volume | Tokens / GB / TB |
| Data collection date range | |
| Languages represented | |
| Primary data sources | |
| Pre-training data description | |
| Fine-tuning / RLHF data description (if applicable) | |

#### A2.2 Data Sources Breakdown

| Source | Type | Volume (approx.) | Licence / Rights Basis | Personal Data? | Special Category Data? |
|---|---|---|---|---|---|
| | Web crawl | | | ☐ Yes / ☐ No | ☐ Yes / ☐ No |
| | Licensed dataset | | | ☐ Yes / ☐ No | ☐ Yes / ☐ No |
| | Books / publications | | | ☐ Yes / ☐ No | ☐ Yes / ☐ No |
| | Code repositories | | | ☐ Yes / ☐ No | ☐ Yes / ☐ No |
| | Synthetic data | | | ☐ Yes / ☐ No | ☐ Yes / ☐ No |
| | Other: | | | ☐ Yes / ☐ No | ☐ Yes / ☐ No |

#### A2.3 EU Copyright Compliance (Article 53(1)(c))

Providers must maintain a policy to comply with EU copyright law, including Directive 2019/790 on Copyright in the Digital Single Market.

| Requirement | Status | Evidence |
|---|---|---|
| Text and data mining (TDM) opt-out reservations identified and honoured | ☐ Done / ☐ Pending | |
| Process in place to identify and exclude opt-out content | ☐ Done / ☐ Pending | |
| Records of rights assessments maintained | ☐ Done / ☐ Pending | |
| Copyright compliance policy documented | ☐ Done / ☐ Pending | Reference: |

#### A2.4 Training Data Summary for Public Disclosure (Article 53(1)(d))

Article 53 requires providers to publish a sufficiently detailed summary of the content used for training. This section provides the basis for that summary.

**Summary (suitable for publication):**

> [Model Name] was trained on approximately [X] tokens of data drawn from [general description of sources — e.g. publicly available web text, licensed books, code repositories, and curated datasets]. Training data collection spanned [date range]. The dataset includes content in [N] languages. [Describe any filtering, deduplication, or quality measures applied.]

---

### A3 — Training Process

#### A3.1 Compute and Infrastructure

| Field | Detail |
|---|---|
| Training compute (FLOPs, approximate) | |
| Training infrastructure | Cloud / On-premise / Hybrid |
| Hardware used | GPU type / TPU / Other |
| Training duration | |
| Energy consumption (MWh, approximate) | |
| Carbon footprint (tCO₂e, if measured) | |

> **Systemic Risk Threshold Check:** If training compute exceeds **10²⁵ FLOPs**, the model is presumed to have systemic risk under Article 51. Complete Part B of this document.

#### A3.2 Training Methodology

| Field | Detail |
|---|---|
| Pre-training objective | |
| Optimisation algorithm | |
| Batch size | |
| Learning rate schedule | |
| Data parallelism / model parallelism approach | |
| Regularisation techniques | |
| Safety training applied (RLHF, Constitutional AI, etc.) | Yes (describe) / No |

---

### A4 — Evaluation and Testing (Annex XI, Section 4)

#### A4.1 Capability Evaluations

| Benchmark / Evaluation | Score / Result | Comparison Baseline | Notes |
|---|---|---|---|
| | | | |
| | | | |

#### A4.2 Limitations

Describe known limitations of the model, including circumstances under which it may perform poorly or produce unreliable outputs:

| Limitation | Description | Impact | Mitigation |
|---|---|---|---|
| Hallucination / factual errors | | High | |
| Bias in outputs | | Medium–High | |
| Language / dialect gaps | | Medium | |
| Temporal knowledge cutoff | Date: | Medium | |
| Context window limits | | Low–Medium | |
| Other: | | | |

#### A4.3 Safety and Misuse Evaluations

| Evaluation Type | Conducted? | Result Summary | Evidence |
|---|---|---|---|
| Harmful content generation testing | ☐ Yes / ☐ No | | |
| Bias and fairness testing | ☐ Yes / ☐ No | | |
| Privacy leakage / memorisation testing | ☐ Yes / ☐ No | | |
| Jailbreak / prompt injection testing | ☐ Yes / ☐ No | | |
| Dual-use / CBRN risk assessment | ☐ Yes / ☐ No | | |
| Disinformation risk assessment | ☐ Yes / ☐ No | | |

---

### A5 — Information for Downstream Providers (Article 53(1)(b))

GPAI model providers must provide downstream providers (who build applications on top of the model) with sufficient information to enable their own compliance.

#### A5.1 Downstream Provider Information Package

| Document / Information | Available? | Format | Access Method |
|---|---|---|---|
| Model card | ☐ Yes / ☐ No | | |
| System card | ☐ Yes / ☐ No | | |
| API documentation | ☐ Yes / ☐ No | | |
| Acceptable use policy | ☐ Yes / ☐ No | | |
| Known limitations disclosure | ☐ Yes / ☐ No | | |
| Safety guidance for deployment | ☐ Yes / ☐ No | | |
| Fine-tuning guidance and restrictions | ☐ Yes / ☐ No | | |
| Data provenance summary | ☐ Yes / ☐ No | | |

#### A5.2 Contractual Obligations on Downstream Providers

Describe any contractual or terms-of-service obligations placed on downstream providers to ensure responsible deployment:

[Describe — e.g. prohibitions on high-risk use without additional safeguards, requirement to maintain acceptable use policies, etc.]

---

### A6 — Post-Training Safety Measures

| Measure | Implemented? | Description |
|---|---|---|
| Output filtering / content moderation | ☐ Yes / ☐ No | |
| Refusal training for harmful requests | ☐ Yes / ☐ No | |
| Watermarking of AI-generated content | ☐ Yes / ☐ No | |
| Rate limiting / abuse detection | ☐ Yes / ☐ No | |
| User reporting mechanism | ☐ Yes / ☐ No | |
| Incident monitoring and logging | ☐ Yes / ☐ No | |

---

## PART B — Systemic Risk GPAI Model Documentation (Annex XII — Article 51 models only)

> Complete this section **only** if your model has training compute >10²⁵ FLOPs or has been designated as systemic risk by the EU AI Office under Article 51(2).

### B1 — Systemic Risk Assessment

| Field | Entry |
|---|---|
| Basis for systemic risk designation | FLOPs threshold / EU AI Office designation / Both |
| Training compute (FLOPs) | |
| EU AI Office designation reference (if applicable) | |
| Date of designation | |

#### B1.1 Systemic Risk Categories

Assess the model's potential contribution to each systemic risk category:

| Risk Category | Risk Level | Justification | Mitigation |
|---|---|---|---|
| Misuse for CBRN weapons development | 🟢 / 🟡 / 🟠 / 🔴 | | |
| Large-scale cyberattacks / critical infrastructure attacks | 🟢 / 🟡 / 🟠 / 🔴 | | |
| Large-scale disinformation / manipulation campaigns | 🟢 / 🟡 / 🟠 / 🔴 | | |
| Undermining democratic processes | 🟢 / 🟡 / 🟠 / 🔴 | | |
| Widespread discriminatory outcomes at societal scale | 🟢 / 🟡 / 🟠 / 🔴 | | |
| Irreversible societal or environmental harm | 🟢 / 🟡 / 🟠 / 🔴 | | |

---

### B2 — Adversarial Testing / Red-Teaming (Article 55(1)(a))

Providers of systemic risk GPAI models must perform adversarial testing (red-teaming) to identify and mitigate systemic risks.

| Field | Detail |
|---|---|
| Red-team exercise conducted? | ☐ Yes / ☐ No |
| Date(s) of red-team exercise | |
| Conducted by | Internal team / Independent third party / Both |
| Third-party assessor name (if applicable) | |
| Scope of red-teaming | |
| Critical findings summary | |
| Mitigations implemented | |
| Follow-up red-team scheduled? | ☐ Yes — Date: / ☐ No |

Red-Team Exercise Log:

| Exercise ID | Date | Assessor | Scope | Findings | Severity | Mitigated? |
|---|---|---|---|---|---|---|
| RT-001 | | | | | | ☐ Yes / ☐ No |

---

### B3 — Serious Incident Reporting (Article 55(1)(b))

Providers of systemic risk GPAI models must report serious incidents to the EU AI Office without undue delay.

| Incident Reporting Requirement | Status |
|---|---|
| Incident monitoring system established | ☐ Done / ☐ Pending |
| EU AI Office reporting procedure documented | ☐ Done / ☐ Pending |
| Internal incident classification criteria defined | ☐ Done / ☐ Pending |
| Contact point designated for EU AI Office communications | ☐ Done / ☐ Pending |

**EU AI Office Contact:** [https://digital-strategy.ec.europa.eu/en/policies/ai-office](https://digital-strategy.ec.europa.eu/en/policies/ai-office)

Serious Incident Log:

| Incident ID | Date | Description | Severity | Reported to EU AI Office? | Date Reported | Resolution |
|---|---|---|---|---|---|---|
| INC-001 | | | | ☐ Yes / ☐ No | | |

---

### B4 — Cybersecurity Measures (Article 55(1)(c))

| Measure | Implemented? | Description |
|---|---|---|
| Model weights access controls | ☐ Yes / ☐ No | |
| API authentication and rate limiting | ☐ Yes / ☐ No | |
| Protection against model extraction/theft | ☐ Yes / ☐ No | |
| Infrastructure security (SOC 2 / ISO 27001 / equivalent) | ☐ Yes / ☐ No | Reference: |
| Penetration testing of model serving infrastructure | ☐ Yes / ☐ No | |
| Supply chain security (training pipeline) | ☐ Yes / ☐ No | |
| Insider threat controls | ☐ Yes / ☐ No | |

---

### B5 — Energy Efficiency Reporting (Article 55(1)(d))

| Field | Value |
|---|---|
| Training energy consumption (MWh) | |
| Inference energy per query (Wh, approximate) | |
| Total annual inference energy (MWh, estimated) | |
| Data centre PUE | |
| Renewable energy percentage | |
| Carbon intensity of compute (gCO₂/kWh) | |
| Reporting standard used | |

---

### B6 — Codes of Practice (Article 56)

| Field | Entry |
|---|---|
| Signed up to EU AI Office GPAI Code of Practice? | ☐ Yes / ☐ No / ☐ In progress |
| Code of Practice version / date | |
| Compliance assessment completed? | ☐ Yes / ☐ No |
| Areas of non-compliance identified | |
| Remediation plan | |

---

## Document Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| GPAI Model Owner / Provider Representative | | | |
| Legal / Compliance | | | |
| AI Safety Lead | | | |
| EU Authorised Representative (if non-EU provider) | | | |

**Next Review Date:** _______________
**Review Triggers:** Model update / New version release / EU AI Office guidance update / Systemic risk redesignation

---

*Part of the EU AI Act Compliance Toolkit*
