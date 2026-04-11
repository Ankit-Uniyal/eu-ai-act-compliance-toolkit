# 04 — Technical Documentation Template (Annex IV)

**EU AI Act Reference:** Article 11 | Annex IV  
**Applies to:** Providers of High-Risk AI Systems  
**Retention Period:** 10 years after last placement on market (Article 18)  
**Last Updated:** April 2026

---

## Purpose

Article 11 requires providers of high-risk AI systems to draw up technical documentation **before** the system is placed on the market or put into service. The documentation must be kept up to date and made available to market surveillance authorities on request.

This template follows the structure prescribed in **Annex IV** of the EU AI Act.

---

## Document Control

| Field | Entry |
|-------|-------|
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

> *Describe the specific purpose for which the AI system is intended, including the specific context and conditions of use, the categories of natural persons and groups it is intended to be used upon, and the users it is intended for.*

### 1.2 System Description

| Field | Description |
|-------|-------------|
| System name and version | |
| Category of AI system | |
| Hardware the system is intended to run on | |
| Software (OS, frameworks, dependencies) | |
| Form (product / standalone / embedded) | |
| Intended deployment territory | |
| Provider name and address | |
| EU Authorised Representative (if applicable) | |

### 1.3 Interaction with Hardware / Software

> *Describe how the AI system interacts with other hardware or software that is not part of the AI system itself.*

### 1.4 Versions of Relevant Software

| Software Component | Version | Licence |
|-------------------|---------|---------|
| | | |
| | | |

### 1.5 Description of Deployment

> *Describe each deployment form in which the AI system is placed on the market or put into service.*

### 1.6 Instructions for Use (Summary)

> *Provide the instructions for use, including: a concise general description of the AI system; its characteristics, capabilities, and limitations; information regarding the accuracy and robustness of the system.*

---

## Annex IV, Section 2 — Detailed Description of Elements

### 2.1 Methods and Steps for System Development

> *Describe the methods and steps performed for the development of the AI system, including the relevant design choices and their rationale.*

### 2.2 Design Specifications

| Specification | Detail |
|--------------|--------|
| Overall architecture | |
| Number and type of models | |
| Training methodology | |
| Optimisation techniques | |
| Key design decisions | |
| Rejected alternatives and rationale | |

### 2.3 System Architecture

> *Provide an architectural diagram or description showing all components and their interactions.*

```
[Insert system architecture diagram here]
```

### 2.4 Model Information

| Field | Detail |
|-------|--------|
| Model type(s) | |
| Model size (parameters) | |
| Training approach | Supervised / Unsupervised / Reinforcement / Other |
| Fine-tuning approach (if applicable) | |
| Inference method | |

### 2.5 Training, Validation, and Testing Data

#### Training Data

| Field | Detail |
|-------|--------|
| Data source(s) | |
| Data collection method | |
| Data volume | |
| Data format | |
| Date range of data | |
| Personal data included? | Yes / No |
| Special category data? | Yes / No |
| Data governance measures | |
| Bias assessment conducted? | Yes / No — Reference: |

#### Validation Data

| Field | Detail |
|-------|--------|
| Validation dataset description | |
| Validation approach | |
| Validation metrics used | |

#### Test Data

| Field | Detail |
|-------|--------|
| Test dataset description | |
| Holdout / test split | |
| Real-world test conditions | |

### 2.6 Data Labelling and Annotation

> *Describe the data labelling procedures and any annotation instructions used.*

### 2.7 Metrics and Performance

| Metric | Value | Benchmark / Threshold |
|--------|-------|----------------------|
| Accuracy | | |
| Precision | | |
| Recall | | |
| F1 Score | | |
| AUC-ROC | | |
| Fairness metric | | |
| Other: | | |

### 2.8 Computational Resources

| Resource | Specification |
|----------|--------------|
| Training infrastructure | |
| Cloud / On-premise | |
| Estimated training compute | |
| Inference infrastructure | |

---

## Annex IV, Section 3 — Monitoring, Functioning, and Control

### 3.1 Capabilities and Limitations

> *Describe the capabilities and limitations of the AI system, including the foreseeable circumstances that may lead to risks to health, safety, or fundamental rights.*

| Capability | Description |
|-----------|-------------|
| | |

| Limitation | Impact | Mitigation |
|-----------|--------|-----------|
| | | |

### 3.2 Reasonably Foreseeable Misuse

| Misuse Scenario | Likelihood | Impact | Mitigation |
|----------------|-----------|--------|-----------|
| | | | |
| | | | |

### 3.3 Human Oversight Measures

> *Describe the measures put in place to enable humans to oversee the AI system, including the technical measures to facilitate interpretation by deployers.*

### 3.4 Logging Capabilities

| Log Type | Retained For | Format | Access |
|----------|-------------|--------|--------|
| Operation logs | | | |
| Decision logs | | | |
| Error logs | | | |
| Audit trail | | | |

### 3.5 Performance on Specific Groups

| Group | Performance Notes | Disparity Identified? |
|-------|-----------------|----------------------|
| | | |

---

## Annex IV, Section 4 — Risk Management

### 4.1 Risk Management System Overview

> *Describe the risk management system established in accordance with Article 9.*

### 4.2 Risk Register Summary

| Risk ID | Risk Description | Likelihood | Severity | Residual Risk | Mitigation |
|---------|-----------------|-----------|---------|--------------|-----------|
| R-001 | | | | | |
| R-002 | | | | | |

### 4.3 Cybersecurity Measures

> *Describe the measures implemented to address cybersecurity risks, including resilience against attempts to alter use or performance.*

---

## Annex IV, Section 5 — Changes Made Over Lifecycle

| Version | Date | Changes Made | Change Reason | Approved By |
|---------|------|-------------|--------------|------------|
| v1.0 | | Initial release | | |
| | | | | |

---

## Annex IV, Section 6 — Standards Applied

| Standard | Version | Scope of Application |
|----------|---------|---------------------|
| ISO/IEC 42001:2023 | | AI Management Systems |
| ISO/IEC 27001 | | Information Security |
| ISO 31000 | | Risk Management |
| Other: | | |

---

## Annex IV, Section 7 — EU Declaration of Conformity

> *Reference or attach the EU Declaration of Conformity drawn up in accordance with Article 47.*

**Declaration Reference:** _______________  
**Date of Declaration:** _______________  
**Notified Body (if applicable):** _______________  
**Notified Body Certificate Number:** _______________

---

## Annex IV, Section 8 — Post-Market Monitoring

> *Describe the post-market monitoring plan in accordance with Article 72.*

**Reference:** See [09-POST-MARKET-MONITORING-PLAN.md](09-POST-MARKET-MONITORING-PLAN.md)

---

*Part of the [EU AI Act Compliance Toolkit](README.md)*
