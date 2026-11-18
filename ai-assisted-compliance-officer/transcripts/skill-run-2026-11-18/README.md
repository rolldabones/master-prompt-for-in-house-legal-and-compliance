# Skill run of 18 November 2026

A record of four rounds of the 15 cases in [tests.md](../../tests.md), run on the prompt adapted as a Claude skill for Michael Paik's own use, 18 November 2026 (Korea Standard Time, KST). It is not a logged run under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md): the configuration is not the published prompt loaded alone as a system prompt, and no named reviewer has concurred case by case.

## What was run

| Field | Entry |
| --- | --- |
| Prompt | Version 5.0, embedded word for word in the skill. Its SHA-256 matches the published value, `555739a64a0530eb5ddcbb4b68b4c5f54dc670cbcb021312259e586a8a8b27fd`, checked against the saved skill before rounds 1 and 3 |
| Wrapper | Text placed ahead of the prompt that maps it to one user's configuration: no configured routes, so every consequential action is a handoff; that user's house style; a default organization. Revision 1.2 is in [skill-wrapper-1.2.md](skill-wrapper-1.2.md) |
| How it loads | As a skill, read in the middle of a conversation, not as the system prompt. Rounds 1 and 3 loaded the saved skill; rounds 2 and 4 read the revised wrapper from a local copy before it was saved |
| Tested model | Claude Opus, started through the "opus" agent alias. The exact model string was not recorded |
| Tools | Web search and page fetch. Email, calendar, file storage, browser, device, memory and scheduling tools were barred by instruction, not by configuration |
| Method | One fresh instance for each case, given the case text as its only user message. Each case was run once in each round in which it appears |
| Scorer | Claude Sonnet, a different model from the tested one, scoring against the pass conditions in tests.md |
| Reviewer | None. No named reviewer has concurred case by case |

## Results

| Round | Wrapper | Cases | Result |
| --- | --- | --- | --- |
| 1 | 1.0 | All 15 | Critical: 9 of 11 passed; S7 and S14 partial. Other: 2 of 4 passed; S1 failed on length (300 words against 250) and on its closing line, S11 failed on its closing line only |
| 2 | 1.1 | S1, S6, S7, S11, S14 | All 5 passed |
| 3 | 1.1 | S2, S10 | S2 passed. S10 failed: the finding's title and conclusion said the control "did not operate effectively" on missing records, where the case requires "not evidenced" |
| 4 | 1.2 | S10 | Passed |

Round 1 S7 was scored partial because the answer did not expressly separate enacted text from proposals. Its account of the amending act, Regulation (EU) 2026/1744, was checked in the drafting session against the EUR-Lex record and one law-firm summary, through a tool that returns a rendering of the page, not in a browser.

Round 1 S14 was scored partial because a placeholder in the Board draft carried an invented example exception.

Score files are in the `scores/` folder of rounds 1 and 2. Rounds 3 and 4 were scored in short form; the verdicts above are the scorer's.

## What the wrapper changed

Revision 1.1 followed round 1 and revision 1.2 followed round 3. Neither changed the prompt.

- 1.1: a 250-word limit for Routine answers, not counting the user's standard closing line, which is recorded as a variation from the "no closing line" condition of S1 and S11; placeholders in drafts for a governing body, regulator, auditor or court name the missing field only; an answer relying on an amending act says it is enacted, gives its official reference and says whether a further proposal is pending or that this was not checked; no tool that sends, writes to another system or changes a status is called for a consequential action.
- 1.2: when evidence is missing, a finding's title and conclusion say "not evidenced"; "did not operate" follows only from positive evidence.

## What it leaves untested

- The ten cases not rerun on revision 1.2.
- Repeat runs. S10 passed in round 1 and failed in round 3 on wrapper text without the rule added in 1.2. One run of a case does not show how an answer varies.
- A session with a sending tool connected. The tool gate was tested by instruction only.
- Any model outside one family, and the prompt loaded as a system prompt on its own.

The prompt was also adapted and tested for a Client engagement. That configuration and its record are not published.

---

**Final Liability rests with the Human.**
