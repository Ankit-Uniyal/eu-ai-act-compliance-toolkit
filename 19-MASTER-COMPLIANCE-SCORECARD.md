# 19 — Master Compliance Scorecard

**EU AI Act Reference:** All Articles
**Applies to:** All organisations providing or deploying AI systems in the EU
**Last Updated:** April 2026

---

## Purpose

This Master Compliance Scorecard provides a single consolidated view of your organisation's EU AI Act compliance position across all 20 toolkit documents. Use it to:

- Conduct an initial gap analysis before building your compliance programme
- Track progress as you implement each requirement
- Present compliance status to senior leadership and the board
- Prepare for regulatory review or audit
- Identify priority actions based on risk tier and compliance deadline

**How to use:** Complete the scorecard for each AI system in scope. Systems at different risk tiers will have different applicable requirements — the scorecard identifies N/A items automatically via the tier columns.

---

## Document Control

| Field | Entry |
|---|---|
| Organisation Name | |
| Scorecard Version | |
| Scoring Date | |
| Scored By | |
| Approved By | |
| Next Review Date | |
| Regulatory Deadline Focus | High-Risk Annex I: Aug 2026 / All provisions: Aug 2027 |

---

## Part 1 — AI System Portfolio Summary

Complete one row per AI system identified in your AI System Register (Document 05).

| System ID | System Name | Risk Tier | Annex III Category | Art. 6(3) Exclusion? | Provider / Deployer / Both | Compliance Deadline |
|---|---|---|---|---|---|---|
| | | Unacceptable / High / Limited / Minimal | | Yes / No | | |

**Portfolio Summary:**

| Risk Tier | Count | % of Portfolio | Priority Level |
|---|---|---|---|
| Unacceptable (must be withdrawn) | | | CRITICAL — immediate action |
| High Risk | | | HIGH — August 2026 / 2027 |
| Limited Risk | | | MEDIUM — ongoing obligations |
| Minimal Risk | | | LOW — voluntary only |

---

## Part 2 — Scorecard Scoring Guide

Use the following status codes throughout the scorecard:

| Code | Meaning |
|---|---|
| DONE | Requirement fully met; evidence available |
| IN PROGRESS | Partially completed; on track |
| GAP | Not started or materially incomplete |
| N/A | Not applicable to this risk tier or role |
| PENDING | Awaiting external input (e.g. EU database, Notified Body) |

**Priority codes:**

| Code | Meaning |
|---|---|
| P1 | Critical — blocks market placement or continued operation |
| P2 | High — required before or immediately after market placement |
| P3 | Medium — ongoing obligation; address within 90 days |
| P4 | Low — best practice or periodic obligation |

---

## Part 3 — Foundation: Risk Classification and Scoping

*Applies to: All organisations, all AI systems*
*Reference: Document 01 — 01-RISK-CLASSIFICATION-GUIDE.md*

| # | Requirement | Status | Priority | Evidence / Notes | Owner | Due Date |
|---|---|---|---|---|---|---|
| 1.1 | All AI systems identified and inventoried | | P1 | | | |
| 1.2 | Each system assessed under Article 3(1) — is it an AI system? | | P1 | | | |
| 1.3 | Each system checked against Article 5 prohibited practices | | P1 | | | |
| 1.4 | Each system assessed for Annex I high-risk (Article 6(1)) | | P1 | | | |
| 1.5 | Each system assessed for Annex III high-risk (Article 6(2)) | | P1 | | | |
| 1.6 | Article 6(3) exclusion assessed where Annex III applies | | P1 | | | |
| 1.7 | Article 6(3) exclusions documented and approved | | P2 | | | |
| 1.8 | Each system checked for limited-risk / Article 50 obligations | | P2 | | | |
| 1.9 | Risk classification decisions recorded in AI System Register | | P2 | | | |
| 1.10 | FRIA scoping decision completed for each high-risk system | | P2 | | | |

**Section 3 Status: ___ / 10 DONE**

---

## Part 4 — High-Risk AI: Pre-Market Requirements

*Applies to: Providers of High-Risk AI Systems (all Annex I and Annex III systems)*

### 4.1 Risk Management System (Article 9)
*Reference: Document 02, Section A*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 2.1 | Risk management system established and documented | | P1 | | |
| 2.2 | Risks identified for each intended purpose and foreseeable misuse | | P1 | | |
| 2.3 | Risk estimation and evaluation completed | | P1 | | |
| 2.4 | Risk management measures adopted | | P1 | | |
| 2.5 | Residual risks documented and communicated to deployers | | P2 | | |
| 2.6 | Risk management system tested with real-world conditions | | P1 | | |
| 2.7 | Risk management is iterative throughout lifecycle | | P3 | | |

### 4.2 Data and Data Governance (Article 10)
*Reference: Documents 02 (Section B), 04 (Section 2.5), 18*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 3.1 | Training, validation, and test data subject to governance practices | | P1 | | |
| 3.2 | Data is relevant and sufficiently representative | | P1 | | |
| 3.3 | Data has appropriate statistical properties | | P1 | | |
| 3.4 | Bias examination conducted | | P1 | | |
| 3.5 | Personal data safeguards in place; GDPR alignment confirmed | | P1 | See Doc 18 | |
| 3.6 | Data provenance documented in technical documentation | | P2 | | |

### 4.3 Technical Documentation (Article 11 + Annex IV)
*Reference: Document 04*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 4.1 | Technical documentation prepared before market placement | | P1 | | |
| 4.2 | All 8 Annex IV sections completed | | P1 | | |
| 4.3 | Documentation up to date and version controlled | | P2 | | |
| 4.4 | 10-year retention plan in place | | P2 | | |

### 4.4 Logging and Record-Keeping (Article 12)
*Reference: Document 02 (Section D), Document 04 (Section 3.4)*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 5.1 | Automatic logging capability built into system | | P1 | | |
| 5.2 | Logging covers full operational lifetime | | P1 | | |
| 5.3 | Log types and retention periods documented | | P2 | | |

### 4.5 Transparency and Instructions for Use (Article 13)
*Reference: Document 02 (Section E)*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 6.1 | Instructions for use prepared and reviewed | | P1 | | |
| 6.2 | Instructions include all Article 13(3) required content | | P1 | | |
| 6.3 | Instructions provided to deployers | | P1 | | |

### 4.6 Human Oversight (Article 14)
*Reference: Document 07*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 7.1 | System designed to be effectively overseen by natural persons | | P1 | | |
| 7.2 | Oversight measures identified and built into system design | | P1 | | |
| 7.3 | Override and stop mechanisms implemented and tested | | P1 | | |
| 7.4 | Automation bias risks identified and mitigations in place | | P2 | | |
| 7.5 | Oversight roles defined and persons assigned (Article 14(3)) | | P2 | See Doc 17 | |

### 4.7 Accuracy, Robustness, Cybersecurity (Article 15)
*Reference: Document 02 (Section G)*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 8.1 | Accuracy metrics achieved and declared | | P1 | | |
| 8.2 | System resilient against errors and faults | | P1 | | |
| 8.3 | Cybersecurity measures implemented | | P1 | | |
| 8.4 | Technical redundancy / fail-safe plans in place | | P2 | | |

### 4.8 Quality Management System (Article 17)
*Reference: Document 16*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 9.1 | QMS established and documented | | P1 | See Doc 16 | |
| 9.2 | QMS covers all Article 17(1)(a)-(g) elements | | P1 | | |
| 9.3 | QMS approved by Senior Responsible Officer | | P1 | | |

---

## Part 5 — High-Risk AI: Conformity and Market Placement

### 5.1 Conformity Assessment (Articles 43-48)
*Reference: Document 02*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 10.1 | Conformity assessment completed before market placement | | P1 | | |
| 10.2 | Assessment method identified (internal vs. Notified Body) | | P1 | See Doc 20 | |
| 10.3 | Conformity assessment result: CONFORMANT / CONDITIONAL / NON-CONFORMANT | | P1 | | |
| 10.4 | Remediation plan in place if CONDITIONAL | | P1 | | |

### 5.2 EU Declaration of Conformity (Article 47)
*Reference: Document 12*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 11.1 | EU Declaration of Conformity drafted | | P1 | | |
| 11.2 | DoC references all applicable requirements and standards | | P1 | | |
| 11.3 | DoC signed by authorised person | | P1 | | |
| 11.4 | DoC retained for 10 years | | P2 | | |

### 5.3 EU Database Registration (Articles 49, 71)
*Reference: Document 05*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 12.1 | System registered in EU AI database before market placement | | P1 | | |
| 12.2 | Registration number recorded in AI System Register | | P1 | | |

### 5.4 CE Marking (Article 48)
*Reference: Document 14*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 13.1 | CE marking requirement assessed | | P2 | | |
| 13.2 | CE marking affixed where required | | P1 | N/A if not Annex I | |

---

## Part 6 — Deployer Obligations

*Applies to: Deployers of High-Risk AI Systems*
*Reference: Document 10*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 14.1 | System used in accordance with provider's instructions for use | | P2 | | |
| 14.2 | Human oversight assigned to competent, authorised persons (Art. 26(2)) | | P1 | See Doc 17 | |
| 14.3 | Input data is relevant and representative (Art. 26(3)) | | P2 | | |
| 14.4 | System operation monitored (Art. 26(4)) | | P2 | | |
| 14.5 | Serious incidents reported to provider / MSA (Art. 26(5)) | | P1 | See Doc 08 | |
| 14.6 | Logs retained where within deployer's control (Art. 26(6)) | | P2 | | |
| 14.7 | Workers and representatives informed before workplace AI deployment (Art. 26(7)) | | P2 | | |
| 14.8 | Transparency obligations with natural persons met (Art. 26(8)) | | P2 | See Doc 06 | |

---

## Part 7 — FRIA (Article 27)

*Applies to: Public sector deployers and private bodies providing public services in regulated sectors*
*Reference: Document 03*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 15.1 | FRIA scoping decision completed | | P1 | | |
| 15.2 | FRIA mandatory — public body or public-service deployer | | P1 | N/A if not applicable | |
| 15.3 | FRIA completed before deployment | | P1 | | |
| 15.4 | FRIA outcome: APPROVED / APPROVED WITH CONDITIONS / DEFERRED / REJECTED | | P1 | | |
| 15.5 | Conditions / mitigations from FRIA implemented | | P1 | | |
| 15.6 | FRIA signed off by Senior Responsible Officer and DPO | | P2 | | |

---

## Part 8 — Limited Risk: Transparency Obligations (Article 50)

*Applies to: All providers/deployers of chatbots, deepfake AI, emotion recognition, GPAI*
*Reference: Document 06*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 16.1 | Chatbot / conversational AI disclosure implemented | | P2 | N/A if no chatbot | |
| 16.2 | Deepfake / AI-generated content labelling implemented | | P2 | N/A if no gen AI | |
| 16.3 | Emotion recognition / biometric categorisation disclosure implemented | | P2 | N/A if not applicable | |
| 16.4 | User rights information (GDPR Arts. 21-22) provided | | P2 | See Doc 18 | |

---

## Part 9 — GPAI Model Obligations (Articles 51-56)

*Applies to: Providers of GPAI models (foundation models, LLMs)*
*Reference: Document 11*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 17.1 | GPAI technical documentation (Annex XI) prepared and kept up to date | | P1 | | |
| 17.2 | Information provided to downstream providers | | P1 | | |
| 17.3 | EU copyright compliance policy in place | | P1 | | |
| 17.4 | Training data summary published | | P1 | | |
| 17.5 | Systemic risk designation assessed (>10^25 FLOPs?) | | P1 | N/A if below threshold | |
| 17.6 | Red-teaming / adversarial testing completed (systemic risk only) | | P1 | N/A if not systemic | |
| 17.7 | EU AI Office incident reporting in place (systemic risk only) | | P1 | N/A if not systemic | |
| 17.8 | Energy efficiency reporting in place (systemic risk only) | | P2 | N/A if not systemic | |

---

## Part 10 — Ongoing Obligations: Post-Market and Incidents

*Applies to: Providers of High-Risk AI Systems (ongoing)*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 18.1 | Post-market monitoring plan established (Art. 72) | | P1 | See Doc 09 | |
| 18.2 | Continuous automated performance monitoring active | | P2 | | |
| 18.3 | Deployer feedback collection mechanism in place | | P2 | | |
| 18.4 | Drift detection implemented | | P2 | | |
| 18.5 | Serious incident reporting procedure operational (Art. 73) | | P1 | See Doc 08 | |
| 18.6 | Incident register maintained | | P2 | | |
| 18.7 | Substantial modification assessment procedure in place (Art. 25) | | P2 | | |

---

## Part 11 — Supply Chain: Non-EU Providers, Importers, Distributors

*Reference: Documents 13, 14, 15*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 19.1 | Authorised Representative designated (non-EU providers) | | P1 | N/A if EU provider | See Doc 13 |
| 19.2 | AR registered in EU AI database | | P1 | N/A if EU provider | |
| 19.3 | Importer pre-market verification completed | | P1 | N/A if not Importer | See Doc 15 |
| 19.4 | Distributor pre-distribution verification completed | | P1 | N/A if not Distributor | See Doc 15 |
| 19.5 | Supply chain due diligence register maintained | | P2 | | |

---

## Part 12 — AI Literacy and Competency (Article 4)

*Applies to: All providers and deployers*
*Reference: Document 17*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 20.1 | AI literacy programme established | | P2 | See Doc 17 | |
| 20.2 | Role-based training requirements defined | | P2 | | |
| 20.3 | All staff completed required training modules | | P2 | | |
| 20.4 | AI oversight persons certified per Article 14(3) | | P1 | | |
| 20.5 | Training records maintained | | P3 | | |

---

## Part 13 — GDPR and AI Act Joint Compliance

*Applies to: All organisations processing personal data in AI systems*
*Reference: Document 18*

| # | Requirement | Status | Priority | Evidence / Notes | Owner |
|---|---|---|---|---|---|
| 21.1 | Personal data inventory for all AI systems completed | | P1 | See Doc 18 | |
| 21.2 | Lawful basis for all AI-related processing identified | | P1 | | |
| 21.3 | Privacy notices updated for AI processing disclosure | | P2 | | |
| 21.4 | Automated decision-making assessment (GDPR Art. 22) completed | | P1 | | |
| 21.5 | DPIA completed where required (GDPR Art. 35) | | P1 | | |
| 21.6 | DPO consulted on all high-risk AI deployments | | P2 | | |
| 21.7 | Data subject rights procedures updated for AI context | | P2 | | |
| 21.8 | Dual incident reporting procedure (MSA + DPA) in place | | P1 | | |

---

## Part 14 — Consolidated Gap Summary

After completing all sections, summarise your compliance position here:

### 14.1 Overall Scorecard Summary

| Section | Total Items | DONE | IN PROGRESS | GAP | N/A | % Complete |
|---|---|---|---|---|---|---|
| 3 — Risk Classification | 10 | | | | | |
| 4 — Pre-Market (High Risk) | 29 | | | | | |
| 5 — Conformity and Placement | 10 | | | | | |
| 6 — Deployer Obligations | 8 | | | | | |
| 7 — FRIA | 6 | | | | | |
| 8 — Limited Risk Transparency | 4 | | | | | |
| 9 — GPAI | 8 | | | | | |
| 10 — Post-Market and Incidents | 7 | | | | | |
| 11 — Supply Chain | 5 | | | | | |
| 12 — AI Literacy | 5 | | | | | |
| 13 — GDPR Intersection | 8 | | | | | |
| **TOTAL** | **100** | | | | | |

### 14.2 P1 Critical Gaps (Action Required Before Market Placement)

| Gap ID | Section | Requirement | Action Required | Owner | Target Date |
|---|---|---|---|---|---|
| G-001 | | | | | |

### 14.3 P2 High Priority Gaps (Address Within 30 Days)

| Gap ID | Section | Requirement | Action Required | Owner | Target Date |
|---|---|---|---|---|---|
| G-010 | | | | | |

### 14.4 P3 Medium Priority Gaps (Address Within 90 Days)

| Gap ID | Section | Requirement | Action Required | Owner | Target Date |
|---|---|---|---|---|---|
| G-020 | | | | | |

---

## Part 15 — Executive Summary Dashboard

Designed for presentation to senior leadership and the board:

| Metric | Value |
|---|---|
| Total AI systems inventoried | |
| High-risk AI systems | |
| Systems with P1 gaps | |
| Systems compliant / ready for market | |
| Overall compliance completion % | |
| Regulatory deadline (primary) | August 2026 (Annex I high-risk) |
| Estimated completion date (current trajectory) | |
| Budget required to close P1 gaps | |

**Traffic Light Summary:**

| Compliance Area | Status |
|---|---|
| Risk Classification | GREEN / AMBER / RED |
| Conformity Assessments | GREEN / AMBER / RED |
| Technical Documentation | GREEN / AMBER / RED |
| Human Oversight | GREEN / AMBER / RED |
| Post-Market Monitoring | GREEN / AMBER / RED |
| Incident Reporting | GREEN / AMBER / RED |
| Quality Management | GREEN / AMBER / RED |
| AI Literacy | GREEN / AMBER / RED |
| GDPR Intersection | GREEN / AMBER / RED |
| **Overall** | **GREEN / AMBER / RED** |

---

## Part 16 — Scorecard Review History

| Version | Date | Scored By | Key Findings | Approved By |
|---|---|---|---|---|
| 1.0 | | | Initial assessment | |

---

*Part of the EU AI Act Compliance Toolkit*
*This document does not constitute legal advice. Seek qualified legal counsel for binding compliance determinations.*
