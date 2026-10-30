---
this_file: README.md
---
# URW Core 35 Fonts

This repository contains 35 URW font styles in 11 families.
They provide alternatives to the standard PostScript fonts.
The files include the URW++ corrections that Artifex distributed in 2017 and 2020.

All 140 font and metrics files match the selected
[Artifex source revision](https://github.com/ArtifexSoftware/urw-base35-fonts/tree/3c0ba3b5687632dfc66526544a4e811fe0ec0cd9/fonts).
The files have not been rebuilt here. Old versions are no longer included.

## Font files

Each style has these files:

| Files | Format |
|---|---|
| `.otf` | OpenType with CFF outlines |
| `.ttf` | OpenType with TrueType outlines |
| `.t1` and `.afm` | Type 1 font program and its font metrics |

Select the format that your application supports.
Use each Type 1 font with its matching AFM file.
Python is necessary only for the checks below, not for font use.

| URW family | PostScript counterpart | Styles |
|---|---|---|
| NimbusSans | Helvetica | Regular, Italic, Bold, Bold Italic |
| NimbusSansNarrow | Helvetica Narrow | Regular, Oblique, Bold, Bold Oblique |
| NimbusRoman | Times | Regular, Italic, Bold, Bold Italic |
| NimbusMonoPS | Courier | Regular, Italic, Bold, Bold Italic |
| URWGothic | ITC Avant Garde Gothic | Book, Book Oblique, Demi, Demi Oblique |
| URWBookman | ITC Bookman | Light, Light Italic, Demi, Demi Italic |
| P052 | Palatino | Roman, Italic, Bold, Bold Italic |
| C059 | Century Schoolbook | Roman, Italic, Bold, Bold Italic |
| StandardSymbolsPS | Symbol | Regular |
| D050000L | Dingbats | Regular |
| Z003 | ITC Zapf Chancery | Medium Italic |

The counterpart column identifies the corresponding PostScript design.
It does not give the installed name of the URW font.

## License

Select one of these licenses:

- [AGPL v3](COPYING), with the [font-embedding exemption](LICENSE.md#agpl-v3).
- [LPPL 1.3c](LICENSE.LPPL).
- [OFL 1.1](LICENSE.OFL), with no Reserved Font Names.

These are alternative licenses. You do not have to apply all three.
See [LICENSE.md](LICENSE.md) for the license information.
See [font sources and licensing](docs/provenance.md) for the URW++ authorization.

## Versions and old names

“Version 2.00” is the collection label for the 2016 release.
This repository also includes the later corrections.
The version inside an individual font can differ from the collection label.
Repository tags such as `v1.0.1` identify repository revisions, not font versions.

If a document uses an old font name, select the replacement:

| Old name | Replacement |
|---|---|
| `NimbusSans-Oblique` | `NimbusSans-Italic` |
| `NimbusSans-BoldOblique` | `NimbusSans-BoldItalic` |
| `NimbusSansNarrow-BdOblique` | `NimbusSansNarrow-BoldOblique` |

The [changelog](CHANGELOG.md) contains the full history and correction details.
The [original specimen](Core_35.pdf) is a historical document, not a current file list.

## Check the files

Install [uv](https://docs.astral.sh/uv/) to run the checks with their Python dependency.
Run the full test suite from the repository directory:

```bash
./test.sh
```

To check font parsing only, run:

```bash
uv run validate_fonts.py
```

To check the file hashes with `shasum`, run:

```bash
shasum -a 256 -c docs/fonts.sha256
```

The tests check all file hashes, the file list, font tables, glyph outlines,
and the corrected Cyrillic small letter te.
They also check failure handling for missing or damaged files.
[GitHub Actions](.github/workflows/validate.yml) runs the suite on pushes and pull requests.
These checks do not test font display in every application.
See [DEPENDENCIES.md](DEPENDENCIES.md) for the required tools.
