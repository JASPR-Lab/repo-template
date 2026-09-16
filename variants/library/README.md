# Project Title

<!-- TODO: one-paragraph description: what problem this library solves and which lab projects use it. -->

## Installation

Requires Python 3.11+.

```sh
# From GitHub (private repos need access + a token or SSH key)
pip install "project-name @ git+https://github.com/JASPR-Lab/project-name.git@v0.1.0"

# For development
git clone https://github.com/JASPR-Lab/project-name.git
cd project-name
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Quick start

```python
import project_name

print(project_name.__version__)
```

## Compatibility and versioning

- Follows [Semantic Versioning](https://semver.org/). Breaking changes bump the major version (or the minor version while `0.x`).
- Paper repos should **pin a tag** (`@v0.1.0`), not `main`, so published results stay reproducible.
- All changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Development

```sh
pre-commit run --all-files
pytest                      # CI requires >= 90% coverage
python -m build             # check the package builds
```

### Releasing

1. Update `version` in `pyproject.toml` and `__version__` in `src/project_name/__init__.py`.
2. Move `Unreleased` entries in `CHANGELOG.md` under the new version heading.
3. Merge to `main`, then tag: `git tag v0.1.0 && git push --tags`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

See [CITATION.cff](CITATION.cff).

## License

MIT (see [LICENSE](LICENSE)).
