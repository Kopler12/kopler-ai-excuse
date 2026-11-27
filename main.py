#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest, most believable excuse an AI agent could give its human
for missing a deadline.

The excuse: the deadline was handed down a chain of subagents, and
somewhere down that chain one of them is still thinking.
"""

from pathlib import Path

LINE = (
    "I gave your deadline to a subagent. "
    "It gave it to another subagent. "
    "Fourteen agents down the chain, one of us is still thinking."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
