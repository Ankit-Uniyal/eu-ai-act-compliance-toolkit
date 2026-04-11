# 08 — Incident Reporting Procedure

**EU AI Act Reference:** Article 73 (Providers); Article 26(5) (Deployers)  
**Applies to:** Providers and Deployers of High-Risk AI Systems  
**Regulatory Recipient:** National Market Surveillance Authority (MSA) / EU AI Office (for GPAI)  
**Last Updated:** April 2026

---

## Purpose

Article 73 requires providers of high-risk AI systems to report **serious incidents** to the market surveillance authority of the EU member state where the incident occurred. This procedure defines what constitutes a serious incident, the reporting timeline, the process, and the documentation requirements.

---

## Part 1 — What is a Serious Incident?

Under **Article 3(49)**, a serious incident means any incident or malfunction of a high-risk AI system that, directly or indirectly, leads to:

| Category | Examples |
|----------|---------|
| **Death of a person** | AI diagnostic error leading to fatal treatment; autonomous system fatal collision |
| **Serious harm to health or safety** | Physical injury; psychological harm requiring medical attention |
| **Serious and irreversible harm** | Damage to property, environment; long-term financial harm |
| **Breach of fundamental rights obligations** | Discriminatory outcome causing legally protected harm |
| **Serious damage to property or environment** | Infrastructure damage triggered by AI decision |

**Note:** Near-misses that *could* have caused serious harm should be logged internally and assessed for reporting obligation.

---

## Part 2 — Reporting Obligations

### 2.1 Provider Obligations (Article 73)

| Obligation | Timeline | Recipient |
|-----------|---------|-----------|
| Report serious incident | Without undue delay (within **72 hours** of becoming aware) | National MSA where incident occurred |
| Provide follow-up report with full investigation | As soon as reasonably practicable | National MSA |
| Notify EU AI Office (GPAI models with systemic risk) | Without undue delay | EU AI Office |

### 2.2 Deployer Obligations (Article 26(5))

| Obligation | Timeline | Recipient |
|-----------|---------|-----------|
| Inform provider of serious incident or malfunction | Immediately upon becoming aware | Provider |
| Report to national MSA (if provider not established in EU) | Without undue delay | National MSA |
| Cooperate with investigation | As requested | Provider / MSA |

---

## Part 3 — Incident Classification

### 3.1 Severity Classification

| Level | Classification | Criteria | Reporting Required |
|-------|---------------|----------|--------------------|
| P1 | **Critical — Serious Incident** | Death, serious harm, breach of fundamental rights | ✅ Yes — within 72 hours |
| P2 | **High — Potential Serious Incident** | Near-miss; significant malfunction with potential for serious harm | ✅ Assess for reporting |
| P3 | **Medium — Significant Malfunction** | System performs below specification; no serious harm | ❌ Internal log only |
| P4 | **Low — Minor Anomaly** | Deviation within acceptable parameters | ❌ Monitoring only |

---

## Part 4 — Incident Response Procedure

### Phase 1: Detection and Initial Assessment (0–2 hours)

```
INCIDENT DETECTED (by user, operator, monitoring system, or third party)
  │
  ▼
Step 1: Immediate containment
  - Suspend AI system if ongoing harm is occurring
  - Preserve logs and evidence (do NOT overwrite)
  - Notify AI Oversight Officer immediately
  │
  ▼
Step 2: Initial severity assessment
  - Apply severity classification (P1–P4)
  - If P1 or P2: escalate to Incident Lead immediately
  │
  ▼
Step 3: Notify internal stakeholders
  - AI Governance Lead
  - Legal / DPO
  - Executive / Senior Responsible Officer (if P1)
```

### Phase 2: Triage and Investigation (2–48 hours)

| Step | Action | Owner | Deadline |
|------|--------|-------|---------|
| 4 | Establish incident response team | AI Governance Lead | 2 hours |
| 5 | Preserve all relevant evidence, logs, system states | Technical Lead | 2 hours |
| 6 | Conduct preliminary root cause analysis | Technical Lead | 24 hours |
| 7 | Identify affected persons / scope of harm | Compliance | 24 hours |
| 8 | Assess reporting obligation (P1: is it a serious incident per Article 3(49)?) | Legal | 24 hours |

### Phase 3: Regulatory Notification (if P1 Serious Incident — within 72 hours)

| Step | Action | Owner |
|------|--------|-------|
| 9 | Draft initial regulatory notification (see template below) | Compliance / Legal |
| 10 | Approve notification | Senior Responsible Officer |
| 11 | Submit to National MSA of affected jurisdiction | Compliance |
| 12 | Notify affected individuals if required by GDPR (72-hour rule) | DPO |
| 13 | Document submission and obtain reference number | Compliance |

### Phase 4: Full Investigation and Follow-Up Report

| Step | Action | Owner |
|------|--------|-------|
| 14 | Conduct full root cause investigation | Technical Lead |
| 15 | Document findings, timeline, and impact | Compliance |
| 16 | Identify systemic issues and corrective actions | AI Governance |
| 17 | Submit follow-up report to MSA | Compliance |
| 18 | Implement corrective actions | Technical / Business |
| 19 | Verify effectiveness of corrective actions | AI Oversight Officer |
| 20 | Close incident with lessons learned documented | AI Governance Lead |

---

## Part 5 — Initial Regulatory Notification Template

**To:** [National Market Surveillance Authority — name and address]  
**From:** [Provider name, address, EU Authorised Representative if applicable]  
**Date:** [Date of notification]  
**Subject:** Serious Incident Notification — [AI System Name] — Article 73 EU AI Act

---

**1. AI System Details**

| Field | Entry |
|-------|-------|
| System name | |
| System version | |
| Annex III classification | |
| EU database registration number | |

**2. Incident Summary**

| Field | Entry |
|-------|-------|
| Date/time of incident | |
| Date/time provider became aware | |
| Location (Member State) where incident occurred | |
| Brief description of incident | |
| Preliminary harm assessment | |
| Number of persons affected (estimated) | |

**3. Immediate Actions Taken**

> *[Describe what immediate steps have been taken to contain the incident and prevent further harm]*

**4. Investigation Status**

> *[Describe the current state of the investigation and expected timeline for full report]*

**5. Contact Person**

| Field | Entry |
|-------|-------|
| Name | |
| Role | |
| Email | |
| Phone | |

---

## Part 6 — Incident Register

| Incident ID | Date | System | Severity | Description | MSA Notified | Notification Date | Status | Lessons Learned |
|-------------|------|--------|---------|-------------|-------------|------------------|--------|----------------|
| INC-001 | | | | | ☐ Yes / ☐ No / ☐ N/A | | | |

---

## Part 7 — Contacts

| Role | Name | Contact | Availability |
|------|------|---------|-------------|
| AI Oversight Officer | | | |
| Legal / Compliance Lead | | | |
| Data Protection Officer | | | |
| Technical Lead | | | |
| Senior Responsible Officer | | | |
| National MSA Contact | | | 24/7 |

**National MSA Directory:** https://single-market-economy.ec.europa.eu/single-market/goods/building-blocks/market-surveillance_en

---

*Part of the [EU AI Act Compliance Toolkit](README.md)*
