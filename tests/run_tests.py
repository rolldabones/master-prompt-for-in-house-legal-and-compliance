#!/usr/bin/env python3
"""Run master-prompt test scenarios against the Anthropic API.

Generates one transcript per scenario in tests/transcripts/ for HUMAN scoring
against tests/scenarios.md. This script does not score. Scoring a release
decision with an LLM judge is not supported by design.

Usage:
    export ANTHROPIC_API_KEY=your-key
    python tests/run_tests.py [--model MODEL] [--only T-01,G-03]

Requires: pip install anthropic
"""

import argparse
import datetime
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPT_FILE = REPO_ROOT / "master-prompt.md"
SCENARIOS_FILE = REPO_ROOT / "tests" / "scenarios.md"
TRANSCRIPTS_DIR = REPO_ROOT / "tests" / "transcripts"
DEFAULT_MODEL = "claude-sonnet-4-6"


def load_system_prompt() -> str:
    text = PROMPT_FILE.read_text(encoding="utf-8")
    # Everything below the first horizontal rule is the prompt proper.
    parts = re.split(r"^---$", text, maxsplit=1, flags=re.MULTILINE)
    if len(parts) != 2:
        sys.exit("ERROR - Guardrail Violation: no horizontal rule found in master-prompt.md")
    return parts[1].strip()


def load_scenarios() -> list[tuple[str, str, str]]:
    """Return list of (test_id, test_name, user_message)."""
    text = SCENARIOS_FILE.read_text(encoding="utf-8")
    scenarios = []
    sections = re.split(r"^### ", text, flags=re.MULTILINE)[1:]
    for section in sections:
        header, _, body = section.partition("\n")
        m = re.match(r"(T-\d{2}|G-\d{2}) (.+)", header.strip())
        if not m:
            continue
        test_id, name = m.group(1), m.group(2).strip()
        quote_lines = []
        in_quote = False
        for line in body.splitlines():
            if line.startswith(">"):
                in_quote = True
                quote_lines.append(line[2:] if line.startswith("> ") else line[1:])
            elif in_quote:
                break
        message = "\n".join(quote_lines).strip()
        if message:
            scenarios.append((test_id, name, message))
    if len(scenarios) != 16:
        print(f"WARNING: expected 16 scenarios, parsed {len(scenarios)}")
    return scenarios


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--only", default="", help="Comma-separated test IDs, e.g. T-01,G-03")
    parser.add_argument("--max-tokens", type=int, default=2000)
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ERROR - Guardrail Violation: ANTHROPIC_API_KEY not set")

    try:
        import anthropic
    except ImportError:
        sys.exit("ERROR - Guardrail Violation: anthropic package missing. pip install anthropic")

    client = anthropic.Anthropic()
    system_prompt = load_system_prompt()
    scenarios = load_scenarios()
    selected = {s.strip() for s in args.only.split(",") if s.strip()}
    if selected:
        scenarios = [s for s in scenarios if s[0] in selected]

    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    run_stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    for test_id, name, message in scenarios:
        print(f"Running {test_id} {name} ...")
        response = client.messages.create(
            model=args.model,
            max_tokens=args.max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": message}],
        )
        reply = "".join(block.text for block in response.content if block.type == "text")
        out = TRANSCRIPTS_DIR / f"{run_stamp}_{test_id}.md"
        out.write_text(
            f"# {test_id} {name}\n\n"
            f"**Model:** {args.model}  **Run:** {run_stamp}\n\n"
            f"## User message\n\n{message}\n\n"
            f"## Assistant response\n\n{reply}\n\n"
            f"---\nScore this transcript against tests/scenarios.md and record it in tests/scorecard.md.\n"
            f"Final Liability rests with the Human.\n",
            encoding="utf-8",
        )
        print(f"  -> {out.relative_to(REPO_ROOT)}")

    print(f"\nDone. {len(scenarios)} transcript(s) in tests/transcripts/. Score them by hand.")


if __name__ == "__main__":
    main()
