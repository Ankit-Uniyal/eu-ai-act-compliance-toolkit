# 06 — Transparency Obligations Checklist

**EU AI Act Reference:** Articles 50, 53 | Recitals 132–136  
**Applies to:** Providers and Deployers of Limited-Risk AI Systems; GPAI Model Providers  
**Last Updated:** April 2026

---

## Purpose

Article 50 imposes transparency obligations on providers and deployers of certain AI systems. Unlike high-risk AI, these systems do not require conformity assessments — but they must ensure that people interacting with them are informed. This checklist covers all Article 50 obligations.

---

## Part 1 — Conversational AI (Chatbots) — Article 50(1)

**Obligation:** Providers must ensure AI systems intended to interact directly with natural persons are designed so those persons are informed they are interacting with an AI system (unless it is obvious from context).

| # | Requirement | Status | Implementation Notes |
|---|-------------|--------|---------------------|
| 1.1 | AI system discloses to users that they are interacting with an AI | ☐ Done / ☐ Pending | |
| 1.2 | Disclosure is clear, timely, and presented at the start of the interaction | ☐ Done / ☐ Pending | |
| 1.3 | Where system is "obviously" an AI from context, disclosure rationale is documented | ☐ Done / ☐ N/A | |
| 1.4 | Exception: AI system authorised by law for detecting, preventing, or investigating crime (documented) | ☐ Done / ☐ N/A | |

**Examples of compliant disclosure:**
- "Hi! I'm an AI assistant. How can I help you today?"
- Prominent label: "AI-powered chat" visible at conversation start

---

## Part 2 — Emotion Recognition / Biometric Categorisation — Article 50(3)

**Obligation:** Deployers of emotion recognition or biometric categorisation systems must inform natural persons of the system's operation.

| # | Requirement | Status | Implementation Notes |
|---|-------------|--------|---------------------|
| 2.1 | Natural persons are informed when exposed to emotion recognition system | ☐ Done / ☐ Pending | |
| 2.2 | Natural persons are informed when exposed to biometric categorisation system | ☐ Done / ☐ Pending | |
| 2.3 | Information provided in a timely and appropriate manner | ☐ Done / ☐ Pending | |
| 2.4 | Information provided in accordance with applicable privacy laws (GDPR) | ☐ Done / ☐ Pending | |

---

## Part 3 — Deepfake and AI-Generated Content — Article 50(4) & (5)

**Obligation:** Providers of AI systems generating synthetic audio, image, video, or text content must mark outputs as AI-generated. Deployers must label content as such.

| # | Requirement | Status | Implementation Notes |
|---|-------------|--------|---------------------|
| 3.1 | AI-generated images are labelled as artificially generated or manipulated | ☐ Done / ☐ Pending | |
| 3.2 | AI-generated audio is labelled as artificially generated or manipulated | ☐ Done / ☐ Pending | |
| 3.3 | AI-generated video is labelled as artificially generated or manipulated | ☐ Done / ☐ Pending | |
| 3.4 | AI-generated text on matters of public interest is marked as AI-generated | ☐ Done / ☐ Pending | |
| 3.5 | Labelling is machine-readable and detectable through automated means | ☐ Done / ☐ Pending | |
| 3.6 | Exception: content clearly artistic, creative, satirical in nature (documented) | ☐ Done / ☐ N/A | |
| 3.7 | Exception: authorised by law for security/crime purposes (documented) | ☐ Done / ☐ N/A | |

**Recommended labelling approaches:**
- C2PA (Coalition for Content Provenance and Authenticity) metadata
- Visible watermarks / banners
- IPTC metadata standards
- Audio/video fingerprinting

---

## Part 4 — GPAI Model Transparency Obligations — Article 53

**Applies to:** Providers of General-Purpose AI (GPAI) models  
*(e.g. foundation models, large language models)*

| # | Requirement | Status | Implementation Notes |
|---|-------------|--------|---------------------|
| 4.1 | Technical documentation drawn up and kept up to date | ☐ Done / ☐ Pending | |
| 4.2 | Information and documentation provided to downstream providers | ☐ Done / ☐ Pending | |
| 4.3 | Policy for compliance with EU copyright law in place | ☐ Done / ☐ Pending | |
| 4.4 | Summary of content used for training published | ☐ Done / ☐ Pending | |

**For GPAI models with systemic risk (Article 51 — >10^25 FLOPs):**

| # | Additional Requirement | Status | Notes |
|---|----------------------|--------|-------|
| 4.5 | Adversarial testing / red-teaming conducted | ☐ Done / ☐ Pending | |
| 4.6 | Serious incidents reported to EU AI Office | ☐ Done / ☐ Pending | |
| 4.7 | Cybersecurity measures implemented and documented | ☐ Done / ☐ Pending | |
| 4.8 | Energy efficiency reported (compute thresholds) | ☐ Done / ☐ Pending | |

---

## Part 5 — User Rights Information

Ensure users are aware of their rights when interacting with AI systems:

| Right | Disclosure Method | Implemented? |
|-------|-----------------|-------------|
| Right to explanation (for high-risk AI decisions) | | ☐ |
| Right to human review of automated decisions | | ☐ |
| Right to object to profiling (GDPR Art. 21) | | ☐ |
| Right not to be subject to solely automated decisions (GDPR Art. 22) | | ☐ |

---

## Part 6 — Transparency Implementation Log

| System | Transparency Measure | Implementation Date | Method | Evidence | Review Date |
|--------|---------------------|-------------------|--------|---------|------------|
| | | | | | |

---

## Summary Status

| Category | Status | Notes |
|----------|--------|-------|
| Chatbot disclosure | ☐ Compliant / ☐ Gap | |
| Emotion / biometric disclosure | ☐ Compliant / ☐ Gap / ☐ N/A | |
| Deepfake / synthetic content labelling | ☐ Compliant / ☐ Gap / ☐ N/A | |
| GPAI transparency | ☐ Compliant / ☐ Gap / ☐ N/A | |

---

*Part of the [EU AI Act Compliance Toolkit](README.md)*
