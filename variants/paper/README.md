# Project Title

<!-- TODO: paper title, venue, and a one-paragraph summary. -->

**Paper:** _Title_ (Venue Year) · [arXiv/PDF link TODO] · [Project page TODO]

> ⚠️ **Pre-publication:** this repository is private. Do not share code, data, or
> results outside the author list until the checklist in
> [docs/PREPUBLICATION_CHECKLIST.md](docs/PREPUBLICATION_CHECKLIST.md) is complete.

## Setup

Requires Python 3.11+.

```sh
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Data provenance

Every dataset used in this project must be listed here **before** it is used in an experiment.

| Dataset | Source (URL / DOI / contact) | Version / date obtained | License / terms of use | Access level | Where it lives (not in git) | Contains personal data? |
|---|---|---|---|---|---|---|
| _example_ | _https://…_ | _v1.2, 2026-01-15_ | _CC-BY-4.0_ | _public / restricted / DUA_ | _cluster path or bucket, TODO_ | _no_ |

### Restricted data

- Restricted, licensed, or human-subjects data is **never** committed to this repo,
  pushed to any GitHub repo (public or private), or pasted into issues/PRs/notebooks.
- The `data/` folder is git-ignored except for `data/README.md`.
- Access follows the process in the
  [lab-handbook data access request](https://github.com/JASPR-Lab/lab-handbook/blob/main/access-requests/data-access.md).
- If the data is covered by a data use agreement (DUA) or IRB protocol, record the
  agreement/protocol ID in the table above and follow its terms for storage and deletion.

### Derived artifacts

| Artifact (model, features, cached results) | Derived from | Script that produces it | Shareable on release? |
|---|---|---|---|
| _example_ | _dataset above_ | _scripts/…_ | _yes/no_ |

## Reproducing results

| Paper table/figure | Command | Config | Expected runtime / hardware |
|---|---|---|---|
| _Table 1_ | `python scripts/… --config configs/…` | `configs/…` | _TODO_ |

## Repository layout

| Path | Contents |
|---|---|
| `src/project_name/` | Importable Python package |
| `scripts/` | Experiment, preprocessing, and plotting entry points |
| `configs/` | Experiment configs |
| `data/` | Local data (git-ignored; see `data/README.md`) |
| `tests/` | `pytest` tests |
| `docs/` | Notes, pre-publication checklist |
| `notebooks/` | Exploratory notebooks (outputs stripped on commit) |

## Citation

See [CITATION.cff](CITATION.cff). Update it with the final BibTeX after acceptance.

## License

MIT (see [LICENSE](LICENSE)). **Check that dataset and model licenses permit release before making this repo public.**
