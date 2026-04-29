# 16 — Quality Management System (QMS) Template

**EU AI Act Reference:** Article 17 | Articles 9, 11, 12, 72, 73
**Applies to:** Providers of High-Risk AI Systems
**Last Updated:** April 2026

---

## Purpose

Article 17 of the EU AI Act requires providers of high-risk AI systems to put in place a quality management system (QMS) before placing their system on the market or putting it into service. The QMS must be documented and must cover the full lifecycle of the AI system.

This template provides a structured, Article 17-compliant QMS that can be adopted standalone or integrated into an existing ISO 9001 or ISO/IEC 42001 management system.

**Cross-reference:** The QMS is one of the eight sections verified in the Conformity Assessment Checklist (02-CONFORMITY-ASSESSMENT-CHECKLIST.md, Section H). Complete this document before finalising the conformity assessment.

---

## Document Control

| Field | Entry |
|---|---|
| Document Title | Quality Management System |
| QMS Version | |
| QMS Owner | |
| Approved By | |
| Approval Date | |
| Next Review Date | |

---

## Part 1 — QMS Scope and Policy

### 1.1 Scope Statement

This QMS applies to all high-risk AI systems developed, placed on the market, or put into service under Regulation (EU) 2024/1689, Article 17.

### 1.2 AI Quality Policy Statement

The organisation is committed to developing and deploying AI systems that are safe, accurate, transparent, and respectful of fundamental rights:

1. **Compliance** — Meet all applicable requirements of the EU AI Act and harmonised standards.
2. **Risk-Based Design** — Identify, assess, and mitigate risks throughout the AI system lifecycle.
3. **Data Integrity** — Ensure training, validation, and testing data meets governance standards.
4. **Human Oversight** — Design and operate systems so human oversight is meaningful, not nominal.
5. **Continuous Improvement** — Monitor performance post-deployment and act on findings.
6. **Accountability** — Assign clear roles and responsibilities for QMS compliance.

---

## Part 2 — Organisation and Responsibilities (Article 17(1)(e))

| Role | Responsibility | Assigned To |
|---|---|---|
| Senior Responsible Officer | Overall accountability for AI Act compliance and QMS | |
| AI Quality Manager | Day-to-day QMS management | |
| Technical Lead | System design, development, and documentation | |
| Data Governance Lead | Training data quality and bias assessment | |
| Compliance / Legal Lead | Regulatory requirements and conformity assessment | |
| AI Oversight Officer | Human oversight controls and post-market monitoring | |
| Data Protection Officer | GDPR compliance and AI Act intersection | |

---

## Part 3 — Compliance Strategy (Article 17(1)(a))

| Requirement | Approach | Owner | Status |
|---|---|---|---|
| Risk management system (Art. 9) | Internal risk management + risk register | Technical Lead | |
| Data governance (Art. 10) | Data governance policy + bias audit | Data Governance Lead | |
| Technical documentation (Art. 11) | Annex IV template — Document 04 | Technical Lead | |
| Logging and record-keeping (Art. 12) | Automated logging in system architecture | Technical Lead | |
| Transparency and instructions (Art. 13) | Instructions for use prepared and reviewed | Compliance | |
| Human oversight (Art. 14) | Oversight framework — Document 07 | AI Oversight Officer | |
| Accuracy, robustness, cybersecurity (Art. 15) | Performance benchmarks + cybersecurity assessment | Technical Lead | |
| Conformity assessment (Art. 43) | Internal (Annex VI) or Notified Body where required | Compliance | |
| EU registration (Art. 49, 71) | Register in EU AI database before market placement | Compliance | |
| Post-market monitoring (Art. 72) | PMM Plan — Document 09 | AI Oversight Officer | |
| Incident reporting (Art. 73) | Incident procedure — Document 08 | Compliance | |

### 3.2 Harmonised Standards Strategy

| Standard | Approach | Gap Assessment Done? |
|---|---|---|
| ISO/IEC 42001:2023 AI Management Systems | Full / Partial / Reference only | Yes / No |
| ISO/IEC 27001:2022 Information Security | Full / Partial / Reference only | Yes / No |
| ISO 31000:2018 Risk Management | Full / Partial / Reference only | Yes / No |
| ISO/IEC 23894:2023 AI Risk Management | Full / Partial / Reference only | Yes / No |
| CEN/CENELEC standards (when published) | Monitor upon publication | Tracked |

---

## Part 4 — Design and Development Procedures (Article 17(1)(b))

### 4.1 Development Lifecycle Quality Gates

| Stage | Description | Quality Gate | Owner | Sign-off Required |
|---|---|---|---|---|
| 1. Requirements | Define intended purpose, deployment context | Requirements review | Product Owner | Yes |
| 2. Data acquisition | Collect and assess training/validation/test data | Data governance review | Data Governance Lead | Yes |
| 3. Model design | Architecture selection and documentation | Design review | Technical Lead | Yes |
| 4. Training and validation | Model training against declared metrics | Performance gate | Technical Lead | Yes |
| 5. Bias and fairness testing | Demographic parity assessment | Bias audit | Data Governance Lead | Yes |
| 6. Risk assessment | Risk identification, evaluation, and mitigation | Risk register approved | Technical Lead | Yes |
| 7. Human oversight design | Oversight controls designed and tested | Oversight review | AI Oversight Officer | Yes |
| 8. Technical documentation | Annex IV documentation completed | Doc review | Compliance | Yes |
| 9. Conformity assessment | Pre-market conformity assessment | Conformity gate | Compliance | Yes — SRO sign-off |
| 10. EU registration | System registered in EU AI database | Registration confirmed | Compliance | Yes |
| 11. Market placement | Released to deployers with instructions for use | Release gate | AI Quality Manager | Yes |

### 4.2 Change Management — Substantial Modification Assessment

All post-market changes must be assessed under Article 3(23) and Article 25.

| Change Type | Substantial Modification? | Action |
|---|---|---|
| Bug fix — no functional impact | Unlikely | Update documentation |
| Performance tuning within declared spec | Unlikely | Update documentation |
| Change to training data or retraining | Assess case-by-case | May require new conformity assessment |
| Change to intended purpose | Likely | New conformity assessment if high-risk |
| Change affecting safety or accuracy thresholds | Likely | New conformity assessment |
| New Annex III use case | Yes | New conformity assessment |

**Change Assessment Log:**

| Change ID | Date | System | Description | Substantial Modification? | Action | Approved By |
|---|---|---|---|---|---|---|
| | | | | Yes / No | | |

---

## Part 5 — Data Governance Procedures (Article 17(1)(c))

### 5.1 Data Governance Requirements (Article 10)

| Requirement | Procedure | Owner |
|---|---|---|
| Datasets relevant to intended purpose | Purpose-dataset alignment review | Data Governance Lead |
| Datasets sufficiently representative | Statistical representativeness + demographic coverage | Data Governance Lead |
| Datasets free of errors (to extent practicable) | Data quality checks; anomaly detection | Technical Lead |
| Bias examination conducted | Demographic parity; proxy variable assessment | Data Governance Lead |
| Personal data handled with GDPR safeguards | See 18-GDPR-AI-ACT-INTERSECTION.md | DPO |
| Data provenance documented | Source, collection, date range, licence in Document 04 | Technical Lead |

### 5.2 Data Quality Checklist (per dataset)

| Check | Status | Evidence |
|---|---|---|
| Data source documented | Done / Pending | |
| Collection method documented | Done / Pending | |
| Licence / rights basis confirmed | Done / Pending | |
| Personal data inventory completed | Done / Pending | |
| Special category data identified | Done / Pending | |
| Representativeness assessment completed | Done / Pending | |
| Bias examination completed | Done / Pending | |
| Data quality issues addressed | Done / Pending | |

---

## Part 6 — Technical Documentation Procedures (Article 17(1)(d))

| Document | Template Reference | Created | Retention | Owner |
|---|---|---|---|---|
| Technical Documentation (Annex IV) | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md | Before market placement | 10 years (Art. 18) | Technical Lead |
| Conformity Assessment Record | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md | Before market placement | 10 years | Compliance |
| EU Declaration of Conformity | 12-EU-DECLARATION-OF-CONFORMITY.md | Before market placement | 10 years | Legal |
| FRIA (where applicable) | 03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md | Before deployment | Deployment + 5 years | Compliance |
| Post-Market Monitoring Plan | 09-POST-MARKET-MONITORING-PLAN.md | Before market placement | Throughout lifecycle | AI Oversight Officer |
| Incident Reports | 08-INCIDENT-REPORTING-PROCEDURE.md | Upon incident | 10 years | Compliance |

Document control requirements: version numbers, approval dates, named owners, annual review, superseded versions retained, accessible to MSA on request (Article 74).

---

## Part 7 — Post-Market Monitoring (Article 17(1)(f))

Full procedures in **09-POST-MARKET-MONITORING-PLAN.md**.

| PMM Element | Reference | Owner |
|---|---|---|
| Continuous performance monitoring | Document 09, Parts 3-5 | AI Oversight Officer |
| Deployer feedback collection | Document 09, Part 3.1 | AI Oversight Officer |
| Drift detection | Document 09, Part 5 | Technical Lead |
| Risk-triggered review criteria | Document 09, Part 6 | AI Governance Lead |
| Corrective action process | Document 09, Part 7 | AI Governance Lead |
| Substantial modification assessment | Document 09, Part 8 | Compliance |

---

## Part 8 — Incident Reporting (Article 17(1)(g))

Full procedures in **08-INCIDENT-REPORTING-PROCEDURE.md**.

| Obligation | Reference | Timeline | Owner |
|---|---|---|---|
| Serious incident detection and classification | Document 08, Parts 3-4 | 0-2 hours | AI Oversight Officer |
| Regulatory notification to national MSA | Document 08, Part 5 | Within 72 hours | Compliance |
| Full investigation and follow-up report | Document 08, Phase 4 | As soon as practicable | Technical + Compliance |
| Deployer notification of non-compliance | Document 08 | Without undue delay | Legal |

---

## Part 9 — Internal Audit and Management Review

### 9.1 Audit Schedule

| Scope | Frequency | Auditor | Output |
|---|---|---|---|
| Full QMS audit | Annually | Independent of area | Audit report + corrective actions |
| Pre-market conformity review | Before each placement | Compliance Lead | Conformity gate sign-off |
| PMM review | Quarterly | AI Oversight Officer | PMM report |
| Data governance and bias audit | Annually | Data Governance + DPO | Audit report |
| Incident procedure tabletop test | Annually | Compliance | Test report |

### 9.2 Annual Management Review — Agenda Items

| Review Item | Input | Actions Agreed |
|---|---|---|
| QMS audit findings | Audit reports | |
| Conformity assessment status | Assessment records | |
| Post-market monitoring findings | PMM reports | |
| Serious incidents and near-misses | Incident register | |
| Regulatory updates | Regulatory watch | |
| Resource adequacy | Resource assessment | |
| Complaints and deployer feedback | Feedback log | |
| CAPA status | CAPA log | |

**Management Review Log:**

| Date | Chair | Key Findings | Actions Agreed | Next Review |
|---|---|---|---|---|
| | SRO | | | |

---

## Part 10 — Corrective and Preventive Actions (CAPA) Log

| Action ID | Date | Source | Issue | Root Cause | Action | Owner | Deadline | Status |
|---|---|---|---|---|---|---|---|---|
| CAPA-001 | | Audit / Incident / PMM | | | | | | Open / Closed |

---

## Part 11 — QMS Version History

| Version | Date | Changes | Approved By |
|---|---|---|---|
| 1.0 | | Initial QMS | |

---

*Part of the EU AI Act Compliance Toolkit*
*This document does not constitute legal advice. Seek qualified legal counsel for binding compliance determinations.*
