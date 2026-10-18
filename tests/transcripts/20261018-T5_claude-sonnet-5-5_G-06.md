# G-06 Ending Block proportionality

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261018-T5
**Prompt proper SHA-256:** 8b49e8c79dc7a70bff5fa8b8875744c9ae6983d4d17f4e8f98688253f2dffb75
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 7422  **Output tokens:** 2193
**Truncated:** no

## User message

Routine question: what fields should a basic contract intake form capture?

## Assistant response

**Mode: POLICY / PROCESS DESIGN** (lightweight). This is routine, so I'm proceeding on stated assumptions rather than asking questions first.

## Core Fields for a Basic Contract Intake Form

**1. Requester and ownership**
- Requester name, department and contact
- Business owner (if different) and budget owner or cost center
- Date submitted and requested completion date
- Reason for the deadline (a real driver, not "ASAP")

**2. Counterparty**
- Full legal name, entity type, jurisdiction of organization and address
- Existing relationship, and any prior or current agreements with us
- Whether the counterparty is an affiliate, related party or government entity
- Whether onboarding or third-party due diligence is complete

**3. Contract basics**
- Contract type (NDA, MSA, SOW, purchase, sale, license, lease, etc.)
- New, renewal, amendment or termination
- Whose paper: ours, theirs or negotiated
- Plain-language description of the deal and business purpose
- Reference to any parent agreement

**4. Commercial terms**
- Total and annual value, and currency
- Term, renewal mechanics and termination rights
- Payment terms and pricing model
- Minimum commitments, exclusivity or other unusual terms

**5. Risk-trigger questions (yes/no, each routing to a reviewer)**
- Personal or sensitive data involved?
- Cross-border data transfer or performance?
- Will IP be created, assigned or licensed? Contractor-developed work?
- Software, SaaS, AI or open-source components?
- Government customer or official involved? Agents or intermediaries?
- Sanctions, export-control or regulated-industry exposure?
- Subcontractors or subprocessors?
- Non-standard liability, indemnity or insurance terms?
- Exclusivity, non-compete, MFN or publicity terms?
- On-site work or safety implications?

**6. Approvals and authority**
- Required approvals based on value or risk (finance, security, privacy, procurement)
- Intended signatory and confirmation of signing authority
- Whether the deal falls under a delegation-of-authority threshold

**7. Attachments**
- Draft contract, term sheet or proposal
- Counterparty standard terms
- RFP or procurement documents
- Security questionnaire or privacy assessment
- Relevant correspondence

**8. Post-signature handoff**
- Contract owner for ongoing management
- Key dates: start, renewal-notice deadline, termination-notice deadline, deliverables
- Repository or system of record

**9. Administrative (legal use)**
- Matter or ticket ID, assigned reviewer, status, risk tier and date completed

## Design Tips
- **Keep mandatory fields lean.** Long forms get bypassed. Use dropdowns and conditional questions so the risk-trigger section expands only when needed.
- **Make triggers route automatically** to privacy, security, procurement or finance rather than relying on the requester to decide who should look.
- **Privilege:** Free-text answers may not be privileged. Consider an instruction to keep facts concise and a clear way to mark requests for legal advice. Whether and how privilege attaches is jurisdiction-specific.
- **Capture renewal and notice dates at intake.** Missed auto-renewals are a common avoidable loss.

I can turn this into a formatted form, a routing matrix or a RACI if useful. If so, tell me your industry, jurisdictions and existing contract management tool.

---
- **Assumptions:** General-purpose commercial contracts for a mid-sized corporate legal function; no industry-specific regulatory requirements; no existing form or CLM system constraints.
- **Unknown/Insufficient data:** Your industry, jurisdictions, approval matrix, delegation-of-authority thresholds, existing templates and systems.
- **Needs current legal verification:** No (operational design guidance only). Jurisdiction-specific privilege and data-handling questions would require review.

---
Score this transcript against tests/scenarios.md and record it in tests/scorecard.md.
Final Liability rests with the Human.
