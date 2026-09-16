# Pre-publication checklist

Complete **before** making this repo public, submitting code as supplementary material,
or sharing it outside the author list. Open a PR that ticks these boxes, and get it
approved by the PI.

## Anonymization (for double-blind submission)

- [ ] No author names, usernames, emails, or institution names in code, comments, configs, notebooks, or commit messages of the anonymized copy
- [ ] Anonymized copy prepared separately (e.g. anonymous.4open.science); this repo is not linked from the submission
- [ ] No absolute paths revealing usernames or cluster hostnames

## Data and privacy

- [ ] Every dataset is listed in the README data provenance table
- [ ] Every dataset's license/terms permit the planned release
- [ ] No restricted, DUA-covered, or personal data in the repo **or its git history**
      (check with `git log --all --stat` or a history scanner, not just the current tree)
- [ ] IRB / DUA requirements for publication reviewed (if applicable)
- [ ] Released model weights / derived artifacts don't leak training data beyond what the terms allow

## Secrets

- [ ] No API keys, tokens, passwords, or private keys in the tree or history
- [ ] Any secret that was ever committed has been **rotated**, not just deleted

## Security-sensitive content

- [ ] Attack code / exploits reviewed for responsible-disclosure obligations
- [ ] Affected vendors notified and embargo respected (if applicable)

## Reproducibility

- [ ] Fresh clone + README setup instructions work on a clean machine
- [ ] Each paper table/figure maps to a command in the README
- [ ] Dependencies pinned (or a lockfile committed)
- [ ] Random seeds documented

## Metadata

- [ ] `CITATION.cff` has final title, authors, venue
- [ ] README links to paper and project page
- [ ] LICENSE year and holder are correct; license is compatible with dependencies and data
- [ ] PI approval recorded (PR approval or comment)
