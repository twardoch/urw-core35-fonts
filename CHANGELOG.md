---
this_file: CHANGELOG.md
---
# Changelog

This log records font releases, license changes, and repository changes.
It includes the earlier history and all commits in the two checked repositories.

- **This repository**: `twardoch/urw-core35-fonts`, through `84e183c`.
- **Artifex**: `ArtifexSoftware/urw-base35-fonts`, through `3c0ba3b`.
- **Historical sources**: the published announcements and the maintainer's dated correspondence.

Repository tags, such as `v1.0.0`, are not font version numbers.
“Version 2.00” identifies the 2016 font collection.
Individual font files can have different internal version numbers.

The history below uses release dates or original change dates where available.
The complete commit tables also show the Git commit dates.
Artifex imported some earlier history in August 2017. Those import dates are not original release dates.

## [Unreleased]

### 2026-10-30 — Current fonts and documentation

#### Added

- Added `docs/provenance.md` to explain the font sources and URW++ license authorization.
- Added `docs/fonts.sha256` with hashes for all 140 current files.
- Added five regression tests, the `test.sh` runner, and `DEPENDENCIES.md`.
- Added the complete history from both repositories to this changelog.

#### Changed

- Compared all font files with Artifex revision `3c0ba3b5687632dfc66526544a4e811fe0ec0cd9`.
  All 140 source files were already present and identical.
  The 2020 correction had reached this repository on 22 October 2020.
- Kept the current font files without changes to their bytes, names, or hints.
- Corrected the current file list to 35 styles and 140 files.
- Extended `validate_fonts.py` to read AFM and Type 1 files, as well as OTF and TTF files.
  It now decodes all OpenType tables and every glyph outline.
- Changed GitHub Actions to run the complete test suite.
- Rewrote the public documentation with short sentences and consistent technical terms.
  Removed the old company promotion text and obsolete service links.
- Added the former work log's results to this changelog.
  The separate work-log file is no longer used.
- Removed the update procedure from `docs/provenance.md`.
  That document now explains sources and license authorization.

#### Removed

Removed these old fonts in all four file formats: 12 files in total.

| Removed name | Current replacement |
|---|---|
| `NimbusSans-Oblique` | `NimbusSans-Italic` |
| `NimbusSans-BoldOblique` | `NimbusSans-BoldItalic` |
| `NimbusSansNarrow-BdOblique` | `NimbusSansNarrow-BoldOblique` |

The first two old fonts still contained the incorrect Cyrillic te widths.
The old Narrow files shared the current font's PostScript name, but their bytes differed.
Documents and applications that specify an old name must select its replacement.
Old files remain available in Git history.

#### Checks

- The original validator passed for 76 OTF and TTF files before the changes.
- The new tests first detected the 12 old files and the missing AFM and Type 1 checks.
  The Cyrillic te test passed before the changes because the corrected files were already present.
- All five tests passed with fontTools 4.68.0.
  They also passed with Python 3.12 and the minimum supported fontTools version, 4.50.0.
- Full parsing checked 105 font programs and 35 AFM files.
  The outline check decoded 85,982 glyphs.
- The tests checked the complete file list, all hashes, and the correction in all eight affected files.
  They also checked missing files, damaged files, and an empty directory.
- An independent byte comparison found 140 matches with Artifex, with no missing or extra files.
  All retained font files also matched the starting local revision.
- `shasum -a 256 -c docs/fonts.sha256` reported 140 successful checks.
- Ruff and its format check passed for both Python files.
  `git diff --check` passed.
- Local documentation links resolved. Public documents did not contain private email addresses or local user paths.
- Existing changes to `.gitignore` and the `.codegraph/` directory were preserved.

The checks ran locally. Native application display and hosted GitHub Actions were not tested.
The changes were not committed or pushed as part of this work.
The Internet Archive copy was unavailable during the check.
The account of the URW repository rename and closure is attributed to the maintainer.

## 2026-08-17 — CI branch support

Changed the validation workflow to run on both `main` and `master`.
The font files did not change. See local commit `84e183c` in the commit table.

## [1.0.1] — 2026-07-05

### Added

- Added `.gitignore` rules for macOS files, generated snapshots, and Python and editor caches.
- Added `validate_fonts.py` to read OTF and TTF name and glyph tables.
- Added the `validate-fonts` GitHub Actions workflow.
- Added the archive illustration at `docs/assets/icon.png`.
- Added this changelog.

### Changed

Rewrote the README with a family table, format information, license choices, and validation commands.
This was a repository update. It did not replace the fonts.

### Removed

A follow-up commit stopped tracking `.DS_Store` and the generated `llms.txt` file.
See local commits `147209e` and `c16d5e1`.

## 2026-03-29 — License explanation

Added the exact AGPL font-embedding exemption to `LICENSE.md`.
Clarified that users can select one of the three licenses.
The licenses are alternatives, not cumulative requirements. See local commit `85a07f2`.

## [1.0.0] — 2025-09-24

Created the first tagged repository revision.
The repository already contained the Version 2.00 collection and later corrections in Type 1, OTF, and TTF formats.
The AGPL, LPPL, and OFL choices were already present.

The tagged commit added `llms.txt` and changed `.DS_Store`.
It did not introduce a new font release. See local commit `068a350`.

Earlier maintenance commits added or changed `.DS_Store` on 28 July and 6 August 2025.
Those commits did not change fonts.

## 2023 — Artifex fontconfig correction

Removed inappropriate generic aliases for the D050000L symbol font.
The change was authored on 12 February and committed on 3 May.
It changed fontconfig data, not font files. See Artifex commit `3c0ba3b`.

## 2021–2022 — Artifex Century alias

Added the `Century` name to the C059 fontconfig aliases.
The change was authored on 3 November 2021 and committed on 22 February 2022.
It did not change the fonts. See Artifex commit `ae671b1`.

## 2020-10-22 — Current fonts imported here

Merged the `URWPP/Core_35` branch and imported the updated URW fonts.
The import changed 132 files. It included the 2017 updates and the 2020 Cyrillic correction.
Old files under three names remained beside the current files until the October 2026 cleanup.

A follow-up commit removed merge-conflict markers and duplicate text from the README and OFL file.
See local commits `f26e9ba`, `0c8defb`, and `6e1cf35`.

The current files confirm that this import included the 2020 correction.
This corrects the maintainer's earlier statement that the correction had not reached this repository.

## 2020-06-16 — URW++ Cyrillic te correction

Artifex imported replacement files from URW++ in commit `c151055`.
The commit credits URW++ and refers to
[issue 28](https://github.com/ArtifexSoftware/urw-base35-fonts/issues/28).
The affected faces are Nimbus Sans Italic and Bold Italic. Upright Bold did not change.

All four formats changed for each face: AFM, Type 1, OTF, and TTF.
The internal version changed from 1.00 to 1.10.
The correction changes the advance width of Cyrillic small letter te (`U+0442`, `afii10084`):

| Face | AFM / Type 1 / OTF width, 1000 units/em | TTF width, 2048 units/em |
|---|---|---|
| Nimbus Sans Italic | 833 → 374 | 1706 → 766 |
| Nimbus Sans Bold Italic | 889 → 409 | 1821 → 838 |

The replacement files also changed other glyph bounds and kerning.
The Italic AFM kerning-pair count changed from 3867 to 3870.
The Bold Italic count changed from 3820 to 3818.
Each face kept 855 glyphs in AFM, Type 1, and OTF, and 859 glyphs in TTF.

Artifex tag `20200910` points to this June commit.
The tag name is not the date when the correction was authored.
All eight files in this repository match these replacements.

## 2018 — Artifex system integration

- On 9 January, combined the Nimbus Sans Narrow and Nimbus Sans entries in fontconfig and AppStream.
  This did not combine or rename the font files.
- On 9 January, changed the recommended fontconfig file order to a number above 60.
- On 20 February, added a missing closing paragraph tag in AppStream data.
- On 28 February, corrected the collection description in AppStream data.
- On 27 March, corrected `Heroes` to `Heros` in a fontconfig mapping.
  That change was committed on 24 May and is the target of tag `20170801.1`.

## 2017 — Font corrections, repository setup, and license publication

### Font releases

- On 13 July, imported URW++'s 1 May release.
  It changed 132 files and addressed reported bugs 696582 and 697232.
- On 21 July, imported URW++'s 20 July release.
  It updated P052 Bold Italic and replaced Nimbus Sans Oblique and Bold Oblique with Italic and Bold Italic.
- On 1 August, imported URW++'s 27 July release.
  It added the missing blue hint zone at numeral tops in Nimbus Sans Regular and Italic.
- On 4 December, renamed all four `NimbusSansNarrow-BdOblique` files to `NimbusSansNarrow-BoldOblique`.
  This rename was committed on 5 December.

### Artifex repository and system integration

Artifex created the separate `urw-base35-fonts` repository on 17 August.
It first referenced the font source as a submodule.
It then imported the earlier font history and moved the fonts into `fonts/`.
It added license files, a README, fontconfig rules, and AppStream descriptions.

The fontconfig rules map PostScript names and other font names to the URW fonts.
They also provide mappings for older URW names.
The AppStream descriptions identify families, languages, releases, links, and related packages.

Later 2017 commits corrected metadata names, font mappings, and XML syntax.
They also separated the fallback rules into three files.
The complete Artifex table below records every change.
Tags `20170801_test` and `20170801` point to repository setup and metadata commits.

### URW++ authorization and publication

On 3 May, Jürgen Willrodt confirmed the new URW++ GitHub organization and its copy of this repository.
He also gave Adam Twardoch administrator access to make the license changes.

On 2 September, this repository added LPPL and OFL texts, the license explanation, and the original `Core_35.pdf` specimen.
It retained AGPL and its exemption in `COPYING` and `LICENSE.AGPL`.
The README explained the three license choices.
Six local commits record these changes across the branches later merged in 2020.
See [font sources and licensing](docs/provenance.md) for the authorization record.

## 2016 — OFL approval and Version 2.00

On 12 February, Twardoch asked URW++ to add OFL to the core fonts' licenses.
On 26 February, managing director Peter Rosenfeld approved the request.
These dates come from the maintainer's retained correspondence.

The June URW++ release was imported on 12 July.
It extended Greek and Cyrillic coverage from three families to the other applicable fonts.
The Version 2.00 collection included revised outlines and Type 1, OTF, and TTF files.
This repository's recorded license files provided AGPL v3 with the embedding exemption.

## 2015 — Character coverage and metrics

- On 4 February, imported the 22 January URW++ release.
  It added Greek and Cyrillic glyphs to Nimbus Mono, Nimbus Roman, and Nimbus Sans.
- On 17 June, replaced files to correct that character-set update.
- On 29 June, added Nimbus Sans L Bold, the last missing font from that update.
- On 24 August, recorded the 11 August release.
  It restored missing schwa glyphs and AFM kerning data.
  The original repository committed this change on 28 August.

Both repositories contain these changes under different commit identifiers.

## 2013-09-17 — Earlier URW releases in Git

Added the font license files, then imported URW releases 1.05 and 1.10.
The license files specified AGPL v3 with the font-embedding exemption.
Artifex later imported the font commits into its separate repository in August 2017.
The 2013 dates therefore describe the original changes, not the creation of that separate repository.

## 2009-06-22 — LPPL added to the original fonts

Peter Rosenfeld announced that the original 35 Type 1 fonts could also use LPPL version 1 or any later version.
The announcement applied to URW++'s original material, not to later additions by other parties.
It did not introduce new font files.

Jerzy Ludwichowski published the announcement with support from the TeX community.
See the [announcement in Die TeXnische Komödie 3/2009, pages 11–12](https://archiv.dante.de/DTK/PDF/komoedie_2009_3.pdf#page=11).
This event is separate from the later license publication for the Version 2.00 collection.

## 1996-05-14 — Original basic 35 fonts announced

L. Peter Deutsch announced the URW++ basic 35 Type 1 fonts under GPL.
The files included PFB outlines, AFM metrics, and PFM Windows printer metrics.
The announcement also described planned distribution under the Aladdin Ghostscript Free Public License.
See the [announcement preserved by TUG](https://tug.org/fonts/deutsch-urw.txt).

Earlier README text gave 1999–2000 as the original release period.
The dated 1996 announcement corrects that account.

## Former URW repository — dates not established

The maintainer reports that `URWPP/Core_35` became `URWTypeFoundry/Core_35` after the company changed its name.
He reports that the repository closed after Monotype acquired URW Type Foundry.
His account identifies an archive copy dated 4 September 2020.
It does not give exact dates for the rename or closure.
See [the source record](docs/provenance.md#the-former-urw-repository).

## Complete commit record

The tables cover all 24 local commits and all 55 Artifex commits available at the revisions stated above.
Each identifier links to its source commit. Descriptions summarize the recorded changes.
Dates use the commit's recorded time zone. “Author date” is the original change date in Git.
“Commit date” is the date when that commit was recorded, which can be later.
The current uncommitted changes are described under Unreleased.

### This repository

| Author date | Commit date | Commit | Change |
|---|---|---|---|
| 2013-09-17 | 2013-09-17 | [cba37ac](https://github.com/twardoch/urw-core35-fonts/commit/cba37acaac859d5d10278b5f6e02c190ca7054e3) | Added AGPL and the font-embedding exemption. |
| 2013-09-17 | 2013-09-17 | [0c95e26](https://github.com/twardoch/urw-core35-fonts/commit/0c95e26fe5c2a13fe5a113c7ed9791d3a3af0fa7) | Imported URW release 1.05. |
| 2013-09-17 | 2013-09-17 | [149a20b](https://github.com/twardoch/urw-core35-fonts/commit/149a20b9dd7cc2b416d91540355f3f6f50b9d2d6) | Imported URW release 1.10. |
| 2015-02-04 | 2015-02-04 | [8ddd6b3](https://github.com/twardoch/urw-core35-fonts/commit/8ddd6b336d95c43279efcc935cbe4180958b8a31) | Imported the 22 January 2015 release with Greek and Cyrillic additions. |
| 2015-06-17 | 2015-06-17 | [24de0b9](https://github.com/twardoch/urw-core35-fonts/commit/24de0b9eb8fdb96b2446fe24c17b537a947cec22) | Corrected the files for the Greek and Cyrillic additions. |
| 2015-06-29 | 2015-06-29 | [e5b3fce](https://github.com/twardoch/urw-core35-fonts/commit/e5b3fce0aadb091699b409be325468c682bd436d) | Added the missing Nimbus Sans L Bold update. |
| 2015-08-24 | 2015-08-28 | [c983ed4](https://github.com/twardoch/urw-core35-fonts/commit/c983ed400dc278dcf20bdff68252fad6d9db7af9) | Imported the 11 August release with schwa and kerning corrections. |
| 2016-07-12 | 2016-07-12 | [79bcdfb](https://github.com/twardoch/urw-core35-fonts/commit/79bcdfb34fbce12b592cce389fa7a19da6b5b018) | Imported the June 2016 base 35 release. |
| 2017-09-02 | 2017-09-02 | [a826500](https://github.com/twardoch/urw-core35-fonts/commit/a8265008f73e13a714450b3a448999aa9f3192ec) | Added three-license documentation, LPPL, OFL, and the specimen. Renamed LICENSE to LICENSE.AGPL. |
| 2017-09-02 | 2017-09-02 | [9171643](https://github.com/twardoch/urw-core35-fonts/commit/9171643071f5b023df0d5af49f6184a8382d2b2d) | Added the README on the other branch. |
| 2017-09-02 | 2017-09-02 | [3a03cc9](https://github.com/twardoch/urw-core35-fonts/commit/3a03cc968524d2ebb368278dafe57e6f19ad32dd) | Added the license explanation on the other branch. |
| 2017-09-02 | 2017-09-02 | [68062f2](https://github.com/twardoch/urw-core35-fonts/commit/68062f21a3209446254546a293f1d867decda69e) | Added LPPL, OFL, and the specimen on the other branch. |
| 2017-09-02 | 2017-09-02 | [72035a7](https://github.com/twardoch/urw-core35-fonts/commit/72035a76e4c26ac223e349e70e95728ce13895c0) | Revised README license links and format information. |
| 2017-09-02 | 2017-09-02 | [1b5267a](https://github.com/twardoch/urw-core35-fonts/commit/1b5267a9a14d8d5bcf261e067187e382df40c520) | Revised README structure and history. |
| 2020-10-22 | 2020-10-22 | [f26e9ba](https://github.com/twardoch/urw-core35-fonts/commit/f26e9ba646428548c7600668f073848bbcefd78f) | Merged the URWPP/Core_35 master branch. |
| 2020-10-22 | 2020-10-22 | [0c8defb](https://github.com/twardoch/urw-core35-fonts/commit/0c8defb9613bc089f31dc0dff35b153ab6e01090) | Imported the updated URW fonts, including the 2020 correction. |
| 2020-10-22 | 2020-10-22 | [6e1cf35](https://github.com/twardoch/urw-core35-fonts/commit/6e1cf35691d44e8fe9738dbaa11d8c05827474b6) | Removed merge-conflict markers and duplicate README and OFL text. |
| 2025-07-28 | 2025-07-28 | [733514b](https://github.com/twardoch/urw-core35-fonts/commit/733514bda9f593ed9c26184843e1c65d8d7db315) | Added a macOS .DS_Store file. |
| 2025-08-06 | 2025-08-06 | [4de30ff](https://github.com/twardoch/urw-core35-fonts/commit/4de30ffbdb7b60b79587705c85ef8ebcf2bd5d88) | Changed the macOS .DS_Store file. |
| 2025-09-24 | 2025-09-24 | [068a350](https://github.com/twardoch/urw-core35-fonts/commit/068a350f920352a9e3360dd86712e7b1b9e3f276) | Added llms.txt and changed .DS_Store. Tagged v1.0.0. |
| 2026-03-29 | 2026-03-29 | [85a07f2](https://github.com/twardoch/urw-core35-fonts/commit/85a07f255f7e47f495d4e9967b9a040194fcdd55) | Added the exemption text and clarified alternative license choices. |
| 2026-07-05 | 2026-07-05 | [147209e](https://github.com/twardoch/urw-core35-fonts/commit/147209e6b70f53d877c9358890f25de7007932af) | Added validation, CI, ignore rules, an icon, and this log. Revised the README. Tagged v1.0.1. |
| 2026-07-05 | 2026-07-05 | [c16d5e1](https://github.com/twardoch/urw-core35-fonts/commit/c16d5e187a2d59e3f5ec02f15b5e25a990f7f7ba) | Stopped tracking .DS_Store and llms.txt. |
| 2026-08-17 | 2026-08-17 | [84e183c](https://github.com/twardoch/urw-core35-fonts/commit/84e183c5fd17fba4846e6c2ee402bc2cc2f3e175) | Enabled CI for main and master. |

### Artifex repository

| Author date | Commit date | Commit | Change |
|---|---|---|---|
| 2017-08-17 | 2017-08-17 | [8426a29](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/8426a293a11424ed80e46f2c320ba2fcc0f908b5) | Created the repository with a font-source submodule and its configuration. |
| 2017-08-17 | 2017-08-17 | [9927f3c](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/9927f3ca634ebb2e02caecee9b4414218dc994e7) | Added AGPL and the font-embedding exemption. |
| 2013-09-17 | 2017-08-17 | [3f72fbb](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/3f72fbb89df49ec14687b822f2f9731393587382) | Imported the history of URW release 1.05. |
| 2013-09-17 | 2017-08-17 | [61424f9](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/61424f956ffff3e2d0d183f621a69d88aa45f571) | Imported the history of URW release 1.10. |
| 2015-02-04 | 2017-08-17 | [82d041c](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/82d041cc2cda8c452000672ec827efe4899e0323) | Imported the 22 January 2015 release with Greek and Cyrillic additions. |
| 2015-06-17 | 2017-08-17 | [d5947fe](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/d5947fe326d2a0344c9709100b1e2f8439500f42) | Corrected the files for the Greek and Cyrillic additions. |
| 2015-06-29 | 2017-08-17 | [116efaa](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/116efaa6d12cb2b88534ef21fcabe3d9cdcd690b) | Added the missing Nimbus Sans L Bold update. |
| 2015-08-24 | 2017-08-17 | [da390c5](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/da390c51a4df90a35554d16cc719580b76167e26) | Imported the 11 August release with schwa and kerning corrections. |
| 2016-07-12 | 2017-08-17 | [df72ea3](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/df72ea39b7e51ee2ba774b5a2dd7c80fc1b62f84) | Imported the June 2016 base 35 release. |
| 2017-07-13 | 2017-08-17 | [6dc10b9](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/6dc10b9ec897ff40875bb55d62007268e3b2cad2) | Imported the 1 May 2017 release. Addressed bugs 696582 and 697232. |
| 2017-07-21 | 2017-08-17 | [b6bc4fe](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/b6bc4fe7c17dcd8cf32636a73a2f27337fcb2e63) | Imported the 20 July release. Replaced Nimbus Sans Oblique names with Italic names and updated P052 Bold Italic. |
| 2017-08-01 | 2017-08-17 | [8c44be1](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/8c44be14edc4a0d2fb906f0751f1e6653ffbf6c2) | Imported the 27 July release. Added numeral hint zones in Nimbus Sans Regular and Italic. |
| 2017-08-17 | 2017-08-17 | [c1e3ec2](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/c1e3ec2886de92b8898f90e4dad9926549bb28a5) | Moved imported files into fonts/ and reorganized the repository. |
| 2017-08-17 | 2017-08-17 | [e4fb67e](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/e4fb67e639f51bf9a66d048b919d298dce2b6385) | Added directories for system integration data. |
| 2017-08-17 | 2017-08-17 | [b16444f](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/b16444f8910736aa45e833a2ad38362f73afb888) | Removed a temporary fontconfig file. |
| 2017-07-27 | 2017-08-17 | [1af6faa](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/1af6faaa1d9f09c612893502a11d428af056c469) | Added basic fontconfig rules. |
| 2017-08-01 | 2017-08-17 | [43f78df](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/43f78df5d4573e1c93c76dce07838ba448039e3e) | Added fontconfig substitutions for PostScript, GUST, Windows, and Google fonts. |
| 2017-08-01 | 2017-08-17 | [3cb4ad4](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/3cb4ad41226f1f672eaeaee2bc2089e7b807a64a) | Added fontconfig substitutions for older URW names. |
| 2017-08-17 | 2017-08-17 | [7a911f4](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/7a911f4698d196a24326577723155ddad6fe5b78) | Removed a temporary AppStream file. |
| 2017-08-08 | 2017-08-17 | [2c06b4d](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/2c06b4d6360912b6393b4f99d89362b48a5d2d74) | Added initial AppStream descriptions. |
| 2017-08-15 | 2017-08-17 | [3d936c1](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/3d936c1450a7a99d2250f1a8de4e7bcf5f3d6e02) | Added AppStream homepage and issue-report links. |
| 2017-08-15 | 2017-08-17 | [5d9815a](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/5d9815a200d6bc0c5868d18707ec4140bac3b295) | Added supported languages to AppStream descriptions. |
| 2017-08-15 | 2017-08-17 | [329b502](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/329b502c5e7f46ad85324bbf5458bea513c30cfd) | Added the AppStream developer name. |
| 2017-08-15 | 2017-08-17 | [b16c095](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/b16c09536346c1d188bb2d4b835a6b835a0e812b) | Added AppStream related-package suggestions. |
| 2017-08-15 | 2017-08-17 | [e82dca4](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/e82dca4fbd80491c0de25836195eb8d914802687) | Added the AppStream update-contact field. |
| 2017-08-16 | 2017-08-17 | [a20f733](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/a20f733273846b3f9b6d1ac5bf9e8bcb7359beb8) | Added the latest official release to AppStream data. |
| 2017-08-16 | 2017-08-17 | [8eb80bd](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/8eb80bdf256553317d615b2a14e4ec59e45d3f0e) | Added AppStream data for installation of all 35 fonts. |
| 2017-08-16 | 2017-08-17 | [5ee329a](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/5ee329afa32582132578a129ae54aebf87026c50) | Added the AppStream collection suggestion. |
| 2017-08-17 | 2017-08-17 | [8d94454](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/8d944545e990ea6af5624fd6d492ebd8f7776c85) | Added the AppStream release entry for version 20170801. |
| 2017-08-17 | 2017-08-17 | [99f4a57](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/99f4a5798a93d0ac5dd45c0a8b82d8b33b36cf95) | Removed the unused .gitmodules file. |
| 2017-08-17 | 2017-08-17 | [c2f460c](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/c2f460c4775883fbdae01594af0349e509216670) | Added the repository README. Target of tag 20170801_test. |
| 2017-08-18 | 2017-08-18 | [2ada73b](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/2ada73b87c8d2741655fcb7e5d00bdc1b1300fca) | Renamed AppStream files to match their reverse-DNS identifiers. |
| 2017-08-22 | 2017-08-22 | [7f09f1c](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/7f09f1c92ae713400af6d11c9321a3d741f30821) | Renamed configuration files to follow fontconfig conventions. |
| 2017-08-23 | 2017-08-25 | [a7ca016](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/a7ca016d800824213351d3b5360d2c47a1e03e8f) | Mapped Nimbus Sans Narrow to Helvetica Narrow instead of Helvetica Condensed. |
| 2017-08-23 | 2017-08-25 | [3c9f664](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/3c9f6645ceae4e0f1857fae40c713eee9e91e44e) | Added another substitution for Standard Symbols PS. |
| 2017-08-23 | 2017-08-25 | [ee8966f](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/ee8966f29fcc9afe809180593b6fcd59e4abb77e) | Added mappings to the original PostScript font names. |
| 2017-08-24 | 2017-08-25 | [99580c0](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/99580c01c04cb1f0928fae1147e82658e7225eed) | Reordered and reformatted fontconfig substitutions. |
| 2017-08-24 | 2017-08-25 | [93b54fe](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/93b54fe27924329aeb368130f34b9cae78a818ee) | Added a fallback configuration for older font names. |
| 2017-08-24 | 2017-08-25 | [6684afb](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/6684afb27c15c93102b5b276bc0f7001947e1101) | Moved fallback rules into their own file and added Nimbus Mono fallback. |
| 2017-08-25 | 2017-08-25 | [273399f](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/273399f6ef2d099ff4847b5de45b7e01f25fe350) | Added the fontconfig README. |
| 2017-08-28 | 2017-08-29 | [3edb6ec](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/3edb6ecbef4af24ce4723c24f317c2e8409c6cd2) | Changed the repository README to Markdown and corrected text. |
| 2017-08-28 | 2017-08-29 | [fae83cf](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/fae83cfc21d30ff55be2152e406f852862386692) | Changed the fontconfig README to Markdown and corrected text. |
| 2017-08-28 | 2017-08-29 | [b1605de](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/b1605de3323b42ca3fae7aea3bf2dd72aa2cd490) | Added the AppStream README. |
| 2017-09-22 | 2017-09-22 | [c3cc161](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/c3cc161864186cfab937a2b4eb998009f803e22d) | Added the urw- prefix to fontconfig filenames. Target of tag 20170801. |
| 2017-09-25 | 2017-09-25 | [70aaae7](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/70aaae73a0dba9c94c001bfc464b6cb6d1f3d0f9) | Separated fallback configuration into three files. |
| 2017-10-02 | 2017-10-02 | [766d777](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/766d77767fc912742f3e7236f083e2de8fdfc0e9) | Corrected AppStream field names and XML comments. |
| 2017-12-04 | 2017-12-05 | [15193de](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/15193de2d6e421af88f9a3297833530b60c40a09) | Renamed NimbusSansNarrow-BdOblique files to NimbusSansNarrow-BoldOblique. |
| 2018-01-09 | 2018-01-09 | [965bea8](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/965bea8798ffe76885e4ea4556155a6df5e7fc4d) | Combined Nimbus Sans Narrow and Nimbus Sans integration entries. |
| 2018-01-09 | 2018-01-09 | [6a60234](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/6a60234ea6eb3cc30f70234c047eb7431e3ccee6) | Recommended a fontconfig order number above 60. |
| 2018-02-20 | 2018-02-20 | [d11c5ea](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/d11c5ea1d74846f3652b1b8ae14a09a724f99ee9) | Added a missing closing paragraph tag in AppStream data. |
| 2018-02-28 | 2018-02-28 | [65962e2](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/65962e27febc3883a17e651cdb23e783668c996f) | Corrected the AppStream collection description. |
| 2018-03-27 | 2018-05-24 | [b758567](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/b758567463df532414c520cf008e27d9448b55a4) | Corrected Heroes to Heros in a font mapping. Target of tag 20170801.1. |
| 2020-06-16 | 2020-06-16 | [c151055](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/c15105598aa7eb256b1ebfcecd3d078801521e73) | Imported the URW++ Cyrillic te correction. Target of tag 20200910. |
| 2021-11-03 | 2022-02-22 | [ae671b1](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/ae671b1b1f4219b090628f259b994eada336d965) | Added the Century alias for C059. |
| 2023-02-12 | 2023-05-03 | [3c0ba3b](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/3c0ba3b5687632dfc66526544a4e811fe0ec0cd9) | Removed inappropriate generic aliases for D050000L. |
