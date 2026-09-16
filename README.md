# Project Title

> **Template repo notice:** if you are reading this in a freshly created repo, run
> `python3 scripts/init_variant.py <paper|library|demo> --name <python_package_name>`
> first. See [TEMPLATES.md](https://github.com/JASPR-Lab/.github/blob/main/TEMPLATES.md).

One-paragraph description of what this repository does.

## Setup

Requires Python 3.11+.

```sh
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Usage

```sh
# Example: python scripts/run.py --config configs/example.yaml
```

## Repository layout

| Path | Contents |
|---|---|
| `src/project_name/` | Importable Python package |
| `scripts/` | Entry-point scripts (experiments, preprocessing, plotting) |
| `configs/` | Experiment/config files |
| `tests/` | `pytest` tests |
| `docs/` | Longer-form documentation |
| `notebooks/` | Exploratory notebooks (outputs are stripped on commit) |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

See [CITATION.cff](CITATION.cff).

## License

MIT — see [LICENSE](LICENSE).
