# this_file: tests/test_fonts.py
"""Verify the upstream inventory, corrected te, and validator failure behavior."""

import contextlib
import hashlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from fontTools.afmLib import AFM
from fontTools.pens.recordingPen import RecordingPen
from fontTools.t1Lib import T1Font
from fontTools.ttLib import TTFont

import validate_fonts

ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = (".afm", ".otf", ".t1", ".ttf")


class FontTests(unittest.TestCase):
    def test_inventory_matches_all_upstream_checksums(self) -> None:
        rows = [
            line.split()
            for line in (ROOT / "docs/fonts.sha256").read_text().splitlines()
        ]
        expected = {name: digest for digest, name in rows}
        actual = {p.name for p in ROOT.iterdir() if p.suffix in EXTENSIONS}
        self.assertEqual(
            len(rows), 140, "Manifest must contain all four formats of 35 fonts"
        )
        self.assertEqual(
            actual, set(expected), "Missing current fonts or leftover legacy fonts"
        )
        for name, digest in expected.items():
            with self.subTest(font=name):
                self.assertEqual(
                    hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), digest
                )
        for stem in {Path(name).stem for name in expected}:
            self.assertTrue(all(stem + ext in expected for ext in EXTENSIONS), stem)

    def test_cyrillic_te_has_corrected_width_in_every_format(self) -> None:
        for style, width, tt_width in (("Italic", 374, 766), ("BoldItalic", 409, 838)):
            stem = ROOT / f"NimbusSans-{style}"
            with self.subTest(style=style):
                self.assertEqual(AFM(stem.with_suffix(".afm"))["afii10084"][1], width)
                glyph = T1Font(stem.with_suffix(".t1")).getGlyphSet()["afii10084"]
                glyph.draw(RecordingPen())
                self.assertEqual(glyph.width, width)
                for ext, expected in ((".otf", width), (".ttf", tt_width)):
                    with TTFont(stem.with_suffix(ext)) as font:
                        self.assertEqual(font["name"].getDebugName(5), "Version 1.10")
                        self.assertEqual(
                            font.getGlyphSet()[font.getBestCmap()[0x442]].width,
                            expected,
                        )

    def test_validator_rejects_missing_and_corrupt_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for ext in EXTENSIONS:
                path = Path(directory) / ("broken" + ext)
                with self.subTest(format=ext):
                    self.assertIsNotNone(
                        validate_fonts.check(path), "Missing file must fail"
                    )
                    path.write_bytes(b"not a font\n")
                    self.assertIsNotNone(
                        validate_fonts.check(path), "Corrupt file must fail"
                    )

    def test_validator_rejects_empty_archive(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            patch.object(validate_fonts, "ROOT", Path(directory)),
            contextlib.redirect_stderr(io.StringIO()),
        ):
            self.assertEqual(validate_fonts.main(), 1, "Empty archive must fail")

    def test_validator_parses_all_current_formats(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(validate_fonts.main(), 0, "All current files must parse")
        self.assertIn(
            "Validated 140", output.getvalue(), "AFM and Type 1 must also be checked"
        )


if __name__ == "__main__":
    unittest.main()
