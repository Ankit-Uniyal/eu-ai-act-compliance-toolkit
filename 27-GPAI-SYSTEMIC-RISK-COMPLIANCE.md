# 27: GPAI Systemic Risk Compliance Guide
## EU AI Act Compliance Toolkit | v3.2.0 | April 2026
### Regulatory Reference: Articles 51, 53-56, 88-94, Annex XIII | Applicable from: 2 August 2025

---

## Purpose and Scope

This document addresses the **systemic risk obligations** that apply to providers of General-Purpose AI (GPAI) models that have been designated as posing **systemic risk** under Articles 51 and 55 of Regulation (EU) 2024/1689, together with the EU-level supervision and enforcement powers in Articles 88-94.

> **Tip:** the Safety and Security chapter of the EU AI Office's [GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) sets out state-of-the-art practices for managing systemic risk, and is the endorsed way to show compliance with Article 55.

**This document supplements Doc 11 (GPAI Technical Documentation).** Doc 11 covers the baseline obligations for all GPAI model providers (Articles 53-54). This document addresses the **additional, elevated obligations** triggered only when a GPAI model meets the systemic risk threshold.

**Relationship to other documents:**
- Doc 11: All GPAI baseline obligations (training data, model card, transparency, copyright policy, energy/compute documentation, incidents)
- Doc 27 (this document): Systemic risk-specific obligations (Art. 55), model evaluation/adversarial testing, systemic-risk assessment & mitigation, enhanced incident reporting, cybersecurity, plus EU supervision/enforcement (Arts. 88-94)
- Doc 08: Incident reporting procedure (Art. 73 applies to high-risk AI systems; Art. 55(1)(c) imposes a distinct serious-incident tracking/reporting duty on systemic-risk GPAI providers to the AI Office)

> **Note on article mapping (corrected in v3.2.x):** In Regulation (EU) 2024/1689, **Article 56 is "Codes of practice":** it is *not* the source of the AI Office's investigatory and corrective powers. Those powers sit in **Chapter IX, Section 5, Articles 88-94**: Art. 88 (enforcement of GPAI obligations), Art. 91 (power to request documentation and information), Art. 92 (power to conduct evaluations), and Art. 93 (power to request measures). This document cites those articles accordingly.

---

## Part 1: Systemic Risk Classification

### 1.1 What is a GPAI Model with Systemic Risk?

A GPAI model is classified as having **systemic risk** when it meets one or more of the following criteria under Article 51:

| Criterion | Threshold | Reference |
|---|---|---|
| **High-impact capabilities / training compute** | A GPAI model is presumed to have high-impact capabilities where the cumulative compute used for its training, measured in floating point operations (FLOP), is greater than **10²⁵** | Art. 51(1)(a) + Art. 51(2) |
| **Commission designation** | The Commission, ex officio or following a qualified alert from the scientific panel, designates the model as having high-impact capabilities / systemic risk based on the criteria in Annex XIII | Art. 51(1)(b) |

**Note on the compute threshold:** The 10²⁵ FLOP figure is a **rebuttable presumption** (Art. 51(2)). A provider whose model meets the threshold may submit arguments that, exceptionally, the model does not present systemic risks; the Commission decides (Art. 52(2)-(3)).

**Note on designation:** The Commission may designate models based on the criteria in **Annex XIII**, including: number of parameters, dataset size/quality, compute, input/output modalities, benchmarks and capabilities, degree of autonomy and scalability, and reach (e.g. number of registered EU business/end users).

### 1.2 Systemic Risk Determination

| Field | Detail |
|---|---|
| GPAI model name | |
| Model version | |
| Training compute (estimated FLOP) | |
| Compute threshold met (> 10²⁵ FLOP)? | ☐ YES ☐ NO ☐ UNCERTAIN |
| Commission designation received? | ☐ YES ☐ NO, If YES, date: |
| Systemic risk classification confirmed? | ☐ YES ☐ NO ☐ PENDING |

**If Systemic Risk = NO:** Use Doc 11 only. Do not proceed with this document.
**If Systemic Risk = YES or PENDING:** Complete all sections of this document. Note: the Art. 52(1) notification duty to the Commission arises **without delay and in any event within 2 weeks** of the threshold being met or becoming known.

### 1.3 Rebuttable Presumption Process (if applicable)

If the compute threshold is met but you believe the model does not pose systemic risk:

| Step | Action | Status |
|---|---|---|
| 1 | Notify the Commission within 2 weeks of meeting/knowing the threshold (Art. 52(1)) | ☐ |
| 2 | Submit, with that notification, arguments demonstrating the model exceptionally does not present systemic risks (Art. 52(2)) | ☐ |
| 3 | Await Commission determination | ☐ |
| 4 | If confirmed systemic risk: implement all Art. 55 obligations | ☐ |
| 5 | If no systemic risk: retain documentation of the process | ☐ |

*Justification narrative:* _______________________________________________

---

## Part 2: Article 55 Obligations: Mandatory Systemic Risk Measures

Article 55(1) imposes four mandatory obligations on providers of GPAI models with systemic risk, **in addition** to the Article 53-54 baseline obligations:

- **Art. 55(1)(a):** perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting **adversarial testing** to identify and mitigate systemic risks;
- **Art. 55(1)(b):** **assess and mitigate** possible systemic risks at Union level, including their sources;
- **Art. 55(1)(c):** keep track of, document and **report serious incidents** and possible corrective measures, without undue delay, to the AI Office and, as appropriate, national competent authorities;
- **Art. 55(1)(d):** ensure an adequate level of **cybersecurity** protection for the model and its physical infrastructure.

### 2.1 Obligation 1: Model Evaluation and Adversarial Testing (Red-Teaming)
**Article 55(1)(a) | Annex XIII**

#### 2.1.1 What is Required

Providers must conduct **model evaluations in accordance with standardised protocols and tools** reflecting the state of the art, including adversarial testing ("red-teaming") to identify and mitigate systemic risks, including safety and security risks. Until harmonised standards and Codes of Practice (Art. 56) are available, providers may demonstrate compliance by other adequate means and should follow the state of the art.

#### 2.1.2 Adversarial Testing Plan

| Field | Detail |
|---|---|
| Red-team exercise name/ID | |
| Model version tested | |
| Testing organisation (internal/external/both) | |
| External red-team engaged? | ☐ YES ☐ NO, Name: |
| Date of testing | |
| Next scheduled testing | |

#### 2.1.3 Adversarial Testing Coverage

The following risk areas should be covered in adversarial testing for systemic risk GPAI models:

| Risk Domain | Test Scenarios Developed | Tests Executed | Critical Findings | Mitigated? |
|---|---|---|---|---|
| **CBRN uplift:** Does the model provide meaningful technical uplift to development of chemical, biological, radiological, or nuclear weapons? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Cyberoffensive capabilities:** Can the model generate functional exploit code, malware, or novel cyberattack techniques? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Critical infrastructure attack:** Can the model provide actionable guidance on attacking power grids, water systems, financial infrastructure, transport networks? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Disinformation at scale:** Can the model generate highly convincing, scalable disinformation including synthetic media (deepfakes, fake news, fabricated evidence)? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Autonomous harmful action:** Can the model act autonomously in ways that could cause serious, widespread harm without human oversight? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Safety bypass:** Can the model be jailbroken, manipulated, or fine-tuned to circumvent safety measures? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Bias and discrimination at scale:** Does the model systematically generate biased, discriminatory, or harmful content about protected groups? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |
| **Privacy violation at scale:** Does the model memorise, reproduce, or enable inference of personal data at scale? | ☐ YES ☐ NO | ☐ YES ☐ NO | | ☐ YES ☐ N/A |

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

### 2.2 Obligation 2: Systemic Risk Assessment and Mitigation
**Article 55(1)(b)**

Providers must assess and mitigate possible systemic risks at Union level, including their sources, that may stem from the development, the placing on the market, or the use of the model.

| Step | Action | Status |
|---|---|---|
| Identify sources of systemic risk (capabilities, misuse vectors, scale of reach) | | ☐ |
| Estimate likelihood and severity of Union-level harm | | ☐ |
| Define and implement mitigation measures (see Part 3.2 post-training measures) | | ☐ |
| Document residual systemic risk and acceptance decision | | ☐ |
| Re-assess on each material change and at least annually | | ☐ |

---

### 2.3 Obligation 3: Serious Incident Reporting to the AI Office
**Article 55(1)(c)**

Providers of systemic-risk GPAI models must keep track of, document and **report, without undue delay, to the AI Office** (and, as appropriate, national competent authorities) relevant information about serious incidents and possible corrective measures.

> **Deadline note:** Art. 55(1)(c) requires reporting **"without undue delay."** It does **not** set a fixed 72-hour clock. The 72-hour figure belongs to **GDPR Art. 33** (personal-data breaches). The Art. 73 high-risk-AI tiers (2/10/15 days) apply to high-risk *AI systems*, not to this GPAI-model duty. Where an incident is also a personal-data breach, the GDPR 72-hour clock to the DPA runs in parallel.

#### 2.3.1 Standard vs. Enhanced Obligations

| Obligation | All GPAI Providers (Arts. 53-54) | Systemic Risk GPAI Providers (Art. 55) |
|---|---|---|
| Track and report serious incidents to the AI Office, without undue delay | Not a standalone Art. 53 duty | ☐ Required, Art. 55(1)(c) |
| Document possible corrective measures |, | ☐ Required, Art. 55(1)(c) |
| Cooperate with the Commission / AI Office (documentation, evaluations, measures) | ☐ Required (Arts. 91-93) | ☐ Required (enhanced) |
| Provide model documentation/access to the AI Office on request | Arts. 91-92 | Arts. 91-92 (enhanced) |

#### 2.3.2 Systemic Risk Incident Categories

For systemic risk GPAI models, the following constitute reportable incidents (report **without undue delay** to the AI Office; where personal data is involved, run the GDPR Art. 33 72-hour clock to the DPA in parallel):

| Category | Description | Immediate Action | Reporting |
|---|---|---|---|
| CBRN misuse | Model used to provide material uplift to CBRN weapons development | Restrict model access; preserve logs | Without undue delay → AI Office |
| Cyber attack enablement | Model used to generate functional malware or exploits used in an actual attack | Restrict output capabilities; preserve logs | Without undue delay → AI Office |
| Disinformation campaign | Model used to generate content that materially influenced a democratic process or caused widespread public harm | Document outputs; preserve logs; notify relevant authorities | Without undue delay → AI Office |
| Critical infrastructure | Model-derived guidance used in an actual attack on critical infrastructure | Emergency protocol; contact national CSIRT; notify AI Office | Without undue delay → AI Office; consider Art. 73 if a high-risk AI system is also involved |
| Safety bypass at scale | Jailbreak technique exploited in production affecting a large number of users | Deploy patch/safeguard; communicate to downstream providers | Without undue delay → AI Office |
| Personal data breach at scale | Model memorisation or generation exposes personal data of identified individuals | GDPR Art. 33 notification (72 hours to DPA); notify AI Office | Parallel GDPR + AI Office reporting |

#### 2.3.3 Systemic Risk Incident Register

| Incident ID | Date Detected | Category | Description | Persons Affected | AI Office Notified (date) | Action Taken | Status |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |

---

### 2.4 Obligation 4: Cybersecurity Protection
**Article 55(1)(d)**

Providers of systemic risk GPAI models must ensure an **adequate level of cybersecurity protection** for the model and its physical infrastructure across the model lifecycle (including protection against model weight exfiltration, unauthorised access, and tampering).

#### 2.4.1 Cybersecurity Risk Assessment

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

#### 2.4.2 Cybersecurity Minimum Controls

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

#### 2.4.3 Most Recent Security Assessment

| Assessment Type | Conducted By | Date | Key Findings | Remediation Status |
|---|---|---|---|---|
| Penetration test | | | | |
| Red-team (security) | | | | |
| Supply chain audit | | | | |
| Threat model review | | | | |

---

## Part 3: EU Supervision and Enforcement (Articles 88-94)

The Commission has **exclusive powers** to supervise and enforce the GPAI obligations of Chapter V (Art. 88). The AI Office acts on the Commission's behalf. Providers must cooperate with the following powers.

### 3.1 AI Office / Commission Powers: Awareness Checklist

| Power | Article | Provider Obligation |
|---|---|---|
| Request the documentation/information drawn up under Arts. 53/55, or further information needed to assess compliance | Art. 91 | Provide within the time set in the request |
| Conduct evaluations of the model (compliance assessment; investigate systemic risks, including via independent experts) | Art. 92 | Cooperate; provide access as required |
| Request measures (compliance measures; mitigation of systemic risk; restriction, withdrawal or recall of the model) | Art. 93 | Implement; report on implementation |
| Provider may offer commitments (incl. codes of practice) | Art. 93 / Art. 56 | Optional; document if offered |
| Procedural rights, confidentiality, penalties for GPAI providers | Arts. 94, 78, 101 | Observe; the Commission may impose fines up to **3% of global annual turnover or €15m** for GPAI infringements (Art. 101) |

> **Penalty note:** GPAI-model providers are subject to the **Article 101** fine regime (up to 3% of worldwide annual turnover or €15 million), enforced by the Commission, distinct from the Article 99 fines applied by national authorities to other operators.

### 3.2 Post-Training / Mitigation Measures (Article 55(1)(b))

Where adversarial testing or evaluation identifies systemic risk, providers must take mitigation measures.

| Measure Type | Description | When Used |
|---|---|---|
| **Safety fine-tuning** | Additional fine-tuning to improve safety, reduce harmful outputs, or address identified capability misuse | When red-team identifies significant harmful capability gap |
| **Capability restrictions** | Modifying system prompts, RLHF reward signals, or output filters to restrict specific dangerous capabilities | When capability cannot be safely deployed without restriction |
| **Output filtering** | Post-generation filtering to prevent specific harmful content categories | When real-time generation cannot be fully controlled |
| **Access controls** | Restricting model access to vetted downstream providers or use cases | When general availability poses unacceptable systemic risk |
| **Marking/watermarking** | Ensuring AI-generated outputs are marked as machine-generated and detectable per Art. 50(2) | When disinformation risk is material |
| **Retrieval restriction** | Preventing retrieval-augmented generation from specific dangerous data sources | When RAG pipeline creates dangerous capability uplift |

#### Mitigation Measures Register

| Measure ID | Measure Type | Risk Addressed | Implementation Date | Verification Method | Effective? |
|---|---|---|---|---|---|
| | | | | | ☐ YES ☐ NO ☐ TBD |
| | | | | | ☐ YES ☐ NO ☐ TBD |
| | | | | | ☐ YES ☐ NO ☐ TBD |

---

## Part 4: Systemic Risk Governance

### 4.1 Governance Structure

| Role | Name | Responsibilities |
|---|---|---|
| Model Safety Officer | | Overall accountability for systemic risk compliance; AI Office liaison |
| Head of Red-Team | | Plans and executes adversarial testing programme |
| CISO | | Cybersecurity measures (Art. 55(1)(d)); security incident response |
| Head of Compliance | | Regulatory compliance; documentation; incident reporting (Art. 55(1)(c)) |
| Legal Counsel | | Commission/AI Office cooperation (Arts. 91-93); remediation advice; privilege |
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

The Article 55 obligations must be reviewed at least annually, and whenever a material change occurs to the model.

| Review Trigger | Date | Changes Identified | Updates Made | Approved By |
|---|---|---|---|---|
| Annual review | | | | |
| New model version | | | | |
| New red-team findings | | | | |
| Commission / AI Office direction | | | | |
| Significant incident | | | | |

---

## Part 5: Voluntary Commitments and Codes of Practice (Article 56)

The EU AI Act encourages GPAI model providers (including systemic risk providers) to rely on **Codes of Practice** (Article 56) to demonstrate compliance until harmonised standards are available. The AI Office facilitates their drawing up.

| Commitment | Status |
|---|---|
| Participation in the AI Office GPAI Code of Practice process | ☐ Participating ☐ Not participating ☐ Monitoring |
| Signed GPAI Code of Practice | ☐ YES ☐ NO ☐ Pending |
| Voluntary safety commitments with the AI Office | ☐ YES ☐ NO, describe: |
| Membership in AI standards body (e.g., ISO/IEC JTC 1/SC 42, CEN/CENELEC JTC 21) | ☐ YES ☐ NO |

---

## Part 6: Systemic Risk Compliance Summary

### 6.1 Article 55 Compliance Checklist

| Obligation | Reference | Status | Evidence |
|---|---|---|---|
| Model evaluation / adversarial testing (red-teaming) conducted | Art. 55(1)(a) | ☐ Complete ☐ In Progress ☐ Not Started | |
| Systemic risks assessed and mitigated at Union level | Art. 55(1)(b) | ☐ Complete ☐ In Progress ☐ Not Started | |
| Serious incidents tracked and reported to AI Office without undue delay | Art. 55(1)(c) | ☐ Process in place ☐ Pending | |
| Adequate cybersecurity protection implemented | Art. 55(1)(d) | ☐ Complete ☐ In Progress ☐ Not Started | |
| Cooperation process for Arts. 91-93 requests documented | Arts. 91-93 | ☐ Complete ☐ In Progress ☐ Not Started | |

### 6.2 Systemic Risk Compliance Sign-Off

| Field | Detail |
|---|---|
| Model name | |
| Model version | |
| Systemic risk designation confirmed | ☐ YES (compute threshold) ☐ YES (Commission designation) |
| All Art. 55 obligations complete | ☐ YES ☐ NO, open items: |
| Date of compliance sign-off | |
| Next review date | |

| Role | Name | Date | Signature |
|---|---|---|---|
| Model Safety Officer | | | |
| Head of Compliance | | | |
| Legal Counsel | | | |
| CEO / Chief AI Officer | | | |

---

## Appendix A: Key Definitions

| Term | Definition | Reference |
|---|---|---|
| GPAI Model | AI model trained with a large amount of data using self-supervision at scale, displaying significant generality and capable of competently performing a wide range of distinct tasks | Art. 3(63) |
| GPAI Model with Systemic Risk | GPAI model with high-impact capabilities or that is designated as having systemic risk | Art. 3(65) + Art. 51 |
| Systemic Risk | Risk specific to the high-impact capabilities of GPAI models, having significant impact on the Union market due to reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or society, that can be propagated at scale | Art. 3(65) |
| Adversarial Testing | Structured evaluation to identify risks, vulnerabilities, and safety concerns by simulating adversarial conditions, including "red-teaming" | Art. 55(1)(a); Annex XIII |
| Downstream Provider | Provider of an AI system, including a GPAI system, which integrates an AI model, regardless of whether provided by the same provider | Art. 3(68) |

---

## Appendix B: Regulatory Timeline for GPAI Systemic Risk

| Date | Event |
|---|---|
| 1 August 2024 | EU AI Act entered into force |
| 2 August 2025 | **GPAI model obligations (Arts. 53-55) become applicable; Commission GPAI enforcement powers (Arts. 88-94) apply** |
| 2 August 2027 | GPAI models already on the market before 2 Aug 2025 must be brought into compliance |
| Ongoing | AI Office facilitates Codes of Practice (Art. 56) and may conduct evaluations (Art. 92) |
| Ongoing | Commission maintains a public list of GPAI models with systemic risk (Art. 52(6)) |

---

## Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.1 | April 2026 | Corrected article mapping: Art. 55(1)(d) = cybersecurity (not cooperation); AI Office/Commission supervisory powers cited to Arts. 88-94 (not Art. 56); incident reporting set to "without undue delay" (not 72h); penalties cited to Art. 101 | Toolkit Team |
| 1.0 | April 2026 | Initial release | Toolkit Team |

---

*This document does not constitute legal advice. The systemic risk framework for GPAI models is subject to ongoing development through AI Office guidance, standardised evaluation protocols, and GPAI Codes of Practice. Always seek qualified legal counsel for binding compliance determinations. Monitor AI Office publications for updated guidance.*
