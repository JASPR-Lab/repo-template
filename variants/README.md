# variants/

Overlays applied by `scripts/init_variant.py`. Each folder mirrors the repo root.
Its files are copied over the core skeleton, and then the script removes this folder.

| Variant | Adds / replaces | Removes |
|---|---|---|
| `paper` | `README.md` (data provenance), `docs/PREPUBLICATION_CHECKLIST.md`, `data/README.md` | none |
| `library` | `README.md`, `CHANGELOG.md`, `pyproject.toml` (packaging metadata), `.github/workflows/ci.yml` (coverage gate + build) | none |
| `demo` | `README.md`, `pages/`, `scripts/build_site.py`, `ruff.toml`, `.github/workflows/site.yml` | `src/`, `tests/`, `notebooks/`, `pyproject.toml`, `.github/workflows/ci.yml` |

**Maintaining the template:** change shared files in the core, not in the overlays.
Only put a file in an overlay if that variant genuinely needs it to differ.
To test locally, copy the repo somewhere temporary and run the script there.
