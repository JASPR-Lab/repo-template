#!/usr/bin/env python3
"""Apply a repo-template variant to a freshly created repository.

Run once, right after creating a repo from JASPR-Lab/repo-template:

    python3 scripts/init_variant.py paper --name my_package
    python3 scripts/init_variant.py library --name my_package
    python3 scripts/init_variant.py demo

What it does:
  1. Copies files from variants/<variant>/ over the core skeleton.
  2. Removes core files the variant doesn't use (e.g. demo drops src/ and tests/).
  3. Renames the placeholder package `project_name` / `project-name` to --name.
  4. Deletes variants/ and this script.

Review the result with `git status` and `git diff` before committing.
Standard library only; works on Python 3.8+.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARIANTS_DIR = ROOT / "variants"
PLACEHOLDER_PKG = "project_name"
PLACEHOLDER_DIST = "project-name"
PLACEHOLDER_TITLE = "Project Title"

# Core paths each variant removes, relative to the repo root.
REMOVE = {
    "paper": [],
    "library": [],
    "demo": ["src", "tests", "notebooks", "pyproject.toml", ".github/workflows/ci.yml"],
}

TEXT_SUFFIXES = {".md", ".py", ".toml", ".cff", ".yml", ".yaml", ".cfg", ".txt", ".html"}
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "variants"}


def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def copy_overlay(variant: str) -> None:
    src_root = VARIANTS_DIR / variant
    for src in sorted(src_root.rglob("*")):
        if src.is_dir():
            continue
        dest = ROOT / src.relative_to(src_root)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        print(f"  write  {dest.relative_to(ROOT)}")


def remove_paths(variant: str) -> None:
    for rel in REMOVE[variant]:
        path = ROOT / rel
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()
        else:
            continue
        print(f"  remove {rel}")


def iter_text_files():
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file() and (path.suffix in TEXT_SUFFIXES or path.name == "CODEOWNERS"):
            yield path


def rename_package(pkg: str, title: str) -> None:
    dist = pkg.replace("_", "-")
    old_dir = ROOT / "src" / PLACEHOLDER_PKG
    if old_dir.is_dir() and pkg != PLACEHOLDER_PKG:
        old_dir.rename(ROOT / "src" / pkg)
        print(f"  rename src/{PLACEHOLDER_PKG} -> src/{pkg}")
    for path in iter_text_files():
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        new = (
            text.replace(PLACEHOLDER_PKG, pkg)
            .replace(PLACEHOLDER_DIST, dist)
            .replace(PLACEHOLDER_TITLE, title)
        )
        if path.name == "pyproject.toml":
            new = new.replace('extend-exclude = ["variants"]\n', "")
        if new != text:
            path.write_text(new, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("variant", choices=sorted(REMOVE))
    parser.add_argument(
        "--name",
        help="Python package name (snake_case). Defaults to the repo folder name.",
    )
    args = parser.parse_args()

    if not VARIANTS_DIR.is_dir():
        die("variants/ not found; this repo has already been initialized.")

    pkg = args.name or ROOT.name.replace("-", "_").lower()
    if not re.fullmatch(r"[a-z][a-z0-9_]*", pkg):
        die(f"--name must be a snake_case Python identifier, got {pkg!r}")
    title = ROOT.name

    print(f"Applying '{args.variant}' variant (package: {pkg})")
    copy_overlay(args.variant)
    remove_paths(args.variant)
    rename_package(pkg, title)

    shutil.rmtree(VARIANTS_DIR)
    print("  remove variants/")
    Path(__file__).unlink()
    print(f"  remove scripts/{Path(__file__).name}")

    print(
        "\nDone. Next:\n"
        "  1. Replace placeholder usernames in .github/CODEOWNERS\n"
        "  2. Fill in TODOs in README.md and CITATION.cff\n"
        "  3. git status && git diff, then commit"
    )


if __name__ == "__main__":
    main()
