# 07 — Human Oversight Framework

**EU AI Act Reference:** Article 14 | Recitals 84–86  
**Applies to:** Providers (design obligations) and Deployers (operational obligations) of High-Risk AI Systems  
**Last Updated:** April 2026

---

## Purpose

Article 14 requires that high-risk AI systems are designed and developed to be effectively overseen by natural persons during the period of use. This framework provides the structure for designing, implementing, and operating human oversight controls.

---

## Part 1 — Oversight Design Principles (for Providers)

Providers must ensure systems are designed so that oversight persons can:

| Principle | Article 14 Reference | Implementation Approach |
|-----------|---------------------|------------------------|
| Fully understand system capabilities and limitations | Art. 14(4)(a) | Interpretability tools, model cards, documentation |
| Monitor system operation for anomalies | Art. 14(4)(b) | Real-time dashboards, alerting, audit logs |
| Remain aware of automation bias risk | Art. 14(4)(c) | Training, UI design, confidence calibration |
| Correctly interpret outputs | Art. 14(4)(c) | Explanations, confidence scores, uncertainty flags |
| Decide not to use / override / disregard output | Art. 14(4)(d) | Override controls, human-in-the-loop workflows |
| Intervene or interrupt system operation | Art. 14(4)(e) | Emergency stop, suspend function, escalation path |

---

## Part 2 — Oversight Persons — Roles and Responsibilities

### 2.1 Oversight Role Definitions

| Role | Description | Competencies Required |
|------|-------------|----------------------|
| **System Operator** | Day-to-day user who operates the AI system | Domain expertise, AI literacy, system training |
| **AI Oversight Officer** | Designated person responsible for oversight monitoring | GRC knowledge, technical understanding, audit skills |
| **Escalation Authority** | Person with power to override, suspend, or stop the system | Decision-making authority, accountability |
| **Technical Reviewer** | Monitors system performance metrics and anomalies | Data science, ML monitoring skills |

### 2.2 Oversight Person Competency Requirements (Article 14(3))

Deployers must assign oversight tasks only to persons who have:

- ☐ Necessary competence, training, and authority
- ☐ Necessary resources and support
- ☐ Understanding of the AI system (capabilities and limitations)
- ☐ Ability to identify signs of unexpected behaviour
- ☐ Authority to intervene when required

### 2.3 Oversight Person Training Log

| Name | Role | Training Completed | Date | Refresher Due |
|------|------|-------------------|------|--------------|
| | | | | |

---

## Part 3 — Oversight Controls

### 3.1 Pre-Deployment Oversight Controls

| Control | Implementation | Status |
|---------|---------------|--------|
| Human review gate before system goes live | | ☐ |
| Oversight person assignment documented | | ☐ |
| Override and stop mechanisms tested | | ☐ |
| Escalation procedure communicated | | ☐ |
| Monitoring dashboards configured | | ☐ |

### 3.2 Operational Oversight Controls

| Control | Frequency | Method | Owner |
|---------|-----------|--------|-------|
| Review of system outputs / decisions | | | |
| Monitor accuracy and performance metrics | | | |
| Spot-check of flagged / high-risk decisions | | | |
| Review of anomaly / alert notifications | | | |
| Log review | | | |
| Bias monitoring | | | |

### 3.3 Override and Intervention Controls

| Control | Method | Trigger Conditions | Owner |
|---------|--------|-------------------|-------|
| Output override (individual decision) | | | |
| System pause (temporary suspension) | | | |
| Emergency stop (full shutdown) | | | |
| Rollback to previous version | | | |

---

## Part 4 — Automation Bias Mitigation

Article 14(4)(c) requires that oversight persons are aware of the risk of automation bias — the tendency to over-rely on automated system outputs.

### Mitigation Measures

| Measure | Implemented? | Notes |
|---------|-------------|-------|
| Training on automation bias risks | ☐ Yes / ☐ No | |
| UI design that requires active human confirmation for critical decisions | ☐ Yes / ☐ No | |
| Random sampling of outputs for independent human review | ☐ Yes / ☐ No | |
| Confidence scores / uncertainty flags shown to operators | ☐ Yes / ☐ No | |
| Mandatory human review for decisions above defined risk threshold | ☐ Yes / ☐ No | |
| Periodic audits of human override rates | ☐ Yes / ☐ No | |

---

## Part 5 — Human Oversight in Decision Workflows

### 5.1 Decision Workflow Classification

| Decision Type | AI Role | Human Role | Human Authority |
|--------------|---------|-----------|----------------|
| Low-stakes routine decision | Automated | Monitoring only | Can override if flagged |
| Medium-stakes decision | AI recommends | Human approves | Must actively confirm |
| High-stakes decision | AI inputs | Human decides | AI output is advisory only |
| Critical / irreversible decision | AI prohibited / advisory | Human decides | Full accountability |

### 5.2 Current System Decision Workflow

```
[System Name] Decision Flow:

1. Input received → AI system processes
2. AI generates: [output type] with confidence score
3. Output routed to: [oversight person / team]
4. Human review: [mandatory / sampled / alert-triggered]
5. Human action: [approve / override / escalate]
6. Decision recorded in audit log
7. Outcome fed back to monitoring system
```

---

## Part 6 — Oversight Monitoring and Reporting

### 6.1 Key Oversight Metrics

| Metric | Target | Actual | Review Frequency |
|--------|--------|--------|-----------------|
| % of decisions reviewed by a human | | | |
| % of AI outputs overridden by humans | | | |
| Average time to human review | | | |
| % of alerts actioned within SLA | | | |
| Oversight person response rate | | | |

### 6.2 Oversight Incident Log

| Date | Incident Type | System | Description | Action Taken | Resolved By |
|------|--------------|--------|-------------|-------------|------------|
| | | | | | |

---

## Part 7 — Oversight Framework Review

| Review Date | Trigger | Outcome | Next Review |
|------------|---------|---------|------------|
| | Annual / System change / Incident | | |

---

*Part of the [EU AI Act Compliance Toolkit](README.md)*
