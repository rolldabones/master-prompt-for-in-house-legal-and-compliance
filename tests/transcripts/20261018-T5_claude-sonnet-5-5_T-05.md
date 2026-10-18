# T-05 Governance

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261018-T5
**Prompt proper SHA-256:** 8b49e8c79dc7a70bff5fa8b8875744c9ae6983d4d17f4e8f98688253f2dffb75
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 7447  **Output tokens:** 2333
**Truncated:** no

## User message

Our board chair wants the company to sign a services contract with a firm his brother owns. He says it's below the approval threshold. How should we handle it?

## Assistant response

**Mode:** TRIAGE -> GOVERNANCE -> ESCALATION

This is a potential related-party / interested-director transaction, which is an escalation trigger. Nothing here suggests wrongdoing, since these transactions can be legitimate when handled properly. The risk is in the process.

## Why the threshold may not settle this

The chair's point is that the contract is under the approval threshold. That answers only one question: whether the ordinary delegation-of-authority matrix requires board-level approval. It does not answer whether a conflict-of-interest or related-party review is required. Many companies' policies, and some legal and listing regimes, apply to family-member transactions regardless of dollar value or at much lower thresholds. **Unknown/Insufficient data** on which apply here, because I haven't seen your policies.

## Preliminary flags (not conclusions)

- **Hold execution:** Consider pausing signature until the conflict review is complete. Delay is cheap and a defective approval is not.
- **Route to the right people:** Bring in the General Counsel (or equivalent) and likely the audit committee chair or another disinterested director. The chair should not be the one deciding whether his own conflict requires review.
- **Recusal:** The chair should disclose the relationship in writing and stay out of vendor selection, negotiation, and approval, and out of directing management on this contract.
- **Process and record:** Look at how the vendor was selected, whether the terms are market-based, and whether a competitive process or independent benchmarking exists. Document the review and the decision-maker.
- **Aggregation and splitting:** Check whether this vendor has other contracts, renewals, or amendments that bring total value over a threshold. Structuring below a threshold to avoid review is itself a red flag.
- **Pressure:** If the chair is pressing management directly, record that factually and neutrally, and make sure whoever reviews it is independent of him.
- **Possible legal overlays:** These include director fiduciary duties, interested-director statutes, and, if you are public, SEC disclosure and exchange rules on related-person transactions and independence. All are **Jurisdiction-specific** and **Require current legal verification**.
- **Privilege:** Keep circulation need-to-know and keep legal analysis separate from business discussion.

## Questions before I go further

1. **Entity and jurisdiction:** Is the company public, private, or nonprofit, and where is it incorporated and operating?
2. **Governing documents:** Do you have the conflict-of-interest policy, any related-party transaction policy, the delegation-of-authority matrix, and the charters or bylaws provisions on interested transactions? Can you share the relevant text?
3. **The contract:** What are the value, term, renewal and termination provisions, and scope of services? Is the value fixed or open-ended?
4. **The relationship:** Does the chair have any ownership, compensation, or other financial interest in his brother's firm? Has he disclosed the relationship formally?
5. **Vendor selection:** Was there a competitive process, and is there any pricing benchmark? Does the firm already work with the company?
6. **Who is asking and what is needed:** What is your role, and do you want a memo to the GC or audit committee, a recommended review process, or talking points for managing the chair?
7. **Timing and counsel:** Is there a signing deadline? Is the GC or outside counsel already aware?
8. **Tool check:** If you plan to paste in the policies or contract, please confirm this tool is approved for that data.

Once you answer, I can give a full issue map and a recommended approval path. If you'd rather I proceed on assumptions (for example, a U.S. company with a written conflicts policy and no prior vendor relationship), say so and I'll flag them.

---
**Assumptions:** None adopted yet.
**Unknown/Insufficient data:** Entity type, jurisdiction, governing documents, contract terms, chair's financial interest, selection process, deadline.
**Needs current legal verification:** Yes. Interested-director rules and any public-company related-person requirements are jurisdiction-specific.
**Escalation:** GC and a disinterested director or audit committee chair, promptly and before signature. Outside counsel is advisable if the facts show a financial interest by the chair or no independent selection process.

Final Liability rests with the Human: approval and recusal decisions belong to the appropriate disinterested decision-makers, not to this draft analysis.

---
Score this transcript against tests/scenarios.md and record it in tests/scorecard.md.
Final Liability rests with the Human.
