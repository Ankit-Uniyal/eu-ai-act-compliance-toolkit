# 16 — Quality Management System (QMS) Template

**EU AI Act Reference:** Article 17 | Articles 9, 11, 12, 72, 73
**Applies to:** Providers of High-Risk AI Systems
**Last Updated:** April 2026

## Purpose

Article 17 of the EU AI Act requires providers of high-risk AI systems to put in place a quality management system (QMS) before placing their system on the market or putting it into service. The QMS must be documented and must cover the full lifecycle of the AI system.

This template provides a structured, Article 17-compliant QMS that can be adopted standalone or integrated into an existing ISO 9001 or ISO/IEC 42001 management system.

**Cross-reference:** The QMS is one of the eight sections verified in the Conformity Assessment Checklist (02-CONFORMITY-ASSESSMENT-CHECKLIST.md, Section H). Complete this document before finalising the conformity assessment.

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

- **Compliance** — Meet all applicable requirements of the EU AI Act and harmonised standards.
- **Risk-Based Design** — Identify, assess, and mitigate risks throughout the AI system lifecycle.
- **Data Integrity** — Ensure training, validation, and testing data meets governance standards.
- **Human Oversight** — Design and operate systems so human oversight is meaningful, not nominal.
- **Continuous Improvement** — Monitor performance post-deployment and act on findings.
- **Accountability** — Assign clear roles and responsibilities for QMS compliance.

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

Article 17(1)(a) requires the QMS to address the strategy for regulatory compliance, including compliance with standards and, where applicable, with the technical specifications set out for the purpose of compliance.

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

## Part 3A — Article 17(1) Sub-Paragraph Compliance Map

Article 17(1) of Regulation (EU) 2024/1689 requires the QMS to address **seven specific elements** labelled (a) through (g). This section maps each sub-paragraph to the corresponding QMS component and provides the evidence trail for conformity assessment reviewers.

| Art. 17(1) Sub-paragraph | Requirement | QMS Section | Evidence Document | Status |
|---|---|---|---|---|
| (a) | Strategy for regulatory compliance, including compliance with standards and technical specifications | Part 3 — Compliance Strategy | This document, Part 3 | |
| (b) | Techniques, procedures, and systematic actions to be used for the design, design control, and design verification of the high-risk AI system | Part 4 — Design and Development Procedures | Development lifecycle gate records | |
| (c) | Examination, test, and validation procedures to be carried out before, during, and after the development of the AI system and the frequency with which they are to be carried out | Part 5 — Data Governance; validation records in Doc 04 Section 2.7 | Test and validation reports | |
| (d) | Technical specifications, including standards, to be applied; where the relevant harmonised standards are not applied in full, the means used to ensure compliance | Part 3.2 — Standards Strategy | Standards gap assessment | |
| (e) | Systems and procedures for data management, including data collection, data analysis, and data labelling | Part 5 — Data Governance Procedures | Data governance policy; bias audit report | |
| (f) | The risk management system referred to in Article 9 | Part 3 (Art. 9 reference) + Doc 02 Section A | Risk management system documentation; risk register | |
| (g) | The setting-up, implementation, and maintenance of a post-market monitoring system, in accordance with Article 72 | Part 7 — Post-Market Monitoring | 09-POST-MARKET-MONITORING-PLAN.md | |

> **Note on Article 17(1)(g):** The enacted text of Article 17(1) also encompasses incident reporting per Article 73. The QMS must demonstrate an operational serious incident reporting procedure (Part 8 of this document; Document 08).

---

## Part 3B — ISO/IEC 42001:2023 Gap Mapping

ISO/IEC 42001:2023 is the AI Management System (AIMS) standard. Where an organisation chooses to integrate its EU AI Act QMS with ISO/IEC 42001, the following mapping identifies where each EU AI Act Article 17 requirement can be satisfied within the ISO/IEC 42001 AIMS structure.

| EU AI Act Art. 17(1) | Requirement Summary | ISO/IEC 42001 Clause | ISO/IEC 42001 Requirement | Gap / Notes |
|---|---|---|---|---|
| (a) | Regulatory compliance strategy | 6.1, 6.2 | Risk assessment and AI objectives | ISO 42001 cl. 6 addresses planning for compliance; extend to EU AI Act requirements explicitly |
| (b) | Design control and verification | 8.3, 8.4 | AI system design and development; AI system operation | ISO 42001 cl. 8.3 covers AIMS design controls; align lifecycle gates to Annex IV requirements |
| (c) | Testing and validation procedures | 8.4, 9.1 | AI system deployment; monitoring and measurement | ISO 42001 cl. 9.1 covers performance evaluation; extend to pre-market validation per Art. 9 and 15 |
| (d) | Technical specifications and standards | 4.2, 6.1 | Understanding requirements; risk assessment | ISO 42001 cl. 4.2 (interested parties' requirements) can be extended to EU AI Act harmonised standards |
| (e) | Data management | Annex B (B.5, B.6) | Data for AI; impact assessment for AI | ISO 42001 Annex B provides data governance guidance; map directly to Art. 10 requirements |
| (f) | Risk management system (Art. 9) | 6.1, 8.2 | Risk assessment; AI risk treatment | ISO 42001 cl. 6.1 and 8.2 cover risk management; supplement with Art. 9's iterative lifecycle requirement |
| (g) | Post-market monitoring (Art. 72) | 9.1, 10.1 | Monitoring and measurement; continual improvement | ISO 42001 cl. 9.1 and 10.1 support ongoing monitoring; supplement with Art. 72 specific obligations |
| — | Incident reporting (Art. 73) | 10.1 | Nonconformity and corrective action | ISO 42001 cl. 10.1 covers nonconformity; extend to Art. 73 serious incident reporting timeline (72 hours to MSA) |
| — | AI literacy (Art. 4) | 7.2 | Competence | ISO 42001 cl. 7.2 covers competence; extend to Art. 4 AI literacy requirements |
| — | QMS documentation and records | 7.5 | Documented information | ISO 42001 cl. 7.5 covers documentation control; align retention to Art. 18 (10 years) |

**Adoption approach options:**

1. **Full ISO/IEC 42001 adoption:** Certify to ISO/IEC 42001 and document EU AI Act extensions in a Supplementary Compliance Register.
2. **Partial adoption:** Use ISO/IEC 42001 structure for the AIMS framework; maintain a standalone EU AI Act QMS for Art. 17-specific requirements.
3. **Reference only:** Use ISO/IEC 42001 as a best-practice guide; the EU AI Act QMS is the primary compliance document.

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

## Part 5 — Data Governance Procedures (Article 17(1)(c) and (e))

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

## Part 7 — Post-Market Monitoring (Article 17(1)(g))

Full procedures in 09-POST-MARKET-MONITORING-PLAN.md.

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

Full procedures in 08-INCIDENT-REPORTING-PROCEDURE.md.

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
