# Changelog

All notable changes to `ceblpy` are documented here.

## v1.0.0 (2026-09-04)

### Changes

- Import directly from `ceblpy`. `from ceblpy.ceblpy import load_cebl_schedule`
  becomes `from ceblpy import load_cebl_schedule`.
- `load_cebl_coaches()` has been removed. Coaches are now columns on
  `load_cebl_team_boxscore()`.
- Column names have changed across all five datasets. See the
  [data dictionary](https://ryanndu.github.io/ceblpy/data-dictionary/) for
  every column and what it means.
- Requires Python 3.11 or later.
- Documentation has moved to
  [ryanndu.github.io/ceblpy](https://ryanndu.github.io/ceblpy/), built with
  Zensical.
- The project now uses uv and `pyproject.toml` for dependency management.

## v0.1.1 (2025-07-29)

- Fixed typo in project description
- Added link to hosted documentation

## v0.1.0 (2025-07-02)

- First release of `ceblpy`!