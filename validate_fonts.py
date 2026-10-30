#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["fonttools>=4.50"]
# ///
# this_file: validate_fonts.py
"""Parse every font and metrics file, including all tables and glyph outlines."""

from __future__ import annotations

import sys
from pathlib import Path

from fontTools.afmLib import AFM
from fontTools.pens.recordingPen import RecordingPen
from fontTools.t1Lib import T1Font
from fontTools.ttLib import TTFont

ROOT = Path(__file__).parent


def draw_glyphs(font: TTFont | T1Font) -> None:
    """Decode every outline; opening a font alone leaves charstrings unchecked."""
    glyphs = font.getGlyphSet()
    if not glyphs:
        raise ValueError("No glyphs found")
    for glyph in glyphs.values():
        glyph.draw(RecordingPen())


def check(path: Path) -> str | None:
    """Return an error string if the font is unreadable, else None."""
    try:
        if path.suffix == ".afm":
            if not AFM(path).chars():
                raise ValueError("No character metrics found")
        elif path.suffix == ".t1":
            draw_glyphs(T1Font(path))
        else:
            with TTFont(path) as font:
                font.ensureDecompiled()
                font["name"].getDebugName(4)
                draw_glyphs(font)
    except Exception as exc:  # noqa: BLE001 — any failure is a broken font
        return f"{path.name}: {type(exc).__name__}: {exc}"
    return None


def main() -> int:
    fonts = sorted(
        p for p in ROOT.iterdir() if p.suffix in {".afm", ".t1", ".otf", ".ttf"}
    )
    if not fonts:
        print("No font files found — nothing to validate.", file=sys.stderr)
        return 1

    failures = [err for f in fonts if (err := check(f))]
    for err in failures:
        print(f"FAIL {err}", file=sys.stderr)

    print(
        f"Validated {len(fonts)} fonts: {len(fonts) - len(failures)} OK, {len(failures)} broken."
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
