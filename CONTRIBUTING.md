# Contributing

This repo follows the JASPR Lab conventions in the
[lab-handbook](https://github.com/JASPR-Lab/lab-handbook). The short version:

## Workflow

1. Branch from `main`: `git checkout -b <your-name>/<short-description>`.
2. Make small, focused commits.
3. Run checks locally before pushing:
   ```sh
   pre-commit run --all-files
   pytest
   ```
4. Open a pull request and fill in the PR template checklist.
5. Request a review from a CODEOWNER (see `.github/CODEOWNERS`). Wait for one approval before merging.
6. Squash-merge and delete the branch.

See [Git workflow](https://github.com/JASPR-Lab/lab-handbook/blob/main/conventions/git-workflow.md)
and [Code review](https://github.com/JASPR-Lab/lab-handbook/blob/main/conventions/code-review.md).

> **Note:** under our current GitHub Free plan, review approval and CODEOWNERS review
> are **not technically enforced** on private repos. They are lab conventions, so please
> follow them anyway.

## Code style

- Formatting and linting: `ruff` (configured in `pyproject.toml`, run by pre-commit and CI).
- Type hints on public functions.
- Details: [Code style](https://github.com/JASPR-Lab/lab-handbook/blob/main/conventions/code-style.md).

## Data and secrets

- **Never commit** datasets, model weights, credentials, API keys, or personal data.
- Notebook outputs are stripped automatically on commit.
- Details: [Data handling](https://github.com/JASPR-Lab/lab-handbook/blob/main/conventions/data-handling.md).
