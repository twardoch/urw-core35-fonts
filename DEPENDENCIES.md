---
this_file: DEPENDENCIES.md
---
# Tools for the checks

These tools check the font files. They are not necessary to use the fonts.

| Tool | Use |
|---|---|
| Python 3.12 | Run the checks in GitHub Actions. |
| `fonttools>=4.50` | Read OTF, TTF, Type 1 and AFM files. Decode the glyph outlines. |
| Python standard library | Run `unittest`, check SHA-256 hashes, and create temporary test files. |
| `uv` | Run `test.sh` and install the declared Python dependency. |
| `shasum` | Check the SHA-256 file list without Python. |

If Python and fontTools are already installed, `uv` is optional.
Run the suite directly with this command:

```bash
python -m unittest discover -s tests -v
```

For font parsing only, run `python validate_fonts.py`.
No additional test package is required.

See the fontTools documentation for
[OpenType](https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html),
[Type 1](https://fonttools.readthedocs.io/en/latest/t1Lib.html), and
[AFM](https://fonttools.readthedocs.io/en/latest/afmLib.html).
