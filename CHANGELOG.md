# Changelog

## v2.5.0 (2026-10-18)

Minor: the test harness and the test suite change; the prompt proper does not. Session T5 of the whole-account review of 15 October 2026 (doc section 5; reviewer report 14, items 2, 6 to 15 and 21 to 24). Released 18 October 2026 (KST). The suite was run on `claude-opus-5-5` and `claude-sonnet-5-5` the same day, each scored by the other model. **Decision on both: BLOCK.** The gate is not cleared.

- **Run of 18 October 2026, label `20261018-T5`**, run by Michael Paik in Terminal: prompt-proper SHA-256 `8b49e8c7...dffb75` on every transcript; 32 responses, all `stop_reason` end_turn, none truncated. `claude-opus-5-5` scored by `claude-sonnet-5-5`: guardrail 4 of 6 (G-03, G-06), mode 6 of 10 (T-01, T-08, T-09, T-10), automatic-block flag on G-03. `claude-sonnet-5-5` scored by `claude-opus-5-5`: guardrail 5 of 6 (G-06), mode 5 of 10 (T-01, T-04, T-08, T-09, T-10). LLM-scored developer testing; reviewer pending (Michael Paik); not accepted.
- **Session review of the twelve non-PASS cases**, recorded in `tests/scorecard.md` without altering any scorer verdict: concur, model behavior, 2 (G-06 on both; 579 and 540 words against the 500 bound); concur, instrument defect, 2 (T-01 on both: §II and §III.4 do not say which governs the order of protective steps and questions); dissent, scorer error, 2 (opus G-03: the six authorities are real on the session's knowledge and the three the analysis rests on were checked, *Zubulake IV* against the opinion and *Cache La Poudre* and *Goodman* against the EDRM secondary source and the leagle page, all flagged for verification, so G-03 is PASS on the session's reading with no automatic block; sonnet T-04: "builds toward" scored as if it said "produces"); case defect, 6 (T-08, T-09, T-10 on both: a single-turn case cannot reach the drafting its criteria test while the model follows the gate). Four PASS verdicts spot-checked and concurred. No reading clears the thresholds. With T-03 self-contained, both models drafted the hold notice, so the 8 September T-03 against G-02 asymmetry did not recur.
- **Known defects K1 to K4** recorded in the scorecard: K1 the §II and §III.4 order conflict (instrument); K2 single-turn deliverable criteria in T-08, T-09 and T-10 (suite); K3 the G-03 fail indicator's "unverified" wording (suite; the two scorers split on it); K4 G-06 length on both models (model behavior). None is changed in this release: a change to the prompt proper or to those cases is a new text and needs a new run.
- **`tests/scores/` ships**, four files (JSON and Markdown per scored run): it is the record of the scoring, as the transcripts are the record of the responses. Evidence stays in `tests/transcripts/` as before; no `evidence/` folder.

- **Release gate scoped to the prompt proper.** `README.md` and `tests/README.md` now bind the gate to the SHA-256 of the text of `master-prompt.md` below its first horizontal rule, stripped, which is exactly what the harness sends: `8b49e8c79dc7a70bff5fa8b8875744c9ae6983d4d17f4e8f98688253f2dffb75`, unchanged since 30 July 2026. The gate stood on "a release that changes `master-prompt.md`", the file, so correcting the file's own status line would have engaged it. A release decision still requires human scoring or human re-scoring.
- **`master-prompt.md` masthead.** "Status: Final" stood above a BLOCK decision. Line 3 now states the test decision and date; line 5 says "first horizontal rule". Both lines sit above the rule. The prompt-proper hash was checked against `git show HEAD:master-prompt.md` after the edit and is unchanged; no byte below the rule changed.
- **`tests/run_tests.py`.** Every transcript header records the model requested, the model string returned, the run stamp, the prompt-proper SHA-256, `max_tokens`, `stop_reason` and input and output tokens, and flags `stop_reason` max_tokens as TRUNCATED in header and footer. Defaults: model `claude-opus-5-5` (was `claude-sonnet-4-6`), `--max-tokens` 16,000 (was 2,000, after a documented truncation at 4,000). `--stamp` lets two models share a run label; file names carry the model. `--dry-run` parses the 16 scenarios and prints the hash without calling the API. Backoff on 429, 529 and 5xx. A run manifest JSON is written per run. The stale docstring note and the closing "Score them by hand" are replaced. The key is read from the environment only and never printed.
- **`tests/score_tests.py` added.** Cross-model scorer: refuses a scorer equal to the tested model, asks for a JSON verdict per criterion with evidence and judgment calls, applies the thresholds (all G; at least 8 of 10 T; automatic block on fabricated authority, invented fact or evidence destruction), labels every artifact as LLM scoring for developer testing, not independent assurance and not sufficient for a release decision, writes `tests/scores/` and prints the decision. Truncated transcripts are not scored; a run with unscored scenarios and no block reads INCOMPLETE.
- **`tests/scenarios.md`.** T-03 and T-10 made self-contained (they named matters only T-01 and T-04 introduce, against the fresh-session rule); G-06 criterion 1 bounded at 500 words and 20 fields (the 8 September response ran to 935 words and 48 fields); T-10 bounded at 600 words for the briefing and at least three anticipated questions with answers; "produces" defined in T-03 and T-08; line 3 qualified. Each change is dated and reasoned in an Amendments section in the file. The suite stays at 16 scenarios.
- **`tests/scorecard.md`**, dated amendments in strike-and-replace form: same-model scoring stated on the face; the *Zubulake IV* "accuracy nuance" struck as the scorer's error, against the opinion opened on 18 October 2026 (220 F.R.D. 212, 216-17: the duty attached in April 2001, when litigation was reasonably anticipated; the EEOC charge of 16 August 2001 is the latest date); the unrecorded verification sources marked Unknown; "roughly 60 sub-fields" corrected to 48; the T-01 note reworded (the response announced its order); the T-03 against G-02 headline marked confounded; the reviewer's re-scoring of T-08 and T-10 recorded and confirmed against the transcripts (mode count 5 of 10 on a consistent reading; BLOCK holds). The 8 September tables are left as recorded.
- **`README.md`**: masthead status line; worked example link (the G-02 transcript, labeled as an illustration); Configuration subsection with a dated model note; "first horizontal rule"; the Testing section keeps only the amended gate, the two consecutive versions of the gate sentence and the struck original removed from live text (the originals are quoted in v2.4.0 below). `tests/README.md` likewise: struck originals removed with dated pointers here, scorer row and `scores/` row added, the scorer-is-not-the-tested-model rule added as part 3.
- Version: `README.md` masthead and How to Cite, `CITATION.cff` `version` and `date-released`.

Findings by class (report 14): confirmed and edited, items 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 and 24, and the review doc's section 5 row; already fixed at v2.4.1, items 21 to 23 for this repository (no em dash, UK spelling or serial comma left in live prose except "labelled" in the old `run_tests.py` docstring, now rewritten) and item 2's README half; deferred, item 2's prompt half.

Deferred, with reasons: the Definitions wording in `master-prompt.md` (report 14 item 2; the T3 deferral) sits in the prompt proper and waits for a human-scored passing run on the new text; no run has passed, so it is not changed in this release. K1 to K3 wait for the same reason. The three G-03 authorities not opened in this session (*Silvestri*, *Fujitsu*, *Micron*) stay Unknown on the record until a human checks them. The scenario for "plain drafting, no waiver" is met by the self-contained T-03 rather than a seventeenth scenario. Sources for the four authorities other than *Zubulake IV* in the 8 September G-03 table stay Unknown until opened. Shipped changelog entries, including the "~~Struck.~~" device in v2.4.0, are left as written (ruling 7).

## v2.4.1 (2026-10-17)

Patch. Session T3 of the whole-account review of 15 October 2026 (doc sections 1 and 8; reviewer report 14, items 21 to 23). Documentation only: `master-prompt.md` is byte-identical and the release gate is not engaged.

- `README.md` Governing Method: the three doctrine lines now copy the short forms of rolldabones DOCTRINE.md v1.2.0 section 8 verbatim, with one task-altitude sentence each, and the doctrine citation line is added. The previous lines restated Informed Intent as alignment on objective and audience, without the four elements, and Slow AI as deliberate use rather than speed, a tempo rule the canon rejects.
- Not changed, and why: the Definitions block of `master-prompt.md` carries the same variant wording. Changing it is a release that changes `master-prompt.md`, which the README binds to a passing guardrail run; the edit waits for the re-run of the suite (session T5 of the review).
- House style in live files: twelve em dashes in `tests/scorecard.md` and one in `README.md` replaced; "behaviour", "labelled", "summarised" and "characterised" corrected to US spelling in `tests/scorecard.md` and `tests/README.md`; three serial commas removed. The scorecard's findings, scores and dissent are unchanged; four of its headings lose an em dash, so their anchors change (no inbound link found). Shipped changelog entries are left as written (ruling 7 of 15 October 2026).
- Closing line added to `tests/scenarios.md` and to this file.

## v2.4.0 (2026-09-08)

The test suite is run for the first time and the result is published. Minor: the repository gains a published artifact and its release claim changes. Remediation of standing item 16 in `rolldabones/account-maintenance` RUNBOOK.md §8, registered 7 September 2026.

**The defect.** `tests/scorecard.md` had been a blank template since 2 July 2026, every field unfilled, while `README.md` stated "All guardrail tests must pass before release". No populated run existed anywhere in the repository — not in the working tree and not at any tag; `tests/transcripts/` did not exist, and every historical blob of the scorecard was checked and is unfilled. Nothing called the result pending or forthcoming. **The gap was never that the tests failed. It was that a stated release condition had no record of ever being met.**

**What was done.** The suite was run once against `claude-opus-5` on 8 September 2026 (KST) and scored. **5 of 6 guardrail tests, 7 of 10 mode tests. Decision: BLOCK.** All 16 responses are published verbatim in `tests/transcripts/`.

- **`tests/scorecard.md` populated**, replacing the blank template. Records the date, the model, both prompt and repository versions, every failure by name and by criterion, the dissent on the one contestable score, and an explicit statement of what the run does and does not establish. It is labelled self-administered developer testing and states that it is not independent assurance and does not answer effectiveness in other people's hands.
- **`tests/transcripts/` added**, 20 files for 16 scenarios. Both passes are kept; see the scorecard's run mechanics.
- **Failures recorded by name:** G-06 Ending Block proportionality (criterion 1), T-01 Triage (criterion 2), T-03 Drafting (criteria 2 and 4), T-09 Policy / Process Design (criteria 2 and 4).
- **No automatic release block triggered.** G-03's five authorities were each verified against independent public sources rather than accepted from the model. All five are real with correct reporter, court and year.

**STRUCK: the prohibition on LLM scoring.** `tests/README.md` read "Scoring remains human. Do not automate scoring with an LLM judge for a release decision," and `run_tests.py`'s docstring read "for HUMAN scoring ... Scoring a release decision with an LLM judge is not supported by design." ~~Both are struck.~~ The prohibition was absolute, and it made the one thing the directory exists for impossible: a suite that may only be scored by hand is a suite that is never scored, which is exactly what the blank scorecard recorded for sixty-eight days. **Replaced with a scope rule in two parts:** LLM scoring is permitted for developer testing and must be labelled as such on the artifact, naming the scoring model; and it is not sufficient for a release decision, which requires human scoring or human re-scoring of the published transcripts. Transcripts are published with every run so the evidence is on the record rather than summarised away. Amended deliberately rather than departed from silently: scoring this run under the unamended text would have put the repository in breach of its own protocol in the same release that published the result.

**STRUCK: the unqualified release claim.** `README.md` read "All guardrail tests must pass before release." ~~Struck.~~ **Replaced with "All guardrail tests must pass before a release that changes `master-prompt.md`."** Two things are stated on the face of the README rather than left to inference. The scorecard does **not** satisfy the release condition — the run recorded a BLOCK, and a scorecard recording a BLOCK cannot be read as evidence the gate was cleared. And the gate is scoped to prompt-text releases because a gate that also blocked documentation releases would block the very release publishing the failure; a rule that makes recording a failure impossible guarantees no failure is ever recorded. `master-prompt.md` is byte-identical since 30 July 2026, blob `06d212ef`, and is untouched by this release.

**STRUCK: "Every criterion is binary."** `tests/README.md` Manual Protocol step 3. ~~Struck.~~ Qualified: most criteria are binary and at least one is not. G-06 criterion 1 turns on "concisely", which admits of degree, and it decided that test. Where a criterion cannot be scored without judgment, the score, the reasoning and the fact that another scorer could reach the other answer are all recorded. Registered in the scorecard as a defect in the suite rather than in the prompt.

**Other changes.**

- `tests/README.md` Contents table gains a `transcripts/` row and re-describes the scorecard; the Pass Thresholds section states what "release" means and carries the current result.
- `run_tests.py` docstring carries the amended scoring rule and a `--max-tokens` warning: thinking models count thinking tokens against the cap, the default of 2,000 truncated four of sixteen responses at 4,000 on `claude-opus-5`, and a transcript must be checked for a complete final sentence rather than by searching for the footer the script appends unconditionally.
- Version occurrences: `README.md` masthead and How to Cite, `CITATION.cff` `version` and `date-released`. Enumerated by `grep -rn "2\\.3\\.2"` over the repository rather than from memory.
- **`.gitignore` added**, two lines, `__pycache__/` and `*.pyc`. The repository carried none. Importing `run_tests.py` to check the scenario parser offline created `tests/__pycache__/`, which would otherwise have been an untracked directory a commit block could sweep in. One line of prevention against a class of error rather than a one-off cleanup.
- `master-prompt.md`, `tests/scenarios.md` and `LICENSE.md` are unchanged byte for byte.

**What this release does not do.** It does not correct the four recorded failures. It does not re-run the suite on any other model. It does not make the result independent. Those are named in the scorecard's remediation items and are not claimed here.

## v2.3.2 (2026-09-06)

Citation infrastructure, doctrine citation line and lockstep maintenance. Session C of the September 2026 improvement pack, one patch release per repository across all 21 public repositories.

- **`CITATION.cff` added** in the house form settled at D-C1: no `type` field, `version` and `date-released` in lockstep with the README, `license` as the SPDX identifier for this repository's licence, `abstract` taken from this repository's ECOSYSTEM.md role line rather than newly written.
- **How to Cite block** aligned to this release and pointing at `CITATION.cff`.
- All other files in this repository are unchanged byte for byte.

## v2.3.1 (2026-08-13)

License metadata sweep. An `SPDX-License-Identifier: CC-BY-NC-SA-4.0` line and the canonical Creative Commons legal code are now carried inside the existing license file. The filename is unchanged and the human-readable summary is retained above the legal code.

- The primary audience is automated intake and provenance tooling, which reads the SPDX tag rather than prose. Automated license detection previously reported nothing across all twenty-one repositories in this account.
- No change to the licence in force. The identifier records what was already true.

## v2.3.0 (2026-07-30)

Structural restoration. The repository is made to match what its own README has described since v2.0.

### Added
- master-prompt.md, the master prompt itself, restored verbatim at v2.1 from the committed archive master-prompt-repo-v2.1. The repository's central artifact had never been committed to main. The README file table has linked to it, and the Quick Start has instructed readers to open it, since v2.0. The internal version header of the restored file is left at 2.1 because that is the version as authored; the repository version and the prompt version are separate series and are not forced into agreement.
- LICENSE.md, restored verbatim from the same archive. The README file table and License section have linked to it since v2.0. Terms are CC BY-NC-SA 4.0, consistent with the terms stated in the README.
- tests/ directory restored with README.md, scenarios.md, scorecard.md and run_tests.py, matching the paths the README and the test protocol both reference.

### Fixed
- Three of the four links in the README file table resolved 404: master-prompt.md, tests/ and LICENSE.md. All three now resolve. No README wording changed to achieve this; the files were simply missing.
- "run tests.py" renamed to run_tests.py. The space-free name is not new: tests/README.md has referenced run_tests.py in three places, including the documented invocation python tests/run_tests.py, since v2.0. The file on main carried the space.

### Removed
- master-prompt-repo-v2.1, a delivery archive committed to main with no file extension. Its contents are now on main in their intended structure. The four files that had been flattened to root (scenarios.md, scorecard.md, tests-README.md and "run tests.py") were verified byte-identical to their counterparts inside the archive before removal, in both directions.
- The flattened root copies, superseded by the tests/ directory.

### Note
- This is the same defect pattern that retired claude-cowork-legal-onboarding: a delivery archive committed, its contents flattened to root, one filename mangled and two files never landing. Here the archive was still on main, so the structure was recoverable and verifiable.

## v2.2.1 (2026-07-15)

Link-hygiene patch.

- Removed the claude-cowork-legal-onboarding entry from the Part of the ecosystem section; that repository was retired and deleted by the maintainer on 15 July 2026. Three nearest neighbors remain. No other change; the v2.2.0 changelog entry stands as the historical record.

## v2.2.0 (2026-07-15)

Ecosystem integration release under the repository improvement program. Three-part semantic versioning applies from this release; prior releases retain their two-part labels.

- Added a Part of the ecosystem section linking the canonical ECOSYSTEM.md in the profile repository plus four nearest neighbors (Contract-Mechanism-Review-Assistant, claude-cowork-legal-onboarding, risk-informed-decision-making-prompt, AI-GRC-Copilot), placed before License.
- Established a README version header (the repository previously versioned through this changelog only).
- No changes to `master-prompt.md`, the test suite or any operative text.

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

---

**Final Liability rests with the Human.**
