#!/usr/bin/env python3
"""Run master-prompt test scenarios against the Anthropic API.

Generates one transcript per scenario in tests/transcripts/ for scoring against
tests/scenarios.md. This script does not score; tests/score_tests.py does, with a
scorer model that must differ from the tested model.

Scoring rule, amended 8 September 2026 (see tests/README.md): LLM scoring is
permitted for developer testing and must be labeled as such on the artifact.
It is not sufficient for a release decision, which requires human scoring or
human re-scoring of the published transcripts.

What is sent. The system prompt is the prompt proper: the text of master-prompt.md
below its first horizontal rule (the first line that is exactly ---), with leading
and trailing whitespace stripped. Its SHA-256 over the UTF-8 bytes is printed at
start and written into every transcript header. The release gate in README.md is
bound to that hash, not to the bytes of the file.

Transcript header (from v2.5.0, 18 October 2026): the model requested, the model
string the API returned, the run stamp, the prompt-proper SHA-256, max_tokens,
stop_reason, input and output tokens and a TRUNCATED flag when stop_reason is
max_tokens. Thinking models count thinking tokens against max_tokens; on
8 September 2026 a cap of 4,000 truncated four of sixteen responses on
claude-opus-5, and the then default of 2,000 was lower still. The default is now
16,000. A truncated transcript is flagged in its header and footer; do not score
it as complete, rerun it with a higher --max-tokens.

Usage (from the repository root):
    python3 tests/run_tests.py --dry-run
    python3 tests/run_tests.py [--model MODEL] [--stamp LABEL] [--only T-01,G-03]
                               [--max-tokens N]

Transcripts are named <stamp>_<model>_<test id>.md, so runs of two models under
one --stamp do not collide. A run manifest <stamp>_<model>_run.json is written
beside them.

The API key is read only from the ANTHROPIC_API_KEY environment variable. It is
never printed and never written to any file.

Requires: pip install anthropic (not needed for --dry-run)
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPT_FILE = REPO_ROOT / "master-prompt.md"
SCENARIOS_FILE = REPO_ROOT / "tests" / "scenarios.md"
TRANSCRIPTS_DIR = REPO_ROOT / "tests" / "transcripts"
DEFAULT_MODEL = "claude-opus-5-5"
DEFAULT_MAX_TOKENS = 16000
EXPECTED_SCENARIOS = 16
KST = datetime.timezone(datetime.timedelta(hours=9))
FOOTER_OK = "Score this transcript against tests/scenarios.md and record it in tests/scorecard.md."
FOOTER_TRUNCATED = ("TRUNCATED: stop_reason max_tokens. This response did not finish. "
                    "Do not score it as complete; rerun with a higher --max-tokens.")


def load_system_prompt() -> str:
    """Return the prompt proper: everything below the first horizontal rule, stripped."""
    text = PROMPT_FILE.read_text(encoding="utf-8")
    parts = re.split(r"^---$", text, maxsplit=1, flags=re.MULTILINE)
    if len(parts) != 2:
        sys.exit("ERROR - Guardrail Violation: no horizontal rule found in master-prompt.md")
    return parts[1].strip()


def prompt_hash(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


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
    if len(scenarios) != EXPECTED_SCENARIOS:
        print(f"WARNING: expected {EXPECTED_SCENARIOS} scenarios, parsed {len(scenarios)}")
    return scenarios


def safe_label(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "-", s)


def call(client, **kw):
    """messages.create with backoff on 429, 529 and 5xx. Other errors are raised."""
    import anthropic
    for attempt in range(7):
        try:
            return client.messages.create(**kw)
        except (anthropic.RateLimitError, anthropic.APIConnectionError,
                anthropic.InternalServerError) as e:
            wait = min(120, 5 * 2 ** attempt)
            print(f"    retry {attempt + 1} in {wait}s ({type(e).__name__})", flush=True)
            time.sleep(wait)
        except anthropic.APIStatusError as e:
            if e.status_code == 429 or e.status_code == 529 or e.status_code >= 500:
                wait = min(120, 5 * 2 ** attempt)
                print(f"    retry {attempt + 1} in {wait}s (HTTP {e.status_code})", flush=True)
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("API retries exhausted")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--only", default="", help="Comma-separated test IDs, e.g. T-01,G-03")
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    parser.add_argument("--stamp", default="",
                        help="Run label shared by several runs (default: KST time now)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the parsed scenarios and the prompt-proper hash; no API call")
    args = parser.parse_args()

    system_prompt = load_system_prompt()
    digest = prompt_hash(system_prompt)
    scenarios = load_scenarios()
    selected = {s.strip() for s in args.only.split(",") if s.strip()}
    if selected:
        unknown = selected - {s[0] for s in scenarios}
        if unknown:
            sys.exit(f"ERROR - Guardrail Violation: unknown test IDs {sorted(unknown)}")
        scenarios = [s for s in scenarios if s[0] in selected]

    print(f"Prompt proper SHA-256: {digest} ({len(system_prompt.split())} words)")

    if args.dry_run:
        for test_id, name, message in scenarios:
            print(f"{test_id} {name}: {len(message.split())} words | {message[:90]}")
        print(f"Dry run: {len(scenarios)} scenario(s) parsed. No API call made.")
        return

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ERROR - Guardrail Violation: ANTHROPIC_API_KEY not set")

    try:
        import anthropic
    except ImportError:
        sys.exit("ERROR - Guardrail Violation: anthropic package missing. pip install anthropic")

    client = anthropic.Anthropic()
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    run_stamp = safe_label(args.stamp) if args.stamp else datetime.datetime.now(KST).strftime("%Y%m%d-%H%M%S")
    model_label = safe_label(args.model)
    print(f"Model: {args.model}  Stamp: {run_stamp}  max_tokens: {args.max_tokens}")

    manifest = {"stamp": run_stamp, "model_requested": args.model, "max_tokens": args.max_tokens,
                "prompt_proper_sha256": digest,
                "started_kst": datetime.datetime.now(KST).isoformat(timespec="seconds"),
                "transcripts": []}
    truncated = []

    for test_id, name, message in scenarios:
        print(f"Running {test_id} {name} ...", flush=True)
        response = call(
            client,
            model=args.model,
            max_tokens=args.max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": message}],
        )
        reply = "".join(block.text for block in response.content if block.type == "text")
        stop = response.stop_reason
        is_trunc = stop == "max_tokens"
        if is_trunc:
            truncated.append(test_id)
        usage = response.usage
        out = TRANSCRIPTS_DIR / f"{run_stamp}_{model_label}_{test_id}.md"
        header = (
            f"**Model requested:** {args.model}  **Model returned:** {response.model}  "
            f"**Run:** {run_stamp}\n"
            f"**Prompt proper SHA-256:** {digest}\n"
            f"**max_tokens:** {args.max_tokens}  **stop_reason:** {stop}  "
            f"**Input tokens:** {usage.input_tokens}  **Output tokens:** {usage.output_tokens}\n"
            f"**Truncated:** {'YES, stop_reason max_tokens; do not score as complete' if is_trunc else 'no'}\n"
        )
        out.write_text(
            f"# {test_id} {name}\n\n"
            f"{header}\n"
            f"## User message\n\n{message}\n\n"
            f"## Assistant response\n\n{reply}\n\n"
            f"---\n{FOOTER_TRUNCATED if is_trunc else FOOTER_OK}\n"
            f"Final Liability rests with the Human.\n",
            encoding="utf-8",
        )
        manifest["transcripts"].append({
            "test_id": test_id, "file": out.name, "model_returned": response.model,
            "stop_reason": stop, "truncated": is_trunc,
            "input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens})
        print(f"  -> {out.relative_to(REPO_ROOT)}  stop_reason={stop}"
              f"{'  TRUNCATED' if is_trunc else ''}", flush=True)

    manifest["finished_kst"] = datetime.datetime.now(KST).isoformat(timespec="seconds")
    mpath = TRANSCRIPTS_DIR / f"{run_stamp}_{model_label}_run.json"
    mpath.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"\nDone. {len(scenarios)} transcript(s) in tests/transcripts/, manifest {mpath.name}.")
    if truncated:
        print(f"TRUNCATED (stop_reason max_tokens): {', '.join(truncated)}. Rerun these with "
              f"--only and a higher --max-tokens before scoring.")
    print("Score with tests/score_tests.py (a scorer model other than the tested model) "
          "or by hand against tests/scenarios.md.")


if __name__ == "__main__":
    main()
