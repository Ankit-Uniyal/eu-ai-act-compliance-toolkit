# 04 — Technical Documentation Template (Annex IV)

**EU AI Act Reference:** Article 11 | Annex IV
**Applies to:** Providers of High-Risk AI Systems
**Retention Period:** 10 years after last placement on market (Article 18)
**Last Updated:** April 2026

## Purpose

Article 11 requires providers of high-risk AI systems to draw up technical documentation before the system is placed on the market or put into service. The documentation must be kept up to date and made available to market surveillance authorities on request.

This template follows the structure prescribed in **Annex IV** of the EU AI Act.

## Document Control

| Field | Entry |
|---|---|
| Document Title | Technical Documentation — [System Name] |
| System ID | |
| Version | |
| Classification | CONFIDENTIAL / RESTRICTED |
| Author | |
| Approved By | |
| Approval Date | |
| Review Date | |
| Document Status | Draft / Under Review / Approved / Superseded |

---

## Annex IV, Section 1 — General Description

### 1.1 Intended Purpose

Describe the specific purpose for which the AI system is intended, including the specific context and conditions of use, the categories of natural persons and groups it is intended to be used upon, and the users it is intended for.

### 1.2 System Description

| Field | Description |
|---|---|
| System name and version | |
| Category of AI system | |
| Hardware the system is intended to run on | |
| Software (OS, frameworks, dependencies) | |
| Form (product / standalone / embedded) | |
| Intended deployment territory | |
| Provider name and address | |
| EU Authorised Representative (if applicable) | |

### 1.3 Interaction with Hardware / Software

Describe how the AI system interacts with other hardware or software that is not part of the AI system itself.

### 1.4 Versions of Relevant Software

| Software Component | Version | Licence |
|---|---|---|
| | | |

### 1.5 Description of Deployment

Describe each deployment form in which the AI system is placed on the market or put into service.

### 1.6 Instructions for Use (Summary)

Provide the instructions for use, including: a concise general description of the AI system; its characteristics, capabilities, and limitations; information regarding the accuracy and robustness of the system.

---

## Annex IV, Section 2 — Detailed Description of Elements

### 2.1 Methods and Steps for System Development

Describe the methods and steps performed for the development of the AI system, including the relevant design choices and their rationale.

### 2.2 Design Specifications

| Specification | Detail |
|---|---|
| Overall architecture | |
| Number and type of models | |
| Training methodology | |
| Optimisation techniques | |
| Key design decisions | |
| Rejected alternatives and rationale | |

### 2.3 System Architecture

Provide an architectural diagram or description showing all components and their interactions.

*[Insert system architecture diagram here]*

### 2.4 Model Information

| Field | Detail |
|---|---|
| Model type(s) | |
| Model size (parameters) | |
| Training approach | Supervised / Unsupervised / Reinforcement / Other |
| Fine-tuning approach (if applicable) | |
| Inference method | |

### 2.5 Training, Validation, and Testing Data

**Training Data**

| Field | Detail |
|---|---|
| Data source(s) | |
| Data collection method | |
| Data volume | |
| Data format | |
| Date range of data | |
| Personal data included? | Yes / No |
| Special category data? | Yes / No |
| Data governance measures | |
| Bias assessment conducted? | Yes / No — Reference: |

**Validation Data**

| Field | Detail |
|---|---|
| Validation dataset description | |
| Validation approach | |
| Validation metrics used | |

**Test Data**

| Field | Detail |
|---|---|
| Test dataset description | |
| Holdout / test split | |
| Real-world test conditions | |

### 2.6 Data Labelling and Annotation

Describe the data labelling procedures and any annotation instructions used.

### 2.7 Metrics and Performance

| Metric | Value | Benchmark / Threshold |
|---|---|---|
| Accuracy | | |
| Precision | | |
| Recall | | |
| F1 Score | | |
| AUC-ROC | | |
| Fairness metric | | |
| Other: | | |

### 2.8 Computational Resources

| Resource | Specification |
|---|---|
| Training infrastructure | Cloud / On-premise |
| Estimated training compute | |
| Inference infrastructure | |

---

## Annex IV, Section 3 — Monitoring, Functioning, and Control

### 3.1 Capabilities and Limitations

Describe the capabilities and limitations of the AI system, including the foreseeable circumstances that may lead to risks to health, safety, or fundamental rights.

| Capability | Description | Limitation | Impact | Mitigation |
|---|---|---|---|---|
| | | | | |

### 3.2 Reasonably Foreseeable Misuse

| Misuse Scenario | Likelihood | Impact | Mitigation |
|---|---|---|---|
| | | | |

### 3.3 Human Oversight Measures

Describe the measures put in place to enable humans to oversee the AI system, including the technical measures to facilitate interpretation by deployers.

### 3.4 Logging Capabilities

| Log Type | Retained For | Format | Access |
|---|---|---|---|
| Operation logs | | | |
| Decision logs | | | |
| Error logs | | | |
| Audit trail | | | |

### 3.5 Performance on Specific Groups

| Group | Performance | Notes | Disparity Identified? |
|---|---|---|---|
| | | | |

---

## Annex IV, Section 4 — Risk Management

### 4.1 Risk Management System Overview

Describe the risk management system established in accordance with Article 9.

### 4.2 Risk Register Summary

| Risk ID | Risk Description | Likelihood | Severity | Residual Risk | Mitigation |
|---|---|---|---|---|---|
| R-001 | | | | | |
| R-002 | | | | | |

### 4.3 Cybersecurity Measures

Describe the measures implemented to address cybersecurity risks, including resilience against attempts to alter use or performance.

---

## Annex IV, Section 5 — Changes Made Over Lifecycle

| Version | Date | Changes Made | Change Reason | Approved By |
|---|---|---|---|---|
| v1.0 | | Initial release | | |

---

## Annex IV, Section 6 — Standards Applied

| Standard | Version | Scope of Application |
|---|---|---|
| ISO/IEC 42001:2023 | | AI Management Systems |
| ISO/IEC 27001 | | Information Security |
| ISO 31000 | | Risk Management |
| Other: | | |

---

## Annex IV, Section 7 — EU Declaration of Conformity

Reference or attach the EU Declaration of Conformity drawn up in accordance with Article 47.

- Declaration Reference: _______________
- Date of Declaration: _______________
- Notified Body (if applicable): _______________
- Notified Body Certificate Number: _______________

---

## Annex IV, Section 8 — Post-Market Monitoring

Article 72 of the EU AI Act requires providers of high-risk AI systems to establish a post-market monitoring system proportionate to the nature of the AI technology and its risks. This section of the technical documentation must describe that system.

The full Post-Market Monitoring Plan is maintained separately as **09-POST-MARKET-MONITORING-PLAN.md**. This section provides the Annex IV summary required within the technical documentation record.

### 8.1 PMM System Overview

| Field | Detail |
|---|---|
| PMM Plan Reference | 09-POST-MARKET-MONITORING-PLAN.md |
| PMM Plan Version | |
| PMM Owner | |
| Last Updated | |

### 8.2 Performance Monitoring Approach

Describe how the system's performance is monitored after market placement:

| Monitoring Activity | Method | Frequency | Owner | Threshold / Alert Criteria |
|---|---|---|---|---|
| Model accuracy monitoring | Automated metric tracking | [e.g. Monthly] | | [e.g. accuracy drops below declared threshold] |
| Bias and fairness monitoring | Demographic parity re-assessment | [e.g. Quarterly] | | [e.g. >5% disparity vs. baseline] |
| Input data distribution monitoring | Statistical drift detection | [e.g. Monthly] | | [e.g. KS test p < 0.05] |
| Deployer feedback collection | Structured feedback forms | [e.g. Quarterly] | | Any reported issue triggering review |
| User complaint monitoring | Complaint register review | [e.g. Monthly] | | Any complaint involving safety or discrimination |

### 8.3 Data Collection from Deployers (Article 72(3))

Providers must collect and review relevant data from deployers to evaluate whether the system continues to meet requirements. Document the data collection mechanism:

| Data Type | Collection Method | Frequency | Storage Location |
|---|---|---|---|
| System performance logs | Automated log export / deployer submission | | |
| Incidents and near-misses | Deployer incident reports (Doc 08) | | |
| User feedback and complaints | Deployer feedback forms | | |
| Environmental / contextual changes | Deployer questionnaire | | |

### 8.4 Trigger Criteria for Reactive Review

A reactive review of the AI system's performance must be triggered upon any of the following:

| Trigger | Action Required |
|---|---|
| Performance falls below declared accuracy threshold | Immediate investigation; consider market withdrawal pending review |
| Serious incident reported under Article 73 | Initiate full PMM-driven investigation |
| Deployer reports unexpected behaviour | Log; assess within 10 working days |
| Regulatory authority request for investigation | Respond within required timeline; provide PMM data |
| Substantial modification contemplated (Article 25) | PMM data review as part of modification assessment |
| New information on risks to health, safety, fundamental rights | Unscheduled review; update risk management system |

### 8.5 Corrective Actions

If PMM identifies that the system no longer meets requirements, the provider must:

1. **Classify severity** — minor, moderate, or critical
2. **Notify deployers** — provide guidance without undue delay
3. **Assess notifiable incident** — determine if Article 73 serious incident reporting applies
4. **Implement corrective action** — software update, additional instructions, or market withdrawal
5. **Update documentation** — revise technical documentation, risk register, and instructions for use
6. **Assess substantial modification** — determine if a new conformity assessment is required under Article 25

### 8.6 PMM Record-Keeping

| Record Type | Retention Period | Location |
|---|---|---|
| PMM reports (annual and triggered) | 10 years from last placement | |
| Monitoring data summaries | 10 years from last placement | |
| Corrective action records | 10 years from last placement | |
| Deployer feedback records | 10 years from last placement | |

> **Note:** Article 18 requires technical documentation to be retained for 10 years after the AI system is last placed on the market. PMM records form part of this retention obligation.

---

*Part of the EU AI Act Compliance Toolkit*

*This document does not constitute legal advice. Seek qualified legal counsel for binding compliance determinations.*
