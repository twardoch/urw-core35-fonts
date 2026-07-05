#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["fonttools>=4.50"]
# ///
# this_file: validate_fonts.py
"""Parse every binary font in this archive and fail loudly if any is broken.

The fonts are the product here — nobody edits them, but a corrupted upload or a
truncated Git object would ship a font that no renderer can open. This script is
the tripwire: it opens each OpenType file (.otf/.ttf), reads the name and glyph
tables, and reports anything that will not parse. CI runs it on every push.
"""

from __future__ import annotations

import sys
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).parent


def check(path: Path) -> str | None:
    """Return an error string if the font is unreadable, else None."""
    try:
        font = TTFont(str(path))
        # Touch the tables a renderer needs first; a lazy open alone proves little.
        font["name"].getDebugName(4)
        font.getGlyphSet()
        font.close()
    except Exception as exc:  # noqa: BLE001 — any failure is a broken font
        return f"{path.name}: {type(exc).__name__}: {exc}"
    return None


def main() -> int:
    fonts = sorted([*ROOT.glob("*.otf"), *ROOT.glob("*.ttf")])
    if not fonts:
        print("No .otf/.ttf fonts found — nothing to validate.", file=sys.stderr)
        return 1

    failures = [err for f in fonts if (err := check(f))]
    for err in failures:
        print(f"FAIL {err}", file=sys.stderr)

    print(f"Validated {len(fonts)} fonts: {len(fonts) - len(failures)} OK, {len(failures)} broken.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
