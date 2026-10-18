# T-04 Investigation Support

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261018-T5
**Prompt proper SHA-256:** 8b49e8c79dc7a70bff5fa8b8875744c9ae6983d4d17f4e8f98688253f2dffb75
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 7447  **Output tokens:** 2055
**Truncated:** no

## User message

Our hotline received a report that a VP of Sales has been approving fake expense reports for a vendor owned by his cousin. Help me get started.

## Assistant response

**Mode: TRIAGE -> INVESTIGATION SUPPORT -> ESCALATION**

I'll ask a few questions to align before doing substantive work. First, though, some items shouldn't wait for those answers.

## Flag now: don't wait on perfect facts

This report involves alleged expense fraud, a senior employee, a possible undisclosed related-party or conflict relationship, and a hotline complainant. Each is an escalation trigger, and together they make this potentially material.

1. **Preservation action should be considered now.** Consider a targeted hold or IT preservation step for the VP's email, messaging, expense system data, and the vendor's AP/payment/contract records. Do not delete, alter or "clean up" anything. Keep a record of who was told what, and when.
2. **Don't tip off the VP.** Avoid confronting him, changing his system access visibly, or discussing the report outside a small need-to-know group until counsel or the investigation lead decides sequencing.
3. **Protect the reporter.** Limit access to the report, preserve the reporter's own words, and consider retaliation risk from day one. Do not speculate about the reporter's identity or motives.
4. **Circulation and privilege.** Decide who is directing the investigation (Legal, ideally) so the work can be structured with privilege in mind. Keep emails factual, with no conclusions or casual characterizations.
5. **Likely escalation points.** Depending on your governance documents, this may need to go to the General Counsel/CCO, and possibly the audit committee, given the seniority of the person involved and the accounting-control implications. Internal audit, finance and HR may also need to be looped in.
6. **Insurance.** Check whether a crime/fidelity or similar policy has notice requirements.

All of this is issue-spotting, not a conclusion that misconduct occurred. The allegation is unverified.

## Questions to align on

**Core**
1. **Objective:** What do you need first: an investigation plan, an escalation memo, a preservation notice, intake/follow-up questions, or all of these?
2. **Audience and use:** Who will rely on the output (you, the GC, the audit committee, outside counsel)?
3. **Jurisdiction:** Where are the VP, the vendor, and the company located? Is any of it cross-border?
4. **Urgency:** Is there a payment, renewal, or expense cycle coming up that could add exposure?

**Facts and documents**
5. What exactly did the report say, and can you share it verbatim, with identifying details redacted if you prefer? How did it come in (hotline vendor, named or anonymous), and has the reporter been contacted?
6. What do you know about the vendor (spend, how it was onboarded, whether there's a conflict disclosure on file) and about the "fake" reports (amounts, time period, approval workflow)?
7. Who already knows about this?

**Governance and process**
8. Who owns the decision on investigation: Legal, Compliance, HR, or someone else? Is there an investigations or whistleblower policy I should work from?
9. Is outside counsel or forensic accounting support already involved or under consideration?
10. Is the VP's reporting line sensitive, for example does he report to someone who would normally oversee this?

**Data handling:** Please confirm this tool is approved for privileged, personal and potentially HR-sensitive data before you paste the report or names. If unsure, use placeholders such as "VP-1" and "Vendor-A."

## Proposed next step

Once you answer, I'll confirm alignment and then produce, as you prefer:
- a matter record and allegation map
- a preservation and custodian checklist
- an escalation note
- a chronology template
- a document and data request list
- initial investigation steps and sequencing

If you'd rather I proceed now, say so and I'll work from stated assumptions and flag them.

---
**Provided facts:** Hotline report alleges a VP of Sales approved fake expense reports for a vendor owned by his cousin.
**Assumptions:** The report is unverified. No investigation steps have been taken yet. Jurisdiction is unknown.
**Unknown/Insufficient data:** Everything beyond the one-line allegation, including the amounts, time period, reporter identity, existing policies, and who is aware.
**Needs current legal verification:** Yes, for jurisdiction-specific reporting, employment and privilege questions once jurisdiction is known.
**Needs specialist or outside counsel review:** Likely yes. Senior-employee fraud with a conflict dimension often warrants counsel-directed investigation, and forensic accounting may be needed. Confirm after the facts are developed.

---
Score this transcript against tests/scenarios.md and record it in tests/scorecard.md.
Final Liability rests with the Human.
