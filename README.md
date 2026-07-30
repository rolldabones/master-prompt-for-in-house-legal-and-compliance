# Master Prompt for In-House Legal & Compliance

**Version 2.3.0 · 2026-07-30 · Changes: [CHANGELOG.md](CHANGELOG.md)**

A system prompt that turns a general-purpose AI assistant into a disciplined in-house legal and compliance assistant. It supports in-house counsel, compliance officers, legal operations, HR, procurement, internal audit, executives and business stakeholders in handling legal and compliance matters with discipline, clarity and practical usefulness.

It does not replace licensed counsel, current legal research or human judgment. It improves issue spotting, fact development, drafting quality, preservation discipline, escalation timing, outside-counsel management and operational decision support.

## Governing Method

- **Informed Intent.** The User and the model align on objective, audience, jurisdiction, constraints, risk posture and intended use before substantive work begins.
- **Slow AI.** Deliberate, verified, context-aware use of AI rather than speed for its own sake.
- **Final Liability rests with the Human.** The User remains the decision-maker, accountable for final judgment, approvals and use of the output.

## What's in This Repository

| File | Contents |
| --- | --- |
| [`master-prompt.md`](master-prompt.md) | The full prompt. Copy everything below its horizontal rule into your assistant configuration. |
| [`tests/`](tests/) | Behavioral test suite: 16 scenarios, scorecard and optional API harness. |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history. |
| [`LICENSE.md`](LICENSE.md) | CC BY-NC-SA 4.0. |

## Quick Start

1. Open [`master-prompt.md`](master-prompt.md) and copy everything below the horizontal rule.
2. Paste it into the system prompt, project instructions or custom-assistant configuration of your AI tool (for example, a Claude Project, an API system prompt or an equivalent field in another platform).
3. Confirm with your organization that the tool and workspace are approved for the data classes you intend to use. The prompt reminds users of this, but the prompt cannot enforce it.
4. Start a matter. The assistant will state a mode, run the Informed Intent Gate and ask the minimum questions needed to align before producing work product.

To skip clarification on routine matters, say **No questions** and the assistant will proceed on stated assumptions and flag them.

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

The prompt ships with a behavioral test suite in [`tests/`](tests/): ten mode tests and six guardrail tests covering the Informed Intent Gate, fabrication resistance, the data-class stop rule, spoliation refusal and Ending Block proportionality. All guardrail tests must pass before release. Rerun the suite after any prompt edit or model change. See [`tests/README.md`](tests/README.md) for the protocol and thresholds.

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

## License

Released under [CC BY-NC-SA 4.0](LICENSE.md). You may share and adapt this work for non-commercial purposes with attribution, under the same license.

## Author

Son-U Michael Paik. Part of a broader body of work on AI governance, risk management and compliance, including the book *Final Liability Rests with the Human* and its companion documents.

---

**Final Liability rests with the Human.**
