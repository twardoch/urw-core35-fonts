---
this_file: docs/provenance.md
---
# Font sources and licensing

URW++ made the fonts. Artifex distributed the font files and later corrections.
Adam Twardoch arranged the additional licenses with permission from URW++.
This repository provides those fonts with the three license choices in
[LICENSE.md](../LICENSE.md).

## Source of the current files

All 140 files match Artifex revision
[`3c0ba3b5687632dfc66526544a4e811fe0ec0cd9`](https://github.com/ArtifexSoftware/urw-base35-fonts/tree/3c0ba3b5687632dfc66526544a4e811fe0ec0cd9/fonts).
The byte comparison was completed on 30 October 2026.
The [SHA-256 file list](fonts.sha256) records the expected hashes.

This repository imported the corrected files on 22 October 2020.
The latest font change in the selected Artifex history is the June 2020 correction.
Later Artifex commits change system integration files, not the font programs.
This repository does not include Artifex's fontconfig or AppStream files.

The collection label is “Version 2.00”.
Individual fonts and repository tags use separate version numbers.
See the [README](../README.md#versions-and-old-names) for old names and replacements.
See the [changelog](../CHANGELOG.md) for the complete history from both repositories.

## Permission for the additional licenses

The following account uses the maintainer's explanation and dated correspondence.
The public documents do not reproduce private email addresses or complete messages.

- Twardoch created this repository from files that Artifex had published.
- On 12 February 2016, he asked URW++ to add the SIL Open Font License.
- On 26 February 2016, managing director Peter Rosenfeld approved the request.
- On 3 May 2017, technical director Jürgen Willrodt confirmed the URW++ GitHub organization and its repository copy.
- Willrodt gave Twardoch administrator access to make the license changes.
- On 2 September 2017, the repository commits recorded AGPL, LPPL and OFL as alternative licenses.

Artifex's own [license notice](https://github.com/ArtifexSoftware/urw-base35-fonts/blob/3c0ba3b5687632dfc66526544a4e811fe0ec0cd9/LICENSE)
uses AGPL with the embedding exemption.
The additional choices here come from the separate URW++ authorization.
The [2020 correction commit](https://github.com/ArtifexSoftware/urw-base35-fonts/commit/c15105598aa7eb256b1ebfcecd3d078801521e73)
credits URW++ as the source of the update.

## The former URW repository

According to Twardoch, URW++ made its repository as a copy of this repository.
The name changed from `URWPP/Core_35` to `URWTypeFoundry/Core_35` after the company changed its name.
Twardoch reports that the repository closed after Monotype acquired URW Type Foundry.
The supplied account gives no exact dates for the rename or closure.

The account identifies a
[4 September 2020 archive copy](https://web.archive.org/web/20200904172916/https://github.com/URWTypeFoundry/Core_35/).
That copy was not accessible during the October 2026 check.
The rename and closure account therefore remains attributed to the maintainer.
The available Git history separately records a merge from `URWPP/Core_35` on 22 October 2020.
