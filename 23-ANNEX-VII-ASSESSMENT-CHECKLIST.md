# 23 — Annex VII Assessment Criteria Checklist

**EU AI Act Reference:** Annex VII | Article 43 | Article 44
**Applies to:** Providers of high-risk AI systems requiring Notified Body (NB) assessment; internal conformity teams preparing documentation packages
**Last Updated:** April 2026

## Purpose

Annex VII of the EU AI Act sets out the technical requirements for the conformity assessment procedure based on assessment of the quality management system and assessment of the technical documentation. This checklist maps what a Notified Body (NB) will review against specific Article requirements, enabling providers to:

- Self-assess readiness before engaging an NB
- Prepare complete documentation packages
- Anticipate NB findings and pre-emptively remediate gaps
- Understand the evidence standard required for each requirement

This checklist is organised to mirror the NB's assessment sequence: QMS assessment first, then technical documentation assessment.

> **Note:** This checklist reflects the Annex VII structure as enacted in Regulation (EU) 2024/1689. The EU AI Act does not prescribe specific test methods or harmonised standards for all requirements; where standards are absent, NBs apply general conformity assessment methodology. As harmonised standards are published under the AI Act, update this checklist accordingly.

## Document Control

| Field | Entry |
|---|---|
| AI System Name | |
| System ID | |
| Assessment Type | Internal pre-assessment / NB submission readiness |
| Assessed By | |
| Date | |
| Reference: Internal Conformity Assessment | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md |
| Reference: Technical Documentation | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| Reference: QMS | 16-QUALITY-MANAGEMENT-SYSTEM.md |

---

## Part 1 — Phase 1: Quality Management System Assessment

Under Annex VII, the NB first assesses the provider's QMS to determine whether it adequately ensures compliance with applicable requirements.

### 1.1 QMS Documentation Review

The NB will review the QMS documentation to verify it covers all Article 17(1)(a)-(g) requirements.

| # | What the NB Checks | EU AI Act Reference | Evidence Required | Readiness (Green / Amber / Red) | Notes |
|---|---|---|---|---|---|
| QMS-01 | QMS document is in place and version controlled | Art. 17 | QMS document (Doc 16); version history | | |
| QMS-02 | QMS scope covers the specific AI system under assessment | Art. 17 | QMS scope statement; system ID cross-reference | | |
| QMS-03 | Compliance strategy documented — Art. 17(1)(a) | Art. 17(1)(a) | Doc 16 Part 3; standards gap assessment | | |
| QMS-04 | Design and development procedures documented — Art. 17(1)(b) | Art. 17(1)(b) | Doc 16 Part 4; lifecycle gate records | | |
| QMS-05 | Testing, validation, and examination procedures documented — Art. 17(1)(c) | Art. 17(1)(c) | Test plans; validation methodology; test reports | | |
| QMS-06 | Technical specifications and standards strategy documented — Art. 17(1)(d) | Art. 17(1)(d) | Standards list; gap assessment vs. harmonised standards | | |
| QMS-07 | Data management procedures documented — Art. 17(1)(e) | Art. 17(1)(e) | Data governance policy; bias audit procedure | | |
| QMS-08 | Risk management system documented — Art. 17(1)(f) | Art. 17(1)(f) | Risk management procedure; risk register (Doc 02) | | |
| QMS-09 | Post-market monitoring system documented — Art. 17(1)(g) | Art. 17(1)(g) | PMM Plan (Doc 09); monitoring procedure | | |
| QMS-10 | Incident reporting procedure documented | Art. 17(1)(g) + Art. 73 | Incident procedure (Doc 08); notification timelines | | |
| QMS-11 | Roles and responsibilities assigned and documented | Art. 17 | Roles table (Doc 16 Part 2); named individuals | | |
| QMS-12 | QMS approved by senior management | Art. 17 | Signed approval; management review record | | |
| QMS-13 | Internal audit procedure established | Art. 17 | Audit schedule (Doc 16 Part 9); last audit report | | |
| QMS-14 | CAPA (corrective and preventive action) process established | Art. 17 | CAPA log (Doc 16 Part 10); CAPA procedure | | |
| QMS-15 | Change management procedure for substantial modifications | Art. 25 | Change assessment log; substantial modification criteria | | |

**QMS Assessment Summary:**

| Status | Count |
|---|---|
| Green (evidence ready) | |
| Amber (partial evidence; needs improvement) | |
| Red (gap; NB finding likely) | |

---

## Part 2 — Phase 2: Technical Documentation Assessment

After the QMS assessment, the NB assesses whether the technical documentation demonstrates the system meets all Chapter III Section 2 requirements.

### 2.1 Annex IV Section 1 — General Description

| # | What the NB Checks | AI Act Reference | Evidence Required | Readiness | Notes |
|---|---|---|---|---|---|
| TD-01 | Intended purpose clearly defined | Art. 13(3)(a); Annex IV §1 | Doc 04 Section 1.1; intended purpose statement | | |
| TD-02 | System description complete (hardware, software, deployment forms) | Annex IV §1 | Doc 04 Section 1.2-1.5 | | |
| TD-03 | Interaction with other hardware/software described | Annex IV §1 | Doc 04 Section 1.3 | | |
| TD-04 | Relevant software versions documented | Annex IV §1 | Doc 04 Section 1.4 | | |
| TD-05 | Instructions for use (summary) included | Art. 13; Annex IV §1 | Doc 04 Section 1.6; instructions for use document | | |

### 2.2 Annex IV Section 2 — Detailed System Description

| # | What the NB Checks | AI Act Reference | Evidence Required | Readiness | Notes |
|---|---|---|---|---|---|
| TD-06 | Development methodology and design choices documented | Annex IV §2; Art. 11 | Doc 04 Section 2.1-2.2 | | |
| TD-07 | System architecture described or diagrammed | Annex IV §2 | Doc 04 Section 2.3; architecture diagram | | |
| TD-08 | Model information documented (type, size, training approach) | Annex IV §2 | Doc 04 Section 2.4 | | |
| TD-09 | Training data documented (sources, volume, format, provenance) | Art. 10; Annex IV §2 | Doc 04 Section 2.5 training data fields | | |
| TD-10 | Data governance measures documented (personal data, bias) | Art. 10; Annex IV §2 | Doc 04 Section 2.5; GDPR mapping (Doc 18) | | |
| TD-11 | Validation and test data documented | Art. 10; Annex IV §2 | Doc 04 Section 2.5 validation/test fields | | |
| TD-12 | Bias examination conducted and documented | Art. 10(2)(f) | Bias audit report; methodology; results | | |
| TD-13 | Performance metrics documented and benchmarks declared | Art. 15; Annex IV §2 | Doc 04 Section 2.7; benchmark table | | |
| TD-14 | Data labelling and annotation procedures documented | Art. 10; Annex IV §2 | Doc 04 Section 2.6 | | |

### 2.3 Annex IV Section 3 — Monitoring, Functioning, and Control

| # | What the NB Checks | AI Act Reference | Evidence Required | Readiness | Notes |
|---|---|---|---|---|---|
| TD-15 | Capabilities and limitations documented (including foreseeable misuse) | Art. 9; Annex IV §3 | Doc 04 Section 3.1-3.2 | | |
| TD-16 | Human oversight measures described (design and implementation) | Art. 14; Annex IV §3 | Doc 04 Section 3.3; Doc 07 | | |
| TD-17 | Logging capabilities implemented and documented | Art. 12; Annex IV §3 | Doc 04 Section 3.4; logging architecture evidence | | |
| TD-18 | Performance on specific demographic groups assessed | Art. 10(2)(f); Annex IV §3 | Doc 04 Section 3.5; demographic performance analysis | | |

### 2.4 Annex IV Section 4 — Risk Management

| # | What the NB Checks | AI Act Reference | Evidence Required | Readiness | Notes |
|---|---|---|---|---|---|
| TD-19 | Risk management system overview documented | Art. 9; Annex IV §4 | Doc 04 Section 4.1 | | |
| TD-20 | Risk register populated with identified risks, evaluations, and mitigations | Art. 9; Annex IV §4 | Doc 04 Section 4.2; risk register | | |
| TD-21 | Cybersecurity measures documented | Art. 15; Annex IV §4 | Doc 04 Section 4.3; cybersecurity assessment | | |

### 2.5 Annex IV Section 5 — Lifecycle Changes

| # | What the NB Checks | AI Act Reference | Evidence Required | Readiness | Notes |
|---|---|---|---|---|---|
| TD-22 | Version history and changes documented | Art. 25; Annex IV §5 | Doc 04 Section 5; change log | | |
| TD-23 | Substantial modification assessment procedure referenced | Art. 25 | QMS change management procedure | | |

### 2.6 Annex IV Section 6 — Standards Applied

| # | What the NB Checks | AI Act Reference | Evidence Required | Readiness | Notes |
|---|---|---|---|---|---|
| TD-24 | Standards applied documented (harmonised and others) | Art. 9; Annex IV §6 | Doc 04 Section 6; standards table | | |
| TD-25 | Where harmonised standards not fully applied, alternative means documented | Art. 9; Annex IV §6 | Standards gap assessment; justification for deviations | | |

### 2.7 Annex IV Section 7 — EU Declaration of Conformity

| # | What the NB Checks | AI Act Reference | Evidence Required | Readiness | Notes |
|---|---|---|---|---|---|
| TD-26 | Draft EU Declaration of Conformity prepared and referenced | Art. 47; Annex IV §7 | Draft DoC (Doc 12); references to applicable provisions | | |
| TD-27 | DoC references all applicable requirements | Art. 47 | Doc 12 checklist; complete | | |

### 2.8 Annex IV Section 8 — Post-Market Monitoring

| # | What the NB Checks | AI Act Reference | Evidence Required | Readiness | Notes |
|---|---|---|---|---|---|
| TD-28 | PMM plan described in technical documentation | Art. 72; Annex IV §8 | Doc 04 Section 8; PMM plan summary | | |
| TD-29 | PMM plan (full document) available | Art. 72 | Doc 09 (Post-Market Monitoring Plan) | | |
| TD-30 | Performance monitoring methodology described (metrics, thresholds, frequency) | Art. 72 | Doc 04 Section 8.2; Doc 09 | | |
| TD-31 | Trigger criteria for reactive review documented | Art. 72 | Doc 04 Section 8.4 | | |
| TD-32 | Corrective action process for PMM findings documented | Art. 72 | Doc 04 Section 8.5 | | |

---

## Part 3 — Substantive Requirements Assessment

Beyond documentation completeness, the NB assesses whether the AI system actually meets the substantive requirements.

### 3.1 Risk Management (Article 9)

| # | What the NB Assesses | Substantive Standard | Evidence of Compliance | Readiness | Notes |
|---|---|---|---|---|---|
| RM-01 | Risk management system is iterative and integrated throughout lifecycle | Art. 9(1) | Risk management procedure shows lifecycle integration | | |
| RM-02 | All known reasonably foreseeable risks identified | Art. 9(2) | Risk register comprehensive; foreseeable misuse covered | | |
| RM-03 | Risk estimation and evaluation methodology sound | Art. 9(3) | Likelihood × severity matrix; residual risk analysis | | |
| RM-04 | Risk management measures appropriate and proportionate | Art. 9(4) | Evidence measures match risk severity | | |
| RM-05 | Testing against real-world conditions documented | Art. 9(6)-(7) | Real-world test evidence; edge case testing | | |

### 3.2 Data Governance (Article 10)

| # | What the NB Assesses | Substantive Standard | Evidence of Compliance | Readiness | Notes |
|---|---|---|---|---|---|
| DG-01 | Data is relevant to intended purpose (no mission creep) | Art. 10(2)(a) | Data purpose mapping; collection justification | | |
| DG-02 | Data is sufficiently representative of intended deployment population | Art. 10(3) | Statistical analysis of population coverage | | |
| DG-03 | Bias examination conducted for all relevant protected characteristics | Art. 10(2)(f) | Bias audit report; demographic performance analysis | | |
| DG-04 | Special category data only used where strictly necessary | Art. 10(5) | Necessity assessment; GDPR Art. 9 basis documented | | |

### 3.3 Human Oversight (Article 14)

| # | What the NB Assesses | Substantive Standard | Evidence of Compliance | Readiness | Notes |
|---|---|---|---|---|---|
| HO-01 | System designed so natural persons can effectively oversee it | Art. 14(1) | Oversight design documentation; technical controls | | |
| HO-02 | Oversight measures implemented in system design (not just policy) | Art. 14(3) | Technical evidence: override mechanisms; stop function | | |
| HO-03 | Automation bias mitigations built in | Art. 14(4) | Design features limiting over-reliance; user interface design | | |
| HO-04 | Override / stop mechanism tested and documented | Art. 14(3) | Test results; override function verification | | |

### 3.4 Accuracy, Robustness, Cybersecurity (Article 15)

| # | What the NB Assesses | Substantive Standard | Evidence of Compliance | Readiness | Notes |
|---|---|---|---|---|---|
| AR-01 | Declared accuracy metric appropriate to use case | Art. 15(1) | Accuracy metric selection rationale | | |
| AR-02 | Declared accuracy level achieved and reproducible | Art. 15(1) | Test results; benchmark evidence | | |
| AR-03 | System robust against errors, faults, and inconsistencies | Art. 15(3) | Robustness testing results; fault tolerance evidence | | |
| AR-04 | Cybersecurity measures implemented against specific AI threats | Art. 15(5) | Cybersecurity assessment; adversarial testing if applicable | | |

### 3.5 Transparency (Article 13)

| # | What the NB Assesses | Substantive Standard | Evidence of Compliance | Readiness | Notes |
|---|---|---|---|---|---|
| TR-01 | Instructions for use contain all Art. 13(3) required elements | Art. 13(3) | Instructions for use document; Art. 13(3) checklist | | |
| TR-02 | Instructions adequate for deployers to implement human oversight | Art. 13(3)(e) | Instructions adequacy review | | |
| TR-03 | System identity disclosed (not presented as human) where applicable | Art. 13(1) | Transparency controls; disclosure mechanisms | | |

---

## Part 4 — Overall Assessment Readiness Summary

### 4.1 Traffic Light Summary

| Assessment Area | Status | Critical Gaps | Action Required Before NB Submission |
|---|---|---|---|
| QMS documentation | Green / Amber / Red | | |
| Annex IV — General Description | Green / Amber / Red | | |
| Annex IV — System Description | Green / Amber / Red | | |
| Annex IV — Monitoring and Control | Green / Amber / Red | | |
| Annex IV — Risk Management | Green / Amber / Red | | |
| Annex IV — Standards | Green / Amber / Red | | |
| Annex IV — DoC | Green / Amber / Red | | |
| Annex IV — PMM | Green / Amber / Red | | |
| Risk Management (Art. 9) | Green / Amber / Red | | |
| Data Governance (Art. 10) | Green / Amber / Red | | |
| Human Oversight (Art. 14) | Green / Amber / Red | | |
| Accuracy / Robustness (Art. 15) | Green / Amber / Red | | |
| Transparency (Art. 13) | Green / Amber / Red | | |
| **Overall NB Submission Readiness** | **Green / Amber / Red** | | |

### 4.2 Pre-Submission Remediation Log

| Item | Gap Description | Action Required | Owner | Due Date | Status |
|---|---|---|---|---|---|
| | | | | | |

### 4.3 Estimated NB Finding Risk

Based on this pre-assessment, estimate the likely NB finding risk:

| Finding Type | Likely Areas | Notes |
|---|---|---|
| Observations (minor improvements) | | |
| Minor non-conformances (rectifiable before certificate) | | |
| Major non-conformances (must be resolved; risk to certificate) | | |

---

## Related Documents

| Document | Reference |
|---|---|
| Conformity Assessment Checklist | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md |
| Technical Documentation Template | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| Quality Management System | 16-QUALITY-MANAGEMENT-SYSTEM.md |
| Post-Market Monitoring Plan | 09-POST-MARKET-MONITORING-PLAN.md |
| Notified Body Engagement Guide | 20-NOTIFIED-BODY-ENGAGEMENT-GUIDE.md |
| EU Declaration of Conformity | 12-EU-DECLARATION-OF-CONFORMITY.md |

---

*Part of the EU AI Act Compliance Toolkit*

*This document does not constitute legal advice. Notified Body assessment methodologies may vary. This checklist is based on the Annex VII structure in Regulation (EU) 2024/1689 and should be updated as harmonised standards are published.*
