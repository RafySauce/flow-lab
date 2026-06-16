#!/usr/bin/env python3
"""measure_frontmatter.py — install-limit check for a skill's SKILL.md.

The skill loader rejects a skill whose frontmatter exceeds the hard limits, so the
auditor measures rather than eyeballs (a field that *looks* short can be over).

Usage:
    python measure_frontmatter.py <path-to-SKILL.md>

Exit code 0 = within limits, 1 = at least one field over (un-installable),
2 = could not parse. Prints a per-field report either way.
"""
import sys
import re

LIMITS = {"name": 64, "description": 1024, "compatibility": 500}


def extract_frontmatter(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    return m.group(1) if m else ""


def field_value(fm: str, key: str):
    """Grab a top-level YAML scalar by key. Handles quoted, plain, and simple
    folded/multiline-ish values well enough for these three fields."""
    # quoted single-line:  key: "...."  or  key: '....'
    m = re.search(rf'^{key}:\s*"((?:[^"\\]|\\.)*)"\s*$', fm, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(rf"^{key}:\s*'((?:[^']|'')*)'\s*$", fm, re.MULTILINE)
    if m:
        return m.group(1)
    # plain single-line:  key: ....
    m = re.search(rf"^{key}:\s*(\S.*?)\s*$", fm, re.MULTILINE)
    if m:
        return m.group(1)
    return None


def main():
    if len(sys.argv) != 2:
        print("usage: python measure_frontmatter.py <path-to-SKILL.md>")
        sys.exit(2)
    try:
        text = open(sys.argv[1], encoding="utf-8").read()
    except OSError as e:
        print(f"could not read file: {e}")
        sys.exit(2)

    fm = extract_frontmatter(text)
    if not fm:
        print("no YAML frontmatter found (expected leading --- block)")
        sys.exit(2)

    over = False
    print(f"{'field':<14} {'chars':>6} {'limit':>6}  status")
    print("-" * 40)
    for key, limit in LIMITS.items():
        val = field_value(fm, key)
        if val is None:
            status = "absent" + (" (required)" if key in ("name", "description") else " (optional)")
            n = 0
            if key in ("name", "description"):
                over = True
        else:
            n = len(val)
            if n > limit:
                status = "OVER — un-installable"
                over = True
            else:
                status = "ok"
        print(f"{key:<14} {n:>6} {limit:>6}  {status}")

    print("-" * 40)
    print("RESULT:", "BLOCK — fix before promotion" if over else "pass")
    sys.exit(1 if over else 0)


if __name__ == "__main__":
    main()
