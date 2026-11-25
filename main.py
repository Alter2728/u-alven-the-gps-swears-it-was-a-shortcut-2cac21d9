#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — writes the GPS's one-line excuse
to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "The map promised a shortcut — it just forgot to mention the
#    wedding, the ducks, and the lake where the road used to be."
# Why it was revised: the GPS never speaks. "The map promised"
# blames a third party from outside, so the line reads like the
# driver's complaint, not the GPS's own excuse — and the judge's
# first criterion is that the line IS the GPS's excuse, in its voice.
#
# REVISION (final): the GPS speaks in the first person and opens by
# defending itself — "The shortcut was real" — then lists the damage
# as a smug receipt ("three minutes shorter, one wedding crashed,
# and a lake where the road used to be"), so the joke turns on the
# GPS treating a disaster as a bargain. The punchline lands last:
# "Blame the map; I only read it" — the GPS caught red-handed,
# blaming the map while admitting it never checked. Fresh, specific
# details (wedding, lake) instead of any recalculating cliché, and
# the line reads cleanly aloud in one breath.
# ---------------------------------------------------------------------------
ENTRY = (
    "The shortcut was real — three minutes shorter, one wedding "
    "crashed, and a lake where the road used to be. Blame the map; "
    "I only read it."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
