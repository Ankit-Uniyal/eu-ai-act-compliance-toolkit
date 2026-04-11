# 09 — Post-Market Monitoring Plan

**EU AI Act Reference:** Article 72 | Article 61 (GPAI Models)  
**Applies to:** Providers of High-Risk AI Systems  
**Last Updated:** April 2026

---

## Purpose

Article 72 requires providers of high-risk AI systems to establish and document a post-market monitoring (PMM) system that actively collects and reviews data from users about the system's performance throughout its lifetime. This plan documents how that monitoring is implemented.

---

## Part 1 — System and Plan Information

| Field | Entry |
|-------|-------|
| System Name | |
| System ID | |
| Version | |
| Risk Classification | High Risk |
| Annex III Category | |
| PMM Plan Author | |
| Plan Version | |
| Plan Approval Date | |
| Next Plan Review Date | |

---

## Part 2 — Monitoring Objectives

| Objective | Description |
|-----------|-------------|
| Performance integrity | Ensure system accuracy and reliability remain within declared thresholds |
| Safety assurance | Detect any safety risks not identified during pre-market assessment |
| Fundamental rights monitoring | Identify discriminatory or rights-infringing outcomes in real-world use |
| Regulatory compliance | Confirm continued compliance with EU AI Act requirements |
| Incident detection | Identify serious incidents and emerging risks early |
| Continuous improvement | Feed findings into system updates and risk management |

---

## Part 3 — Data Collection

### 3.1 Data Sources

| Source | Data Collected | Collection Method | Frequency |
|--------|---------------|------------------|-----------|
| System logs (automated) | All inputs/outputs, errors, decisions | Automated logging | Continuous |
| User feedback (deployers) | Performance reports, complaints, anomalies | Structured reporting form | Monthly |
| Customer / end-user complaints | Reported errors, harms, anomalies | Helpdesk / feedback portal | Continuous |
| Monitoring dashboard | Accuracy, precision, recall, drift | Automated metrics | Daily |
| External sources | Regulatory guidance, academic research, comparable system incidents | Desk review | Quarterly |
| Incident register | Serious incidents and near-misses | Internal incident log | Continuous |

### 3.2 Logging Requirements (Article 12)

| Log Type | Content | Retention Period | Access Control |
|----------|---------|-----------------|---------------|
| Operational logs | Session start/end, inputs used, decisions generated | 10 years (or product lifetime) | Restricted |
| Error logs | System errors, anomalies, unexpected behaviours | 10 years | Restricted |
| Audit trail | Who accessed system, what actions taken | 10 years | Audit team |
| Performance metrics | Accuracy, precision, recall, drift metrics | 10 years | AI Governance |

---

## Part 4 — Performance Metrics and Thresholds

| Metric | Baseline Value | Alert Threshold | Critical Threshold | Review Action |
|--------|---------------|----------------|-------------------|---------------|
| Accuracy | | < [X]% | < [Y]% | Investigate / Suspend |
| Precision | | | | |
| Recall | | | | |
| False Positive Rate | | | | |
| False Negative Rate | | | | |
| Fairness (demographic parity) | | | | |
| Availability / Uptime | | | | |
| Data drift score | | | | |
| Model drift score | | | | |

---

## Part 5 — Monitoring Activities and Schedule

| Activity | Description | Frequency | Owner | Output |
|----------|-------------|-----------|-------|--------|
| Automated performance monitoring | Real-time metric tracking via dashboard | Continuous | Technical Team | Alerts |
| Weekly performance review | Review of metrics vs thresholds | Weekly | AI Oversight Officer | Report |
| Deployer feedback review | Collect and analyse deployer reports | Monthly | AI Governance | Issues log |
| Bias and fairness audit | Statistical analysis for discriminatory outcomes | Quarterly | Compliance | Audit report |
| Model drift assessment | Detect distribution shifts vs training data | Quarterly | Technical Team | Drift report |
| Full PMM review | Comprehensive review of all monitoring data | Annually | AI Governance Lead | PMM report |
| Regulatory review | Assess against updated regulatory guidance | As needed | Legal | Compliance note |

---

## Part 6 — Risk-Triggered Review Criteria

The following events trigger an immediate unscheduled review:

| Trigger Event | Action Required | Timeline |
|--------------|----------------|---------|
| Serious incident reported | Suspend system; conduct root cause analysis | Immediate |
| Performance metric breach (critical threshold) | Alert, investigate, consider suspension | Within 24 hours |
| Regulatory guidance update | Assess impact on compliance obligations | Within 2 weeks |
| System update or significant change | Re-assess risk; update technical documentation | Before deployment |
| Significant change in deployment context | Re-assess risk; consider FRIA update | Before change |
| New evidence of bias or discrimination | Investigate; notify deployers; consider recall | Within 48 hours |
| Complaint or legal challenge | Investigate; document; notify MSA if serious | Within 72 hours |

---

## Part 7 — Corrective Actions and System Updates

| Trigger | Corrective Action Types | Responsibility | Notification Required |
|---------|------------------------|---------------|----------------------|
| Performance degradation | Retrain model / adjust parameters | Technical Lead | Deployers |
| Bias detected | Retrain with corrected data / adjust thresholds | Technical Lead + Compliance | Deployers + MSA if serious |
| Security vulnerability | Patch / update / mitigate | Security Team | Deployers |
| Serious incident | Investigate / suspend / notify / correct | AI Governance Lead | MSA + deployers |
| Regulatory change | Update system / documentation / procedures | Compliance | Deployers |

**When a system update is required:**

1. Document the change in technical documentation (Annex IV, Section 5)
2. Assess whether change constitutes a substantial modification (Article 25)
3. If substantial modification: re-run conformity assessment
4. Notify deployers of update and any changed instructions for use
5. Update EU database registration if required

---

## Part 8 — Substantial Modification Assessment

Under **Article 25**, a substantial modification requires a new conformity assessment.

**Substantial modification triggers:**

| Change Type | Substantial Modification? | Action |
|-------------|--------------------------|--------|
| Significant change to purpose or intended use | Yes | New conformity assessment |
| Change affecting high-risk classification | Yes | New conformity assessment |
| Change to training data affecting performance significantly | Assess case-by-case | Review |
| Bug fix with no performance impact | No | Update documentation |
| UI change with no functional impact | No | Update documentation |
| Minor parameter tuning within spec | No | Update documentation |

---

## Part 9 — PMM Reporting

### 9.1 Internal Reporting

| Report | Audience | Frequency | Content |
|--------|---------|-----------|---------|
| Performance dashboard | AI Oversight team | Weekly | Metrics, alerts, anomalies |
| Monthly PMM summary | AI Governance Lead | Monthly | Trends, incidents, actions |
| Annual PMM review | Senior Leadership | Annually | Full review, risks, improvements |

### 9.2 External Reporting

| Report | Recipient | Trigger | Content |
|--------|----------|---------|---------|
| Serious incident notification | National MSA | Within 72 hours of incident | Per Article 73 template |
| Follow-up investigation report | National MSA | Post-investigation | Root cause, corrective actions |
| Updated technical documentation | Available to MSA on request | After significant updates | |

---

## Part 10 — PMM Plan Review and Update Log

| Version | Date | Changes Made | Approved By |
|---------|------|-------------|------------|
| v1.0 | | Initial plan | |
| | | | |

---

*Part of the [EU AI Act Compliance Toolkit](README.md)*
