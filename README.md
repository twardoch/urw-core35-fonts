# URW Core 35 Fonts, Version 2.00

The thirty-five typefaces that every PostScript printer has spoken since 1984 — Helvetica, Times, Courier, Palatino, Bookman, and the rest — redrawn by their original foundry and handed to you under a license you can actually use. No "evaluation" watermark. No per-seat fee. Just the fonts, in every format a modern toolchain asks for.

This is an archive of URW++'s Version 2.0 originals. Nothing here is a fork or a re-hint. These are the files as URW++ released them.

## What's in the box

Eleven families, 38 styles, in three formats each — Type 1 (`.t1` + `.afm`), OpenType-CFF (`.otf`), and OpenType-TrueType (`.ttf`). Every one parses cleanly (CI checks that on each push).

| URW family | Classic counterpart | Styles |
|---|---|---|
| NimbusSans | Helvetica | Regular, Italic, Oblique, Bold, Bold Italic, Bold Oblique |
| NimbusSansNarrow | Helvetica Narrow | Regular, Oblique, Bold, Bold Oblique, Bd Oblique |
| NimbusRoman | Times | Regular, Italic, Bold, Bold Italic |
| NimbusMonoPS | Courier | Regular, Italic, Bold, Bold Italic |
| URWGothic | ITC Avant Garde Gothic | Book, Book Oblique, Demi, Demi Oblique |
| URWBookman | ITC Bookman | Light, Light Italic, Demi, Demi Italic |
| P052 | Palatino | Roman, Italic, Bold, Bold Italic |
| C059 | Century Schoolbook | Roman, Italic, Bold, Bold Italic |
| StandardSymbolsPS | Symbol | Regular |
| D050000L | Dingbats | Regular |
| Z003 | ITC Zapf Chancery | Medium Italic |

The counterparts are the well-known metric-compatible equivalents; the names sit alongside them, they do not claim them.

## The history, briefly

In 1999–2000, URW++ Design and Development GmbH released the Type 1 implementations of the Core 35 fonts under the GNU General Public License (GPL) and the Aladdin Ghostscript Free Public License (AFPL). In 2009, URW++ additionally released the same fonts under the LaTeX Project Public License (LPPL).

In 2016, URW++ shipped Version 2.0 — an extensive reworking with improved outlines and greatly extended character sets, now including Cyrillic and Greek. Some font names changed in the process. Version 2.0 arrived in Type 1, OpenType-CFF, and OpenType-TTF, released under the GNU Affero General Public License, Version 3 (AGPL) with an exemption.

In 2017, URW++ additionally released the same Version 2.0 fonts under the LaTeX Project Public License (LPPL) Version 1.3c, and under the SIL Open Font License (OFL), Version 1.1, without a "Reserved Font Name" clause.

## License

You pick. The Version 2.0 fonts carry a triple license, and any one of the three applies at your choice:

- **AGPL v3** ([COPYING](./COPYING)) — with a font-embedding exemption: you may embed these fonts in a PostScript or PDF document regardless of the license on the document itself. See [LICENSE.md](./LICENSE.md) for the exact wording.
- **LPPL 1.3c** ([LICENSE.LPPL](./LICENSE.LPPL))
- **OFL 1.1** ([LICENSE.OFL](./LICENSE.OFL)) — no Reserved Font Name.

Copyright 2013, 2014, 2015 by (URW)++ Design & Development.

The three licenses apply to the original Version 2.0 fonts as released by URW++. If you extend or modify the fonts, you may release your changes under any combination of the three. Full text lives in [LICENSE.md](./LICENSE.md).

If you need extended or modified versions, or professional support, contact the [URW++ Font Service](https://www.urwpp.de/en/font-service/).

## Validating the archive

The fonts are the product, so the one thing worth checking is that they still open:

```bash
python validate_fonts.py
```

It parses every `.otf` and `.ttf`, reads the name and glyph tables, and exits non-zero if any font is broken. GitHub Actions runs it on every push (see [`.github/workflows/validate.yml`](./.github/workflows/validate.yml)).

## About URW++

URW++ has long developed and marketed font and software products, with particular strength in corporate type development and in the "global fonts" supplied to OEM customers. Its catalog reaches well beyond Latin — Cyrillic and Greek in the popular Latin designs, plus Japanese, Chinese, Korean, and Indic Devanagari families. URW++ is also the Dutch Type Library's exclusive distribution partner in Germany.

## Links

- [URW++ website](https://www.urwpp.de/en/)
- [URW++ Font Service](https://www.urwpp.de/en/font-service/)
- [URW++ film on type design & technology](https://youtu.be/Sadx3J7ybXw)
