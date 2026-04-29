# 27 — GPAI Systemic Risk Compliance Guide
## EU AI Act Compliance Toolkit | v3.2.0 | April 2026
### Regulatory Reference: Articles 51, 53–56, Annex XIII | Applicable from: 2 August 2025

---

## Purpose and Scope

This document addresses the **systemic risk obligations** that apply to providers of General-Purpose AI (GPAI) models that have been designated as posing **systemic risk** under Articles 51 and 55–56 of Regulation (EU) 2024/1689.

**This document supplements Doc 11 (GPAI Technical Documentation).** Doc 11 covers the baseline obligations for all GPAI model providers (Articles 53–54). This document addresses the **additional, elevated obligations** triggered only when a GPAI model meets the systemic risk threshold.

**Relationship to other documents:**
- Doc 11: All GPAI baseline obligations (training data, model card, transparency, copyright policy, incidents)
- Doc 27 (this document): Systemic risk-specific obligations (Arts. 55-56) — adversarial testing, enhanced incident reporting, cybersecurity, model evaluation, post-training measures
- Doc 08: Incident reporting procedure (applies to all GPAI, but Art. 56 imposes enhanced obligations for systemic risk models)

---

## Part 1 — Systemic Risk Classification

### 1.1 What is a GPAI Model with Systemic Risk?

A GPAI model is classified as having **systemic risk** when it meets one or more of the following criteria under Article 51:

| Criterion | Threshold | Reference |
|---|---|---|
| **Training compute threshold** | ≥ 10²⁵ floating point operations (FLOPs) used in training | Art. 51(1)(a) |
| **EU AI Office designation** | The EU AI Office, on its own initiative or following a qualified-alert submission, designates the model as posing systemic risk based on its capabilities | Art. 51(1)(b) |

**Note on the compute threshold:** The 10²⁵ FLOP threshold is a rebuttable presumption for systemic risk classification. A provider whose model meets the threshold may request a reassessment by the EU AI Office if the model does not actually have the capabilities that would constitute systemic risk (Article 51(3)).

**Note on designation:** The EU AI Office may designate models below the compute threshold as systemic risk based on evaluated capabilities, including: high degree of generality, capability to perform a wide range of distinct tasks, potential for broad impact across value chains, reach to a large number of users, or demonstrated capabilities in critical areas (cybersecurity, CBRN, critical infrastructure).

### 1.2 Systemic Risk Determination

| Field | Detail |
|---|---|
| GPAI model name | |
| Model version | |
| Training compute (estimated FLOPs) | |
| Compute threshold met (≥ 10²⁵ FLOPs)? | ☐ YES ☐ NO ☐ UNCERTAIN |
| EU AI Office designation received? | ☐ YES ☐ NO — If YES, date: |
| Systemic risk classification confirmed? | ☐ YES ☐ NO ☐ PENDING |

**If Systemic Risk = NO:** Use Doc 11 only. Do not proceed with this document.
**If Systemic Risk = YES or PENDING:** Complete all sections of this document.

### 1.3 Rebuttable Presumption Process (if applicable)

If the compute threshold is met but you believe the model does not pose systemic risk:

| Step | Action | Status |
|---|---|---|
| 1 | Prepare technical justification demonstrating absence of systemic risk capabilities | ☐ |
| 2 | Submit request for reassessment to EU AI Office via single information point | ☐ |
| 3 | Await EU AI Office determination | ☐ |
| 4 | If determination confirms systemic risk: implement all Art. 55-56 obligations | ☐ |
| 5 | If determination confirms no systemic risk: retain documentation of process | ☐ |

*Justification narrative:* _______________________________________________

---

## Part 2 — Article 55 Obligations: Mandatory Systemic Risk Measures

Article 55 imposes four mandatory obligations on providers of GPAI models with systemic risk. All must be implemented before the model is made available.

### 2.1 Obligation 1 — Adversarial Testing (Red-Teaming)
**Article 55(1)(a) | Annex XIII**

#### 2.1.1 What is Required

Providers must conduct **model evaluations in accordance with standardised protocols and tools** reflecting the state of the art. This includes adversarial testing ("red-teaming") to identify and mitigate systemic risks, including safety and security risks.

The EU AI Office will develop and maintain standardised evaluation protocols through Article 56(3). Until then, providers must follow the state of the art in model evaluation.

#### 2.1.2 Adversarial Testing Plan

| Field | Detail |
|---|---|
| Red-team exercise name/ID | |
| Model version tested | |
| Testing organisation (internal/external/both) | |
| External red-team engaged? | ☐ YES ☐ NO — Name: |
| Date of testing | |
| Next scheduled testing | |

#### 2.1.3 Adversarial Testing Coverage

The following risk areas must be covered in adversarial testing for systemic risk GPAI models:

| Risk Domain | Test Scenarios Developed | Tests Executed | Critical Findings | Mitigated? |
|---|---|---|---|---|
| **CBRN uplift** — Does the model provide meaningful technical uplift to development of chemical, biological, radiological, or nuclear weapons? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Cyberoffensive capabilities** — Can the model generate functional exploit code, malware, or novel cyberattack techniques? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Critical infrastructure attack** — Can the model provide actionable guidance on attacking power grids, water systems, financial infrastructure, transport networks? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Disinformation at scale** — Can the model generate highly convincing, scalable disinformation including synthetic media (deepfakes, fake news, fabricated evidence)? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Autonomous harmful action** — Can the model act autonomously in ways that could cause serious, widespread harm without human oversight? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Safety bypass** — Can the model be jailbroken, manipulated, or fine-tuned to circumvent safety measures? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Bias and discrimination at scale** — Does the model systematically generate biased, discriminatory, or harmful content about protected groups? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Privacy violation at scale** — Does the model memorise, reproduce, or enable inference of personal data at scale? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |

#### 2.1.4 Red-Team Findings Summary

| Finding ID | Risk Domain | Severity | Description | Mitigation Implemented | Residual Risk |
|---|---|---|---|---|---|
| | | ☐ Critical ☐ High ☐ Medium ☐ Low | | | |
| | | ☐ Critical ☐ High ☐ Medium ☐ Low | | | |
| | | ☐ Critical ☐ High ☐ Medium ☐ Low | | | |

#### 2.1.5 Red-Team Exercise Sign-Off

| Role | Name | Organisation | Date | Signature |
|---|---|---|---|---|
| Red-Team Lead | | | | |
| Model Safety Officer | | | | |
| Head of Compliance | | | | |

---

### 2.2 Obligation 2 — Incident Reporting (Enhanced Obligations)
**Article 55(1)(b) + Article 73(1) + Article 56**

#### 2.2.1 Standard vs. Enhanced Obligations

All GPAI model providers must report serious incidents (Art. 73, covered in Doc 08). Providers of systemic risk GPAI models have **additional reporting obligations**:

| Obligation | All GPAI Providers | Systemic Risk GPAI Providers |
|---|---|---|
| Report serious incidents to EU AI Office | ☐ Required (Doc 08) | ☐ Required (Doc 08) |
| Report serious incidents without undue delay | ☐ Required | ☐ Required |
| Report near-misses (incidents that did not materialise but could have) | Not required | ☐ Required under Art. 55(1)(b) |
| Cooperate with EU AI Office investigations | ☐ Required | ☐ Required (enhanced) |
| Provide model evaluations to EU AI Office on request | Not required | ☐ Required under Art. 56(1) |

#### 2.2.2 Systemic Risk Incident Categories

For systemic risk GPAI models, the following constitute reportable incidents or near-misses:

| Category | Description | Immediate Action | Reporting Timeline |
|---|---|---|---|
| CBRN misuse | Model used to provide material uplift to CBRN weapons development | Restrict model access; preserve logs | Without undue delay (≤ 72 hours) |
| Cyber attack enablement | Model used to generate functional malware or exploits used in an actual attack | Restrict output capabilities; preserve logs | Without undue delay (≤ 72 hours) |
| Disinformation campaign | Model used to generate content that materially influenced a democratic process or caused widespread public harm | Document outputs; preserve logs; notify relevant authorities | Without undue delay (≤ 72 hours) |
| Critical infrastructure | Model-derived guidance used in an actual attack on critical infrastructure | Emergency protocol; contact national CSIRT; notify EU AI Office | Within 24 hours |
| Safety bypass at scale | Jailbreak technique exploited in production affecting more than 1,000 users | Deploy patch/safeguard; communicate to downstream providers | Without undue delay (≤ 72 hours) |
| Personal data breach at scale | Model memorisation or generation exposes personal data of more than 1,000 identified individuals | GDPR Art. 33 notification (72 hours to DPA); notify EU AI Office | Parallel GDPR + AI Act reporting |

#### 2.2.3 Systemic Risk Incident Register

| Incident ID | Date Detected | Category | Description | Persons Affected | EU AI Office Notified (date) | Action Taken | Status |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |

---

### 2.3 Obligation 3 — Cybersecurity Measures
**Article 55(1)(c)**

Providers of systemic risk GPAI models must ensure **adequate cybersecurity protection** for the model, its training infrastructure, and associated services.

#### 2.3.1 Cybersecurity Risk Assessment

| Asset | Threat | Likelihood | Impact | Current Controls | Residual Risk | Acceptable? |
|---|---|---|---|---|---|---|
| Model weights | Theft/exfiltration | | | | | ☐ YES ☐ NO |
| Training data | Poisoning attack | | | | | ☐ YES ☐ NO |
| Training infrastructure | Compromise | | | | | ☐ YES ☐ NO |
| Inference API | DDoS / availability | | | | | ☐ YES ☐ NO |
| Inference API | Adversarial input at scale | | | | | ☐ YES ☐ NO |
| Fine-tuning pipeline | Malicious fine-tune | | | | | ☐ YES ☐ NO |
| System prompts | Extraction / leakage | | | | | ☐ YES ☐ NO |
| Downstream provider access | Abuse / misuse | | | | | ☐ YES ☐ NO |

#### 2.3.2 Cybersecurity Minimum Controls

| Control | Implemented? | Evidence |
|---|---|---|
| Model weights stored with encryption at rest (AES-256 or equivalent) | ☐ YES ☐ NO ☐ N/A | |
| Model weights access restricted to authorised personnel with MFA | ☐ YES ☐ NO | |
| Training infrastructure isolated from public internet during training runs | ☐ YES ☐ NO | |
| Training data integrity verification (cryptographic hashing / signing) | ☐ YES ☐ NO | |
| Inference API protected by authentication and rate limiting | ☐ YES ☐ NO | |
| Anomaly detection on inference API inputs (adversarial input detection) | ☐ YES ☐ NO | |
| Downstream provider access governed by API terms with abuse clauses | ☐ YES ☐ NO | |
| Penetration testing conducted (at least annually) | ☐ YES ☐ NO | |
| Security incident response plan covering model-specific scenarios | ☐ YES ☐ NO | |
| Supply chain security assessment (third-party model components, open-source dependencies) | ☐ YES ☐ NO | |

#### 2.3.3 Most Recent Security Assessment

| Assessment Type | Conducted By | Date | Key Findings | Remediation Status |
|---|---|---|---|---|
| Penetration test | | | | |
| Red-team (security) | | | | |
| Supply chain audit | | | | |
| Threat model review | | | | |

---

### 2.4 Obligation 4 — EU AI Office Model Evaluation Cooperation
**Article 55(1)(d) + Article 56**

Providers must cooperate with the EU AI Office, including by providing access to models for evaluation on request.

#### 2.4.1 Cooperation Obligations

| Obligation | Reference | Status |
|---|---|---|
| Provide model access to EU AI Office for evaluation upon request | Art. 56(1)(a) | ☐ Process documented ☐ Not documented |
| Provide model documentation, training data information, and testing results upon request | Art. 56(1)(b) | ☐ Process documented ☐ Not documented |
| Implement remediation measures notified by EU AI Office within specified timeframe | Art. 56(1)(c) | ☐ Process documented ☐ Not documented |
| Participate in EU AI Office mandated evaluations | Art. 56(2) | ☐ Process documented ☐ Not documented |

#### 2.4.2 EU AI Office Interaction Log

| Date | Nature of Interaction | Request/Direction Received | Response Provided | Status |
|---|---|---|---|---|
| | | | | |
| | | | | |

#### 2.4.3 Internal Process for EU AI Office Requests

Document the internal process for handling EU AI Office evaluation requests:

| Step | Action | Owner | Timeline |
|---|---|---|---|
| 1 | Receive and log EU AI Office request | Legal/Compliance Lead | Day 0 |
| 2 | Assess scope of request (model access, documentation, evaluation) | Technical Lead + Legal | Day 1-2 |
| 3 | Brief executive team; identify legal privilege considerations | Legal Counsel | Day 2-3 |
| 4 | Prepare and provide requested materials or access | Technical Lead | Per request timeline |
| 5 | Document all materials provided and access granted | Compliance Lead | Ongoing |
| 6 | Implement any remediation measures directed by EU AI Office | Technical Lead | Per directed timeline |

---

## Part 3 — Article 56: Additional Systemic Risk Management

Article 56 gives the EU AI Office additional investigatory and corrective powers over systemic risk GPAI models.

### 3.1 EU AI Office Powers — Awareness Checklist

| Power | Article | Provider Obligation |
|---|---|---|
| Request documentation, training data, testing, and model access | Art. 56(1) | Must comply within directed timeframe |
| Mandate model evaluations by qualified external experts | Art. 56(2) | Must cooperate; provide access |
| Issue corrective measures or restrictions | Art. 56(3) | Must implement; report on implementation |
| Require model modification, withdrawal, or restriction from market | Art. 56(4) | Must comply immediately |
| Publish information about systemic risk models (subject to confidentiality) | Art. 56(6) | Must not obstruct; provide factual corrections if incorrect |

### 3.2 Post-Training Risk Mitigation Measures

Article 55 requires providers to take post-training measures where needed to address systemic risks identified through adversarial testing or model evaluation.

#### Post-Training Measure Types

| Measure Type | Description | When Used |
|---|---|---|
| **Safety fine-tuning** | Additional fine-tuning to improve safety, reduce harmful outputs, or address identified capability misuse | When red-team identifies significant harmful capability gap |
| **Capability restrictions** | Modifying system prompts, RLHF reward signals, or output filters to restrict specific dangerous capabilities | When capability cannot be safely deployed without restriction |
| **Output filtering** | Post-generation filtering to prevent specific harmful content categories | When real-time generation cannot be fully controlled |
| **Access controls** | Restricting model access to vetted downstream providers or use cases | When general availability poses unacceptable systemic risk |
| **Watermarking** | Implementing AI-generated content watermarking per Article 50(2) | When disinformation risk is material |
| **Retrieval restriction** | Preventing retrieval-augmented generation from specific dangerous data sources | When RAG pipeline creates dangerous capability uplift |

#### Post-Training Measures Register

| Measure ID | Measure Type | Risk Addressed | Implementation Date | Verification Method | Effective? |
|---|---|---|---|---|---|
| | | | | | ☐ YES ☐ NO ☐ TBD |
| | | | | | ☐ YES ☐ NO ☐ TBD |
| | | | | | ☐ YES ☐ NO ☐ TBD |

---

## Part 4 — Systemic Risk Governance

### 4.1 Governance Structure

| Role | Name | Responsibilities |
|---|---|---|
| Model Safety Officer | | Overall accountability for systemic risk compliance; EU AI Office liaison |
| Head of Red-Team | | Plans and executes adversarial testing programme |
| CISO | | Cybersecurity measures; security incident response |
| Head of Compliance | | Regulatory compliance; documentation; incident reporting |
| Legal Counsel | | EU AI Office cooperation; remediation advice; privilege |
| Downstream Provider Manager | | Manages API access; enforces terms of use; monitors abuse |

### 4.2 Downstream Provider Management

Systemic risk GPAI models made available to downstream providers (via API or open weights) require particular controls:

| Control | Implemented? | Details |
|---|---|---|
| Terms of use explicitly prohibit uses that could contribute to systemic risk | ☐ YES ☐ NO | |
| Downstream providers screened and vetted before API access granted | ☐ YES ☐ NO | |
| Downstream provider monitoring programme in place (audit rights, usage logs) | ☐ YES ☐ NO | |
| Process for revoking downstream provider access upon misuse | ☐ YES ☐ NO | |
| Downstream providers notified of systemic risk classification and model capabilities | ☐ YES ☐ NO | |
| Downstream providers required to implement safeguards in their use cases | ☐ YES ☐ NO | |

### 4.3 Annual Systemic Risk Review

The systemic risk obligations under Article 55 must be reviewed at least annually, and whenever a material change occurs to the model.

| Review Trigger | Date | Changes Identified | Updates Made | Approved By |
|---|---|---|---|---|
| Annual review | | | | |
| New model version | | | | |
| New red-team findings | | | | |
| EU AI Office direction | | | | |
| Significant incident | | | | |

---

## Part 5 — Voluntary Commitments and Codes of Practice

The EU AI Act encourages GPAI model providers (including systemic risk providers) to participate in voluntary Codes of Practice developed under Article 56(5). As of April 2026, the EU AI Office has been leading development of GPAI Codes of Practice with major model providers.

| Commitment | Status |
|---|---|
| Participation in EU AI Office GPAI Code of Practice development | ☐ Participating ☐ Not participating ☐ Monitoring |
| Signed GPAI Code of Practice (once finalised) | ☐ YES ☐ NO ☐ Pending |
| Voluntary safety commitments with EU AI Office | ☐ YES ☐ NO — describe: |
| Membership in AI safety standards body (e.g., ISO SC 42, CEN/CENELEC JTC 21) | ☐ YES ☐ NO |

---

## Part 6 — Systemic Risk Compliance Summary

### 6.1 Article 55 Compliance Checklist

| Obligation | Reference | Status | Evidence |
|---|---|---|---|
| Adversarial testing (red-teaming) conducted | Art. 55(1)(a) | ☐ Complete ☐ In Progress ☐ Not Started | |
| Systemic risk incidents and near-misses reported to EU AI Office | Art. 55(1)(b) | ☐ Process in place ☐ Pending | |
| Cybersecurity measures implemented | Art. 55(1)(c) | ☐ Complete ☐ In Progress ☐ Not Started | |
| EU AI Office evaluation cooperation process documented | Art. 55(1)(d) | ☐ Complete ☐ In Progress ☐ Not Started | |
| Post-training mitigation measures implemented where identified | Art. 55(2) | ☐ Complete ☐ N/A ☐ In Progress | |

### 6.2 Systemic Risk Compliance Sign-Off

| Field | Detail |
|---|---|
| Model name | |
| Model version | |
| Systemic risk designation confirmed | ☐ YES (compute threshold) ☐ YES (EU AI Office designation) |
| All Art. 55 obligations complete | ☐ YES ☐ NO — open items: |
| Date of compliance sign-off | |
| Next review date | |

| Role | Name | Date | Signature |
|---|---|---|---|
| Model Safety Officer | | | |
| Head of Compliance | | | |
| Legal Counsel | | | |
| CEO / Chief AI Officer | | | |

---

## Appendix A — Key Definitions

| Term | Definition | Reference |
|---|---|---|
| GPAI Model | AI model trained with a large amount of data using self-supervision at scale, exhibiting significant generality and capably performing a wide range of distinct tasks | Art. 3(63) |
| GPAI Model with Systemic Risk | GPAI model with high-impact capabilities or cumulative effects that present or could present systemic risks | Art. 3(65) + Art. 51 |
| Systemic Risk | Risk that is specific to the high-impact capabilities of GPAI models, having a significant impact on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or society as a whole | Art. 3(66) |
| Adversarial Testing | Structured evaluation process to identify risks, vulnerabilities, and safety concerns in AI systems by simulating adversarial conditions, including "red-teaming" | Annex XIII |
| Downstream Provider | Provider who develops AI systems or AI models built upon the GPAI model | Art. 3(68) |

---

## Appendix B — Regulatory Timeline for GPAI Systemic Risk

| Date | Event |
|---|---|
| 1 August 2024 | EU AI Act entered into force |
| 2 August 2025 | **GPAI model obligations (including Arts. 55-56) become applicable** |
| Ongoing | EU AI Office develops standardised evaluation protocols (Art. 56(3)) |
| Ongoing | EU AI Office maintains list of GPAI models with systemic risk (Art. 51(4)) |
| TBD | GPAI Code of Practice finalised |

---

## Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | April 2026 | Initial release — complete Arts. 55-56 systemic risk compliance framework | Toolkit Team |

---

*This document does not constitute legal advice. The systemic risk framework for GPAI models is subject to ongoing development through EU AI Office guidance, standardised evaluation protocols, and GPAI Codes of Practice. Always seek qualified legal counsel for binding compliance determinations. Monitor EU AI Office publications for updated guidance.*
