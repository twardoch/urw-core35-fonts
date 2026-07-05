# Changelog

All notable changes to this archive. The fonts themselves are untouched — this
log tracks the scaffolding around them.

## [Unreleased]

### Added
- `.gitignore` covering macOS cruft (`.DS_Store`), generated snapshots
  (`llms.txt`), and Python/editor caches.
- `validate_fonts.py` — parses every `.otf`/`.ttf` with fontTools, reads the
  name and glyph tables, and fails loudly on any broken font.
- GitHub Actions workflow `validate-fonts` running that validator on each push
  and pull request.
- `docs/assets/icon.png` — a single-line concept illustration for the archive.

### Changed
- Rewrote `README.md`: added a family/style/format inventory table mapping each
  URW family to its classic counterpart, a clearer three-license breakdown with
  the AGPL embedding exemption spelled out, and validation instructions.

### Removed
- Untracked `.DS_Store` and the generated `llms.txt` snapshot from version
  control (now ignored).

## [1.0.0]

- Initial tagged archive of the URW Core 35 fonts, Version 2.00, in Type 1,
  OpenType-CFF, and OpenType-TrueType formats under the AGPL / LPPL / OFL triple
  license.
