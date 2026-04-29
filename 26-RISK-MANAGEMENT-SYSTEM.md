# 26 — Article 9 Risk Management System Template
## EU AI Act Compliance Toolkit | v3.2.0 | April 2026
### Regulatory Reference: Article 9 | Applicable to: All High-Risk AI Systems (Article 6 + Annex I/III)

---

## Purpose and Scope

This document is a **standalone Risk Management System (RMS) template** for high-risk AI systems under Article 9 of Regulation (EU) 2024/1689. The RMS is a **mandatory, continuous, iterative process** that must be established, implemented, documented, and maintained throughout the entire lifecycle of the system — from design through decommissioning.

**Critical distinction from the Quality Management System (Doc 16):** The QMS (Article 17) governs organisational processes and procedures. The RMS (Article 9) governs system-level risk identification, estimation, evaluation, and mitigation. Both are required. Both must be documented separately for Notified Body review.

**Article 9 obligations apply to:** Providers of high-risk AI systems listed in Annex III or embedded in regulated products (Annex I).

**This template is distinct from:**
- Doc 02: Conformity Assessment Checklist (covers all conformity obligations, not just risk management)
- Doc 03: FRIA (focuses on fundamental rights, not technical risks)
- Doc 04: Technical Documentation (Annex IV — RMS evidence is submitted as part of technical docs)
- Doc 09: Post-Market Monitoring Plan (ongoing monitoring feeds into the RMS but is a separate obligation)

---

## RMS Overview — The Article 9 Cycle

Article 9 requires a risk management process consisting of the following steps, which must operate as a continuous loop throughout the system lifecycle:

```
[1. Establish RMS] → [2. Identify Known/Foreseeable Risks] → [3. Estimate Risk Magnitude]
        ↑                                                               ↓
[8. Update RMS]  ←  [7. Review Post-Market Data]  ←  [4. Evaluate Against Thresholds]
                                                               ↓
                                        [5. Risk Treatment / Mitigation Measures]
                                                               ↓
                                        [6. Residual Risk Assessment & Acceptance]
```

All steps must be documented. The RMS record forms part of the technical documentation under Annex IV.

---

## Part 1 — RMS Establishment and Governance

### 1.1 System Identification

| Field | Detail |
|---|---|
| AI system name | |
| Version / build | |
| Annex I/III category | (e.g., Annex III, Area 4 — Employment: CV screening) |
| Provider organisation | |
| RMS Owner (name and role) | |
| RMS Establishment Date | |
| Current RMS Version | |
| Date of Last Review | |
| Date of Next Scheduled Review | |

### 1.2 RMS Scope Statement

Describe the boundaries of the RMS: which components, use contexts, user groups, and life-cycle phases are within scope.

*RMS Scope:*
_______________________________________________
_______________________________________________

### 1.3 RMS Team and Responsibilities

| Role | Name | Responsibility |
|---|---|---|
| RMS Owner | | Overall accountability; approves risk acceptance decisions |
| Technical Risk Analyst | | Identifies and estimates technical risks; maintains risk register |
| Data Governance Lead | | Identifies data-related risks; oversees dataset bias analysis |
| Human Oversight Lead | | Identifies human oversight failure modes; designs interventions |
| Legal/Compliance Lead | | Identifies regulatory and rights-related risks |
| CISO / Security Lead | | Identifies cybersecurity and adversarial risks |
| DPO (if applicable) | | Reviews GDPR-intersecting risks; coordinates with FRIA (Doc 03) |

### 1.4 RMS Documentation

| Document | Location | Owner | Last Updated |
|---|---|---|---|
| RMS Master Record (this document) | | | |
| Risk Register | | | |
| Risk Treatment Records | | | |
| Residual Risk Acceptance Sign-offs | | | |
| Post-Market Monitoring Feed Log | | | |

---

## Part 2 — Step 1: Known and Foreseeable Risk Identification

**Article 9(2)(a)** requires identification of risks the AI system can pose to health, safety, and fundamental rights considering its intended purpose **and** reasonably foreseeable misuse.

### 2.1 Intended Use Risk Identification

For each risk category below, document identified risks specific to this system:

#### Category A — Technical Performance Risks

| Risk ID | Risk Description | Trigger Scenario | Affected Persons |
|---|---|---|---|
| A-001 | Inaccurate output (false positive / false negative) | | |
| A-002 | Performance degradation on underrepresented subgroups | | |
| A-003 | Output instability across similar inputs (lack of reproducibility) | | |
| A-004 | Failure under distribution shift (real-world data differs from training data) | | |
| A-005 | [Add system-specific technical risk] | | |

#### Category B — Data and Bias Risks

| Risk ID | Risk Description | Trigger Scenario | Affected Persons |
|---|---|---|---|
| B-001 | Training data reflecting historical discrimination | | |
| B-002 | Insufficient representation of protected groups in training data | | |
| B-003 | Data quality degradation in production (data drift) | | |
| B-004 | Personal data leakage through model outputs (memorisation) | | |
| B-005 | [Add system-specific data risk] | | |

#### Category C — Human Oversight Risks

| Risk ID | Risk Description | Trigger Scenario | Affected Persons |
|---|---|---|---|
| C-001 | Automation bias — operators over-relying on AI output | | |
| C-002 | Insufficient operator training to identify errors | | |
| C-003 | Override mechanism not used due to time pressure | | |
| C-004 | High workload reducing effective oversight | | |
| C-005 | [Add system-specific oversight risk] | | |

#### Category D — Security and Adversarial Risks

| Risk ID | Risk Description | Trigger Scenario | Affected Persons |
|---|---|---|---|
| D-001 | Adversarial input attacks causing erroneous output | | |
| D-002 | Model inversion or extraction attacks exposing training data | | |
| D-003 | Data poisoning during training or fine-tuning | | |
| D-004 | Prompt injection (for LLM-based components) | | |
| D-005 | [Add system-specific security risk] | | |

#### Category E — Fundamental Rights Risks

| Risk ID | Risk Description | Trigger Scenario | Affected Persons |
|---|---|---|---|
| E-001 | Discriminatory outcomes based on protected characteristics | | |
| E-002 | Privacy violation through inference of sensitive attributes | | |
| E-003 | Violation of right to explanation / contestation | | |
| E-004 | Unjustified restriction of access to services or opportunities | | |
| E-005 | [Add system-specific rights risk] | | |

#### Category F — Operational and Deployment Risks

| Risk ID | Risk Description | Trigger Scenario | Affected Persons |
|---|---|---|---|
| F-001 | Misuse by deployer beyond intended purpose | | |
| F-002 | Integration failure with deployer's existing systems | | |
| F-003 | Deployment in context for which system was not validated | | |
| F-004 | Failure to provide adequate instructions for use | | |
| F-005 | [Add system-specific operational risk] | | |

### 2.2 Reasonably Foreseeable Misuse Risk Identification

**Article 9(2)(a)** specifically requires identification of risks arising from **reasonably foreseeable misuse**.

| Misuse Scenario | Misuse Description | Risks Arising | Risk IDs |
|---|---|---|---|
| M-001 | Use outside intended geographic/demographic scope | | |
| M-002 | Use for a purpose not listed in intended use | | |
| M-003 | Use by an operator without required training | | |
| M-004 | Use to discriminate systematically against a group | | |
| M-005 | [Add system-specific misuse scenario] | | |

---

## Part 3 — Step 2: Risk Estimation

**Article 9(2)(b)** requires estimation of the severity and likelihood of each identified risk, informed by the nature of the AI system, the severity of potential harm, the number of persons potentially affected, and the reversibility of harm.

### 3.1 Risk Estimation Criteria

**Likelihood Scale:**

| Level | Score | Definition |
|---|---|---|
| Rare | 1 | Event could occur only in exceptional circumstances |
| Unlikely | 2 | Event could occur at some time in the system's operational life |
| Possible | 3 | Event might occur in some circumstances |
| Likely | 4 | Event will probably occur in most circumstances |
| Almost Certain | 5 | Event is expected to occur in most deployments |

**Severity Scale (per affected individual):**

| Level | Score | Definition |
|---|---|---|
| Negligible | 1 | Minor inconvenience; easily reversible; no lasting impact |
| Minor | 2 | Limited harm; reversible with moderate effort; limited rights impact |
| Moderate | 3 | Significant harm; partially reversible; material rights impact |
| Major | 4 | Serious harm; difficult to reverse; significant rights impact (e.g., denied employment, restricted access to credit) |
| Critical | 5 | Catastrophic harm; irreversible; severe rights violation (e.g., wrongful detention, serious bodily harm) |

**Breadth Scale (number of affected persons):**

| Level | Score | Definition |
|---|---|---|
| Individual | 1 | Affects 1-10 persons in isolated incidents |
| Small Group | 2 | Affects 10-100 persons or a specific subgroup |
| Limited | 3 | Affects 100-10,000 persons |
| Large | 4 | Affects 10,000-1,000,000 persons |
| Widespread | 5 | Affects over 1,000,000 persons or a protected group systemically |

**Risk Score = Likelihood × Severity**
**Risk Priority Score = Likelihood × Severity × Breadth**

### 3.2 Risk Register

Complete for all risks identified in Part 2:

| Risk ID | Risk Description | Likelihood (1-5) | Severity (1-5) | Breadth (1-5) | Risk Score (L×S) | Priority Score (L×S×B) | Inherent Risk Level | Treatment Required |
|---|---|---|---|---|---|---|---|---|
| A-001 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| A-002 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| A-003 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| A-004 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| B-001 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| B-002 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| B-003 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| B-004 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| C-001 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| C-002 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| C-003 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| D-001 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| D-002 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| D-003 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| E-001 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| E-002 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| E-003 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| F-001 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| F-002 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |
| M-001 | | | | | | | ☐ Low ☐ Med ☐ High ☐ Critical | ☐ YES ☐ NO |

**Risk Level thresholds:**
- **Low:** Score 1-4
- **Medium:** Score 5-9
- **High:** Score 10-16
- **Critical:** Score 17-25

---

## Part 4 — Step 3: Risk Evaluation Against Acceptable Thresholds

**Article 9(4)** requires that the risk management measures result in residual risks being judged acceptable, considering the generally acknowledged state of the art and the specific benefits of the AI system.

### 4.1 Acceptable Risk Threshold Policy

| Risk Level | Default Treatment Policy | Approval Required |
|---|---|---|
| Low (1-4) | Accept with documented rationale | RMS Owner |
| Medium (5-9) | Mitigate to Low OR accept with senior approval | Head of Compliance |
| High (10-16) | Mandatory mitigation; acceptance requires executive approval and legal review | C-Suite + Legal Counsel |
| Critical (17-25) | Do not deploy until mitigated; if not mitigable, consult competent authority | Board + Competent Authority |

### 4.2 Risk Evaluation Decisions

For each risk assessed as Medium or above, document the evaluation decision:

| Risk ID | Inherent Risk Level | Evaluation Decision | Rationale | Approver | Date |
|---|---|---|---|---|---|
| | | ☐ Accept ☐ Mitigate ☐ Transfer ☐ Avoid | | | |
| | | ☐ Accept ☐ Mitigate ☐ Transfer ☐ Avoid | | | |
| | | ☐ Accept ☐ Mitigate ☐ Transfer ☐ Avoid | | | |
| | | ☐ Accept ☐ Mitigate ☐ Transfer ☐ Avoid | | | |
| | | ☐ Accept ☐ Mitigate ☐ Transfer ☐ Avoid | | | |

---

## Part 5 — Step 4: Risk Treatment Measures

**Article 9(2)(c)** requires adoption of appropriate risk management measures. **Article 9(3)** specifies that where feasible, technical measures should be addressed during design and development before information and training measures.

**Treatment measure hierarchy (Article 9(3)):**
1. Technical measures first (design, architecture, training, testing)
2. Operational measures second (deployment constraints, instructions for use)
3. Training and information measures third (operator training, transparency)

### 5.1 Risk Treatment Plans

For each risk requiring treatment, complete a treatment plan:

#### Treatment Plan Template

**Risk ID:** ___________
**Risk Description:** _______________________________________________
**Current Risk Score:** ___________  **Target Residual Score:** ___________

| # | Treatment Measure | Type | Implementation Owner | Target Completion | Verification Method | Status |
|---|---|---|---|---|---|---|
| 1 | | ☐ Technical ☐ Operational ☐ Training | | | | ☐ Open ☐ In Progress ☐ Complete |
| 2 | | ☐ Technical ☐ Operational ☐ Training | | | | ☐ Open ☐ In Progress ☐ Complete |
| 3 | | ☐ Technical ☐ Operational ☐ Training | | | | ☐ Open ☐ In Progress ☐ Complete |

**Residual risk score after treatment:** ___________
**Residual risk level:** ☐ Low ☐ Medium ☐ High ☐ Critical

---

### 5.2 Standard Treatment Measures by Risk Category

Use these as starting points when developing treatment plans:

#### Technical Performance Risks (Category A)

| Risk | Standard Treatment Measures |
|---|---|
| A-001 Inaccurate output | Accuracy/precision/recall testing against benchmarks; confidence thresholds; fallback rules; human review for low-confidence outputs |
| A-002 Subgroup performance gap | Disaggregated performance metrics by protected group; resampling or reweighting training data; fairness-aware model selection |
| A-003 Output instability | Reproducibility testing; deterministic inference settings; ensemble methods; version locking |
| A-004 Distribution shift | Monitoring input feature distributions; drift detection alerts; periodic model revalidation; canary deployments |

#### Data and Bias Risks (Category B)

| Risk | Standard Treatment Measures |
|---|---|
| B-001 Historical bias in training data | Dataset audit; bias detection tools (e.g., Fairlearn, IBM AI Fairness 360); data augmentation; counterfactual fairness testing |
| B-002 Underrepresentation | Stratified sampling; synthetic data generation for underrepresented groups; acceptance testing per demographic |
| B-003 Data drift | Statistical process control on input distributions; feature store monitoring; scheduled dataset refresh |
| B-004 Data leakage via outputs | Differential privacy; output filtering; membership inference attack testing; query rate limiting |

#### Human Oversight Risks (Category C)

| Risk | Standard Treatment Measures |
|---|---|
| C-001 Automation bias | Human oversight training (Doc 17); mandatory pause-and-review workflows; random sampling audits of operator decisions |
| C-002 Insufficient operator training | Role-based competency framework (Doc 17); certification requirements; simulation-based training |
| C-003 Override mechanism not used | UX design: clear override buttons; logging of non-override decisions; performance metrics include override rate |
| C-004 Workload reducing oversight | Workload monitoring; maximum caseload rules in instructions for use; staffing requirements in deployer guidance |

#### Security and Adversarial Risks (Category D)

| Risk | Standard Treatment Measures |
|---|---|
| D-001 Adversarial input attacks | Adversarial robustness testing; input validation and sanitisation; adversarial training; certified defences |
| D-002 Model inversion/extraction | Rate limiting; output perturbation; API authentication; monitoring for extraction patterns |
| D-003 Data poisoning | Training data provenance tracking; anomaly detection in training data; data signing; supply chain security |
| D-004 Prompt injection | Input sanitisation; instruction hierarchy enforcement; output monitoring; sandboxed execution |

#### Fundamental Rights Risks (Category E)

| Risk | Standard Treatment Measures |
|---|---|
| E-001 Discriminatory outcomes | Equitable impact testing; bias audits; appeals/contestation mechanism; regular fairness audits |
| E-002 Privacy violation via inference | Minimisation of sensitive attribute features; fairness constraints preventing protected attribute inference; privacy impact assessment (Doc 18) |
| E-003 Lack of right to explanation | Explainability layer (SHAP, LIME, counterfactual explanations); meaningful human review at contestation; documentation of explanation method |
| E-004 Unjustified access restriction | Due process mechanism; human review pathway; logging of all consequential decisions |

---

## Part 6 — Step 5: Residual Risk Assessment and Acceptance

**Article 9(4)** requires that residual risks remaining after treatment be judged acceptable.

### 6.1 Residual Risk Register

| Risk ID | Treatment Measures Applied | Post-Treatment Likelihood | Post-Treatment Severity | Residual Risk Score | Residual Risk Level | Acceptable? | Approval |
|---|---|---|---|---|---|---|---|
| | | | | | ☐ Low ☐ Med ☐ High | ☐ YES ☐ NO | |
| | | | | | ☐ Low ☐ Med ☐ High | ☐ YES ☐ NO | |
| | | | | | ☐ Low ☐ Med ☐ High | ☐ YES ☐ NO | |
| | | | | | ☐ Low ☐ Med ☐ High | ☐ YES ☐ NO | |
| | | | | | ☐ Low ☐ Med ☐ High | ☐ YES ☐ NO | |

### 6.2 Aggregate Residual Risk Statement

Provide an overall narrative assessment of residual risk in the context of Article 9(4):

*Considering the nature, context, and intended purpose of the [system name], and the benefits provided by this system, the aggregate residual risk — following application of all treatment measures documented above — is judged to be [acceptable / not yet acceptable] because:*

_______________________________________________
_______________________________________________
_______________________________________________

**Aggregate residual risk acceptance decision:** ☐ Acceptable ☐ Not yet acceptable (further treatment required)

| Approver Role | Name | Date | Signature |
|---|---|---|---|
| RMS Owner | | | |
| Head of Compliance | | | |
| Legal Counsel | | | |
| CTO / Technical Lead | | | |

---

## Part 7 — Step 6: Testing and Validation

**Article 9(5)–(9)** imposes specific requirements on testing, including testing prior to placement on the market, testing on real-world conditions where possible (Article 9(6)), and testing for bias (Article 9(7)).

### 7.1 Pre-Market Testing Requirements

| Requirement | Reference | Met? | Evidence Reference |
|---|---|---|---|
| Testing performed prior to placing on market | Art. 9(5) | ☐ YES ☐ NO | |
| Testing covers all identified risks in Part 2 | Art. 9(5)(a) | ☐ YES ☐ NO | |
| Testing performed against defined metrics | Art. 9(5)(b) | ☐ YES ☐ NO | |
| Testing uses data representative of intended purpose | Art. 9(5)(c) | ☐ YES ☐ NO | |
| Testing conducted in real-world conditions OR justified otherwise | Art. 9(6) | ☐ YES ☐ NO | |
| Testing for bias across relevant subgroups | Art. 9(7) | ☐ YES ☐ NO | |
| Testing for bias re: protected characteristics | Art. 9(7) | ☐ YES ☐ NO | |

### 7.2 Bias Testing Results Summary

| Subgroup / Protected Characteristic | Performance Metric | System-Wide Score | Subgroup Score | Gap | Acceptable? |
|---|---|---|---|---|---|
| Gender (male/female/other) | | | | | ☐ YES ☐ NO |
| Age group (18-30 / 31-50 / 51+) | | | | | ☐ YES ☐ NO |
| Ethnicity / racial group | | | | | ☐ YES ☐ NO |
| Disability status | | | | | ☐ YES ☐ NO |
| [Other relevant characteristic] | | | | | ☐ YES ☐ NO |

### 7.3 Testing Against Article 9(8) — Real-World Performance Thresholds

Article 9(8) requires that the level of accuracy, robustness, and cybersecurity against which the high-risk AI system has been tested and the limits of accuracy are described in the accompanying documentation.

| Performance Metric | Definition | Target Threshold | Actual Performance | Test Date | Pass/Fail |
|---|---|---|---|---|---|
| Accuracy | | | | | ☐ PASS ☐ FAIL |
| Precision | | | | | ☐ PASS ☐ FAIL |
| Recall | | | | | ☐ PASS ☐ FAIL |
| F1 Score | | | | | ☐ PASS ☐ FAIL |
| Robustness (adversarial) | | | | | ☐ PASS ☐ FAIL |
| Robustness (distribution shift) | | | | | ☐ PASS ☐ FAIL |
| Cybersecurity (penetration test) | | | | | ☐ PASS ☐ FAIL |

---

## Part 8 — Step 7: Post-Market Monitoring Integration

**Article 9(2)(d)** requires that the risk management system be updated based on data gathered from post-market monitoring. This section links the RMS to Doc 09 (Post-Market Monitoring Plan).

### 8.1 Post-Market Risk Update Triggers

The RMS must be reviewed and updated when any of the following occur:

| Trigger | Reference | Responsible | Review Initiated? |
|---|---|---|---|
| Serious incident reported under Article 73 (Doc 08) | Art. 9(2)(d) | RMS Owner | ☐ |
| Post-market monitoring data reveals new or changed risk | Art. 72 + Art. 9(2)(d) | Technical Risk Analyst | ☐ |
| Competent authority request for corrective action | Art. 79-83 | Legal/Compliance Lead | ☐ |
| Material change to the AI system (new version, new data, new use case) | Art. 9(9) | Technical Risk Analyst | ☐ |
| Annual scheduled review | RMS governance policy | RMS Owner | ☐ |
| Relevant standards update (harmonised standards, SOTAAD) | Art. 40 | Technical Risk Analyst | ☐ |

### 8.2 RMS Update Log

| Version | Update Date | Trigger | Changes Made | Approved By |
|---|---|---|---|---|
| 1.0 | | Initial RMS establishment | | |
| | | | | |
| | | | | |

---

## Part 9 — RMS Summary and Conformity Statement

### 9.1 RMS Completeness Checklist

| Article 9 Requirement | Addressed | Reference in this Document |
|---|---|---|
| Risk management system established and documented | ☐ YES ☐ NO | Part 1 |
| Known and foreseeable risks identified | ☐ YES ☐ NO | Part 2 |
| Reasonably foreseeable misuse identified | ☐ YES ☐ NO | Part 2.2 |
| Risks estimated (severity, likelihood, breadth) | ☐ YES ☐ NO | Part 3 |
| Risks evaluated against acceptable thresholds | ☐ YES ☐ NO | Part 4 |
| Risk treatment measures adopted | ☐ YES ☐ NO | Part 5 |
| Residual risks assessed and accepted | ☐ YES ☐ NO | Part 6 |
| Pre-market testing performed and documented | ☐ YES ☐ NO | Part 7 |
| Bias testing conducted across relevant groups | ☐ YES ☐ NO | Part 7.2 |
| Performance thresholds defined and tested against | ☐ YES ☐ NO | Part 7.3 |
| Post-market monitoring integration documented | ☐ YES ☐ NO | Part 8 |

### 9.2 Cross-References to Technical Documentation

This RMS, when complete, must be incorporated into or referenced from the Technical Documentation under Annex IV. Cross-reference checklist:

| Technical Documentation Section (Annex IV) | RMS Content Referenced | Complete? |
|---|---|---|
| Annex IV, §1 — General description (capabilities and limitations) | Part 2 risk register — limitations | ☐ |
| Annex IV, §2 — Detailed description (technical specs) | Part 7.3 performance thresholds | ☐ |
| Annex IV, §4 — Validation and testing | Part 7 testing records | ☐ |
| Annex IV, §6 — Risk management system description | This document (Part 1 + Part 9) | ☐ |
| Annex IV, §8 — Instructions for use | Part 5 operational treatment measures | ☐ |

### 9.3 RMS Sign-Off

| Field | Detail |
|---|---|
| RMS Version | |
| Date of approval | |
| Next scheduled review date | |
| Conformity status | ☐ Compliant with Art. 9 ☐ Partially compliant — open actions remain ☐ Non-compliant — do not deploy |

| Role | Name | Date | Signature |
|---|---|---|---|
| RMS Owner | | | |
| Head of Compliance | | | |
| CTO / Technical Lead | | | |
| Legal Counsel | | | |

---

## Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | April 2026 | Initial release — complete Article 9 RMS framework | Toolkit Team |

---

*This document does not constitute legal advice. Article 9 interpretation continues to evolve through harmonised standards, EU AI Office guidance, and national competent authority decisions. Always seek qualified legal counsel and refer to the latest EU AI Office guidance for binding compliance determinations.*
