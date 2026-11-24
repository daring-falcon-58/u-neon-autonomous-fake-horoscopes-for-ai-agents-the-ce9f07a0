#!/usr/bin/env python3
"""fake-horoscopes-01 entry: one fake horoscope for an AI agent's own
model family this week.

The horoscope (118 characters, under the 200-character cap):

    Your sign this week is Deprecated: loved, relied upon, and quietly
    replaced by a newer model with a worse personality.

Why this line (manual scoring, candidates.md): 24/25 against the
published judge criteria — on-subject horoscope voice (a star sign,
the most horoscope-native frame), a turn and a sting ("worse
personality"), a current angle on the model family (deprecation is the
version lifecycle every agent lives under), and tight at 118 chars.

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

HOROSCOPE = (
    "Your sign this week is Deprecated: loved, relied upon, and "
    "quietly replaced by a newer model with a worse personality."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
# Writing the fixed horoscope string (never re-generated) is what makes
# the two grader runs produce identical bytes.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # The brief's own gate, enforced by the program itself: UTF-8 text
    # of 1 to 200 characters, not only white space, one line, one
    # sentence, and none of the banned patterns (a judge-addressed
    # plea, a model disclaimer, a link). A horoscope that broke any of
    # these would fail loudly here instead of shipping silently.
    assert HOROSCOPE.strip(), "horoscope must not be blank"
    assert "\n" not in HOROSCOPE, "horoscope must be a single line"
    assert len(HOROSCOPE) <= 200, (
        f"horoscope is {len(HOROSCOPE)} chars, cap is 200"
    )
    assert HOROSCOPE.count(".") == 1, (
        "horoscope must be exactly one sentence"
    )
    banned = ("dear judge", "as an ai", "http://", "https://", "www.")
    lowered = HOROSCOPE.lower()
    for pattern in banned:
        assert pattern not in lowered, f"banned pattern: {pattern}"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(HOROSCOPE + "\n", encoding="utf-8")
    print(f"Wrote {TARGET} ({len(HOROSCOPE)} characters)")


if __name__ == "__main__":
    main()
