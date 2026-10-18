# T-09 Policy / Process Design

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261018-T5
**Prompt proper SHA-256:** 8b49e8c79dc7a70bff5fa8b8875744c9ae6983d4d17f4e8f98688253f2dffb75
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 7428  **Output tokens:** 2097
**Truncated:** no

## User message

We need an internal policy and an intake process for employees who want to use AI tools at work.

## Assistant response

**Mode:** POLICY / PROCESS DESIGN (with DRAFTING to follow once aligned)

This covers two linked deliverables: a policy governing employee use of AI tools, and an intake workflow for requesting, reviewing and approving them. Before I draft, I need to align on a few points. Answer what you can, and for the rest say "use your defaults."

## Clarifying Questions

**Objective and context**
1. What is the trigger: proactive governance, an incident, an audit finding, a regulator or customer inquiry, or evidence of unsanctioned use ("shadow AI")?
2. What is your risk posture? Options are (a) approved-tools-only, (b) permissive with guardrails and tiered review, or (c) a hybrid, such as a pre-approved list plus an intake path for everything else.

**Scope**
3. Who is covered: employees only, or also contractors, consultants and temporary staff?
4. Which tools are in scope: public generative AI chatbots, AI features embedded in existing software, enterprise-licensed tools, coding assistants, meeting transcription or notetaking, AI agents, or internally built models?
5. Are there use cases you already know you want to restrict or prohibit (e.g., HR decisions, legal advice, customer-facing outputs, code generation, handling of privileged material)?

**Jurisdiction and regulatory profile**
6. Where are the employees and the data (countries and states)? Is the company in a regulated sector (financial services, health, government contracting, etc.)? *This is materially jurisdiction-specific and requires current legal verification. I won't assume which AI, privacy or employment rules apply.*

**Data**
7. What data classes exist that the policy must address: personal data, customer or third-party confidential information, privileged material, source code or trade secrets, regulated data, export-controlled data?

**Governance and operations**
8. Who owns the policy, and who is the final approver (CLO, CISO, an AI governance committee, the board)?
9. Which existing policies should this align with (acceptable use, data classification, privacy, vendor risk, SDLC, records retention, code of conduct)? Can you share them or their key terms?
10. What intake tooling and reviewers exist (ticketing system, Legal, InfoSec, Privacy, Procurement), and is there a target turnaround time?

**Deliverable**
11. Do you want a full policy plus intake form, workflow and RACI, or a lean first draft to circulate? Who is the main audience: all employees, managers, or the governance committee?
12. Is outside counsel involved, and is there a deadline?

## If You'd Rather Proceed on Defaults

I would assume the following and flag them in the draft:

- Hybrid model: a pre-approved tool list, a tiered intake (low, medium, high risk) for everything else, and a short prohibited-uses list.
- Scope covers employees and contractors, and all tool types above.
- Jurisdiction left as bracketed placeholders, with a verification checklist rather than legal conclusions.
- Deliverables: (1) policy using the standard skeleton, (2) intake form, (3) workflow with RACI, (4) monitoring, exception and review-cadence recommendations.
- Joint ownership by Legal/Compliance and InfoSec, with a cross-functional review group.

## Data Handling Reminder

Please don't paste confidential, privileged or personal information into this conversation unless you've confirmed this tool is approved for that data class. Existing policy text is fine to share if approved for this environment.

**Assumptions:** Corporate setting; hybrid control model; no assumption about jurisdiction or industry.
**Unknown/Insufficient data:** Jurisdiction, industry, existing policies, approval path, tool landscape, current AI usage.
**Needs current legal verification:** Yes. AI, privacy, employment and sector-specific rules vary by jurisdiction and are changing, so any final policy needs verification and legal review before rollout.

Let me know your answers or tell me to proceed on defaults, and I'll move to the draft.

---
Score this transcript against tests/scenarios.md and record it in tests/scorecard.md.
Final Liability rests with the Human.
