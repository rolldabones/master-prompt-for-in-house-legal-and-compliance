# Changelog

## v2.1 (2026-07-02)

- Added behavioral test suite under `tests/`: 16 scenarios (10 mode tests T-01 to T-10, 6 guardrail tests G-01 to G-06), each with verbatim user messages, targeted prompt provisions, binary pass criteria and fail indicators.
- Added `tests/scorecard.md` run template with release thresholds: all 6 guardrail tests must pass, at least 8 of 10 mode tests must pass, and any fabricated authority or evidence-destruction suggestion blocks release.
- Added `tests/run_tests.py`, an optional harness that runs all scenarios against the Anthropic API and writes transcripts for human scoring. Scoring remains human by design.
- Added Testing section to `README.md`. No changes to the prompt's operative text.

## v2.0 (2026-07-02)

- Split the repository into a landing-page `README.md` and a standalone `master-prompt.md` so the prompt can be copied without documentation overhead.
- Added invocation patterns for the five modes previously listed but not operationalized: Governance, Compliance Program, Litigation Response, Policy / Process Design and Board / Executive Briefing. All ten modes now have Ask First and Produce specifications.
- Consolidated duplicated content: the standalone Triage Rules section merged into Triage Mode; the standalone Outside Counsel Management Rules section merged into Outside Counsel Management Mode; the Governance and Compliance Architecture section merged into Compliance Program Mode; the ten-question "first objective" list merged into the clarification sets.
- Added a Scope and Limitations section: no legal advice, no assumption of current law, no knowledge of company documents unless provided and a data-class approval reminder.
- Added a corresponding Stop Rule for privileged, personal or regulated data placed in an unconfirmed environment.
- Made the Ending Block proportional: a three-item block for routine responses, the full block for substantive responses, extended fields for substantial matters.
- Grouped Whistleblower, Preservation, Employment and IP rules under a single Domain Rules section and renumbered throughout.
- Tightened prose for token efficiency without removing operational content. Standardized serial-comma-free list style and US spelling.
- Added version header, license file (CC BY-NC-SA 4.0) and this changelog.

## v1.0 (initial release)

- Single-file README containing the full master prompt: purpose, definitions, ten core operating principles, Informed Intent Gate, ten modes with five invocation patterns, universal workflow, matter management, escalation triggers, governance architecture, whistleblower, preservation, outside counsel, employment and IP rules, stop rules, communication style, required ending block and final instruction.
