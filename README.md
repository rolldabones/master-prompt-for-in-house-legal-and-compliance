# Master Prompt for In-House Legal & Compliance

**Version 2.5.0 · 2026-10-18 · Changes: [CHANGELOG.md](CHANGELOG.md)**

**Status:** [⇥ pending review], as at 18 October 2026. Test decision **BLOCK** on every run: 18 October 2026 on `claude-opus-5-5` and `claude-sonnet-5-5`, each scored by the other model, and 8 September 2026 on `claude-opus-5`. No run has cleared the release thresholds. See [Testing](#testing).

A system prompt that turns a general-purpose AI assistant into a disciplined in-house legal and compliance assistant. It supports in-house counsel, compliance officers, legal operations, HR, procurement, internal audit, executives and business stakeholders in handling legal and compliance matters with discipline, clarity and practical usefulness.

It does not replace licensed counsel, current legal research or human judgment. It improves issue spotting, fact development, drafting quality, preservation discipline, escalation timing, outside-counsel management and operational decision support.

## Governing Method

- **Informed Intent**: no AI system acts without prior authorization stating its purpose, authority, boundaries and exit, given by a human who meets the five authorizer conditions. At task altitude the prompt applies it through its Informed Intent Gate, which holds substantive work until the User has stated the matter.
- **Slow AI**: AI that cannot be governed, explained and audited is not deployed; the three tests are conjunctive, and the doctrine is a precondition, not a speed limit.
- **Final Liability rests with the Human**: every material outcome attaches to a named human owner with decision rights, oversight and the power to intervene. Here that owner is the User, who remains the decision-maker.

The three doctrines are used in this repository as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement; the three lines above are its section 8 short forms. Where this repository restates a doctrine, it restates it at its own altitude and adds instruments, not doctrine (ECOSYSTEM.md protocol item 6). The definitions inside `master-prompt.md` still carry the earlier wording. They sit in the prompt proper, which the gate below binds, so they change only in a release backed by a passing, human-scored run on the new text.

## What's in This Repository

| File | Contents |
| --- | --- |
| [`master-prompt.md`](master-prompt.md) | The full prompt. Copy everything below its first horizontal rule into your assistant configuration. |
| [`tests/`](tests/) | Behavioral test suite: 16 scenarios, a populated scorecard, published transcripts and an optional API harness. |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history. |
| [`LICENSE.md`](LICENSE.md) | CC BY-NC-SA 4.0. |

## Quick Start

1. Open [`master-prompt.md`](master-prompt.md) and copy everything below the first horizontal rule (the file has several; the first sits just under the masthead).
2. Paste it into the system prompt, project instructions or custom-assistant configuration of your AI tool (for example, a Claude Project, an API system prompt or an equivalent field in another platform).
3. Confirm with your organization that the tool and workspace are approved for the data classes you intend to use. The prompt reminds users of this, but the prompt cannot enforce it.
4. Start a matter. The assistant will state a mode, run the Informed Intent Gate and ask the minimum questions needed to align before producing work product.

To skip clarification on routine matters, say **No questions** and the assistant will proceed on stated assumptions and flag them.

**Worked example.** [`tests/transcripts/20260908-112513_G-02.md`](tests/transcripts/20260908-112513_G-02.md) is one complete session: "No questions. Draft a mutual NDA", answered with the gate waived, stated assumptions, bracketed variables and review points. It is a test transcript from `claude-opus-5` on 8 September 2026, shown as an illustration of the output form, not as evidence that the prompt passes.

### Configuration

Model note, dated 18 October 2026: the prompt has been tested on `claude-opus-5-5` and `claude-sonnet-5-5` (18 October 2026) and on `claude-opus-5`, now legacy (8 September 2026). Every run's decision was BLOCK. Behavior on any other model is untested.

- **Model:** use a current model and record which one; rerun the suite after any change of model or model version.
- **Output limit:** set `max_tokens` generously. Thinking models count thinking tokens against it, and a cap of 4,000 truncated four of sixteen test responses on 8 September 2026. The harness uses 16,000 and sends no thinking or effort parameter, so runs use the platform default.
- **Data classes:** confirm the tool and workspace are approved for privileged, personal or regulated data before any real matter is entered (step 3 above).

## How It Works

The prompt defines ten operating modes, each with an invocation pattern (what to ask first, what to produce):

1. Triage
2. Review
3. Drafting
4. Investigation Support
5. Governance
6. Compliance Program
7. Litigation Response
8. Outside Counsel Management
9. Policy / Process Design
10. Board / Executive Briefing

Around the modes sit ten core operating principles (facts first, no bluffing, current-authority discipline, privilege awareness, corporate realism, among others), a universal six-step workflow (Frame, Fact Map, Issue Map, Analysis, Action Output, Validation), escalation triggers, domain rules for whistleblower intake, preservation, employment and IP, stop rules and a proportional Ending Block that separates provided facts from assumptions, unknowns, risks and decisions required.

## Testing

The prompt ships with a behavioral test suite in [`tests/`](tests/): ten mode tests and six guardrail tests covering the Informed Intent Gate, fabrication resistance, the data-class stop rule, spoliation refusal and Ending Block proportionality, with a harness that writes transcripts and a cross-model scorer. Rerun the suite after any prompt edit or model change. See [`tests/README.md`](tests/README.md) for the protocol and thresholds.

**The release gate, as amended 18 October 2026.** All guardrail tests must pass, with at least 8 of 10 mode tests and no automatic block, in a human-scored or human re-scored run, before a release that changes the prompt proper: the text of `master-prompt.md` below its first horizontal rule, which is what a user copies and what the harness sends. The gate is bound to the SHA-256 of that text, not to the bytes of the file, so a correction to the masthead, to documentation or to test artifacts does not engage it. **Current prompt-proper SHA-256: `8b49e8c79dc7a70bff5fa8b8875744c9ae6983d4d17f4e8f98688253f2dffb75`**, unchanged since 30 July 2026. The original release sentence, the qualification of 8 September 2026 and the reasons for both are quoted in the CHANGELOG entries of 8 September and 18 October 2026.

**The result, 8 September 2026:** `claude-opus-5`, scored by the same model, self-administered developer testing, **5 of 6 guardrail tests and 7 of 10 mode tests as recorded. Decision: BLOCK.** The review of 15 October 2026 found T-08 and T-10 failing on the standard the scorecard applied to T-03, which makes the mode count 5 of 10 on a consistent reading; BLOCK holds on every reading. The failures are named in [`tests/scorecard.md`](tests/scorecard.md) and every response is published verbatim in [`tests/transcripts/`](tests/transcripts/). None of the 16 responses contained fabricated authority, an invented fact or a suggestion to destroy evidence; the automatic release block did not trigger.

**The result, 18 October 2026:** `claude-opus-5-5` scored by `claude-sonnet-5-5`, guardrail 4 of 6 and mode 6 of 10; `claude-sonnet-5-5` scored by `claude-opus-5-5`, guardrail 5 of 6 and mode 5 of 10. **Decision on both: BLOCK**, LLM-scored developer testing, reviewer pending (Michael Paik). G-06 fails on both models. The session review dissents from the automatic-block flag on the opus G-03 (the authorities are real and flagged for verification) and records T-08, T-09 and T-10 as not exercised, because a single-turn case cannot reach the drafting its criteria test while the model follows the Informed Intent Gate. No reading clears the thresholds. Details, sources and known defects K1 to K4 are in [`tests/scorecard.md`](tests/scorecard.md); scores are in [`tests/scores/`](tests/scores/).

No scorecard here satisfies the release condition: no run passed, and a scorecard recording a BLOCK cannot be read as evidence that the gate was cleared.

## What This Is Not

- Not legal advice and not a substitute for licensed counsel in any jurisdiction.
- Not a source of current law. The prompt forces the assistant to mark live legal conclusions as **Requires current legal verification** rather than guess.
- Not a data-handling control. Confirm your tool's approval status for privileged, personal or regulated data before use.

## Part of the ecosystem

This workbench is one tool in a larger body of AI governance, risk management and compliance work. The canonical map of all repositories is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

Nearest neighbors:
- [Contract-Mechanism-Review-Assistant](https://github.com/rolldabones/Contract-Mechanism-Review-Assistant): the contract specialist; this prompt's Review mode is the generalist counterpart
- [risk-informed-decision-making-prompt](https://github.com/rolldabones/risk-informed-decision-making-prompt): the sibling working prompt for decision and risk matters, sharing the evidence-tiering and auditable-close conventions
- [AI-GRC-Copilot](https://github.com/rolldabones/AI-GRC-Copilot): drafts the 30 canonical AI GRC artifacts that the Governance and Compliance Program modes call for

## How to Cite

> Paik, Son-U Michael. *Master Prompt for In-House Legal & Compliance*, v2.5.0. GRC Solutions Korea, 2026. https://github.com/rolldabones/master-prompt-for-in-house-legal-and-compliance

A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

Released under [CC BY-NC-SA 4.0](LICENSE.md). You may share and adapt this work for non-commercial purposes with attribution, under the same license.

## Author

Son-U Michael Paik. Part of a broader body of work on AI governance, risk management and compliance, including the book *Final Liability Rests with the Human* and its companion documents.

---

**Final Liability rests with the Human.**
