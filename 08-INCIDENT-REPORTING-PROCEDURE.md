# 08: Incident Reporting Procedure

**EU AI Act Reference:** Article 73 (Providers); Article 26(5) (Deployers)
**Applies to:** Providers and Deployers of High-Risk AI Systems
**Regulatory Recipient:** National Market Surveillance Authority (MSA) / EU AI Office (for GPAI)
**Last Updated:** April 2026

---

## Purpose

Article 73 requires providers of high-risk AI systems to report **serious incidents** to the market surveillance authority of the EU member state where the incident occurred. This procedure defines what constitutes a serious incident, the reporting timeline, the process, and the documentation requirements.

> **Important, reporting deadlines (read first):** The EU AI Act does **not** use a single "72-hour" deadline. Article 73 sets **tiered** deadlines measured from when you become aware of the incident: a general maximum of **15 days**; **2 days** for a widespread infringement or a serious incident involving disruption of critical infrastructure (Art. 3(49)(b)); and **10 days** where a person has died. In all cases the report must be made **immediately** once a causal link (or its reasonable likelihood) is established. The 72-hour figure belongs to the **GDPR** personal-data-breach regime (Art. 33 GDPR), which is separate, see Doc 18.

---

## Part 1: What is a Serious Incident?

Under **Article 3(49)**, a serious incident means an incident or malfunction of an AI system that directly or indirectly leads to any of the following:

| Category | Reference | Examples |
|----------|-----------|---------|
| **Death of a person, or serious harm to health** | Art. 3(49)(a) | AI diagnostic error leading to fatal treatment; autonomous system collision causing injury |
| **Serious and irreversible disruption of critical infrastructure** | Art. 3(49)(b) | AI failure disrupting management/operation of critical infrastructure |
| **Infringement of fundamental rights obligations under Union law** | Art. 3(49)(c) | Discriminatory outcome causing legally protected harm |
| **Serious harm to property or the environment** | Art. 3(49)(d) | Infrastructure or environmental damage triggered by an AI decision |

**Note:** Near-misses that *could* have caused serious harm should be logged internally and assessed for a reporting obligation.

---

## Part 2: Reporting Obligations and Deadlines

### 2.1 Provider Reporting Deadlines (Article 73(2)-(4))

The report must always be made **immediately** after the provider establishes (or reasonably suspects) a causal link between the AI system and the serious incident, and **in any event no later than** the outer limit below:

| Scenario | Outer deadline | Reference |
|----------|---------------|-----------|
| General rule (any serious incident) | **15 days** after becoming aware | Art. 73(2) |
| Widespread infringement, or serious incident disrupting critical infrastructure (Art. 3(49)(b)) | **2 days** after becoming aware | Art. 73(3) |
| Death of a person | **10 days** after becoming aware | Art. 73(4) |
| Initial incomplete report permitted, followed by a complete report | Where needed for timely reporting | Art. 73(5) |

> The reporting period must take account of the **severity** of the incident (Art. 73(2), second subparagraph).

### 2.2 Provider: Other Obligations (Article 73)

| Obligation | Timeline | Recipient |
|-----------|---------|-----------|
| Provide follow-up / complete report after an initial incomplete report | As soon as reasonably practicable | National MSA |
| Conduct investigation and risk assessment of the incident | Without undue delay | Provider (records to MSA) |
| Notify EU AI Office (GPAI models with systemic risk, serious incidents) | Without undue delay | EU AI Office (Art. 55(1)(c)) |

### 2.3 Deployer Obligations (Article 26(5) and Article 73(1))

| Obligation | Timeline | Recipient |
|-----------|---------|-----------|
| Inform provider of serious incident or malfunction | Immediately upon becoming aware | Provider |
| Where the provider cannot be reached, the deployer assumes the provider's Art. 73 reporting deadlines | Per Art. 73(2)-(4) tiers above | National MSA |
| Cooperate with investigation | As requested | Provider / MSA |

> **Note:** Where the same incident is also a personal-data breach, GDPR Art. 33 imposes a **separate 72-hour** notification to the Data Protection Authority. File the AI Act report (per the tiers above) and the GDPR report separately but in a coordinated way. See Doc 18, Part 8.2.

---

## Part 3: Incident Classification

### 3.1 Severity Classification

| Level | Classification | Criteria | Reporting Required |
|-------|---------------|----------|--------------------|
| P1 | **Critical, Serious Incident** | Death, serious harm to health, critical-infrastructure disruption, fundamental-rights infringement, or serious property/environmental harm | ✅ Yes, within the applicable Art. 73 tier (2 / 10 / 15 days) |
| P2 | **High, Potential Serious Incident** | Near-miss; significant malfunction with potential for serious harm | ✅ Assess for reporting |
| P3 | **Medium, Significant Malfunction** | System performs below specification; no serious harm | ❌ Internal log only |
| P4 | **Low, Minor Anomaly** | Deviation within acceptable parameters | ❌ Monitoring only |

---

## Part 4: Incident Response Procedure

### Phase 1: Detection and Initial Assessment (0-2 hours)

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
- Apply severity classification (P1-P4)
- If P1 or P2: escalate to Incident Lead immediately
│
▼
Step 3: Notify internal stakeholders
- AI Governance Lead
- Legal / DPO
- Executive / Senior Responsible Officer (if P1)
```

### Phase 2: Triage and Investigation

| Step | Action | Owner | Deadline |
|------|--------|-------|---------|
| 4 | Establish incident response team | AI Governance Lead | 2 hours |
| 5 | Preserve all relevant evidence, logs, system states | Technical Lead | 2 hours |
| 6 | Conduct preliminary root cause analysis | Technical Lead | 24 hours |
| 7 | Identify affected persons / scope of harm | Compliance | 24 hours |
| 8 | Determine which Art. 73 deadline tier applies (2 / 10 / 15 days) and start the clock | Legal | Immediately on awareness |

### Phase 3: Regulatory Notification (within the applicable Art. 73 tier)

| Step | Action | Owner |
|------|--------|-------|
| 9 | Draft initial regulatory notification (see template below), submit even if incomplete (Art. 73(5)) | Compliance / Legal |
| 10 | Approve notification | Senior Responsible Officer |
| 11 | Submit to National MSA of affected jurisdiction within the applicable tier (2 / 10 / 15 days) | Compliance |
| 12 | If also a personal-data breach: notify the DPA within 72 hours (GDPR Art. 33) and affected individuals where required (Art. 34) | DPO |
| 13 | Document submission and obtain reference number | Compliance |

### Phase 4: Full Investigation and Follow-Up Report

| Step | Action | Owner |
|------|--------|-------|
| 14 | Conduct full root cause investigation | Technical Lead |
| 15 | Document findings, timeline, and impact | Compliance |
| 16 | Identify systemic issues and corrective actions | AI Governance |
| 17 | Submit complete / follow-up report to MSA (Art. 73(5)) | Compliance |
| 18 | Implement corrective actions | Technical / Business |
| 19 | Verify effectiveness of corrective actions | AI Oversight Officer |
| 20 | Close incident with lessons learned documented | AI Governance Lead |

---

## Part 5: Initial Regulatory Notification Template

**To:** [National Market Surveillance Authority, name and address]
**From:** [Provider name, address, EU Authorised Representative if applicable]
**Date:** [Date of notification]
**Subject:** Serious Incident Notification, [AI System Name], Article 73 EU AI Act

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
| Applicable Art. 73 deadline tier (2 / 10 / 15 days) | |
| Location (Member State) where incident occurred | |
| Brief description of incident | |
| Preliminary harm assessment | |
| Number of persons affected (estimated) | |

**3. Immediate Actions Taken**

> *[Describe what immediate steps have been taken to contain the incident and prevent further harm]*

**4. Investigation Status**

> *[Describe the current state of the investigation and expected timeline for the complete report]*

**5. Contact Person**

| Field | Entry |
|-------|-------|
| Name | |
| Role | |
| Email | |
| Phone | |

---

## Part 6: Incident Register

| Incident ID | Date | System | Severity | Description | Art. 73 Tier | MSA Notified | Notification Date | Status | Lessons Learned |
|-------------|------|--------|---------|-------------|--------------|-------------|------------------|--------|----------------|
| INC-001 | | | | | | ☐ Yes / ☐ No / ☐ N/A | | | |

---

## Part 7: Contacts

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
