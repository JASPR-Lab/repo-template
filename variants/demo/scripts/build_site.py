"""Build the static site: copy pages/ into _site/.

Replace with your site generator's build command if you adopt one.
"""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "pages"
OUT = ROOT / "_site"


def main() -> None:
    """Rebuild _site/ from pages/."""
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT)
    if not (OUT / "index.html").exists():
        raise SystemExit("pages/index.html is missing")
    print(f"Built {sum(1 for p in OUT.rglob('*') if p.is_file())} files into {OUT.name}/")


if __name__ == "__main__":
    main()
