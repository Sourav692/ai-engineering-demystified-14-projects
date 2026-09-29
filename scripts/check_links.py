#!/usr/bin/env python3
"""Link and self-containment checks.

Run:  uv run python scripts/check_links.py
Exit 0 = all good; exit 1 = at least one failure.

Checks:
  1. every relative markdown link / image in .md files and notebook markdown
     cells resolves inside this repository
  2. no file points outside the repository: no absolute workstation paths, no
     `../` that climbs above the root, and no path into the old monorepo layout
     (the course used to live in one repository; each repo must now stand alone).
     README.md, CHANGELOG.md and docs/ may *name* the source monorepo for
     provenance, but may not link into its folders.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".venv", ".git", ".ipynb_checkpoints", "node_modules", "__pycache__"}
TEXT = {".md", ".py", ".ipynb", ".toml", ".yaml", ".yml", ".txt", ".json", ".cfg", ".ini"}
MD_LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
IMG_TAG = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"']", re.I)
MONOREPO = re.compile(
    r"(?<![\w-])0[1-6]_(?:Foundations|Core|Advanced|AI_Coding_Tools|Projects|Interview_Prep)/"
)
ABSOLUTE = re.compile(r"(?:/Users/[\w.-]+/|/home/[\w.-]+/|[A-Za-z]:\\\\?(?:Users|3\. Github))")
PROVENANCE_OK = {"README.md", "CHANGELOG.md"}

failures: list[str] = []


def files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and p.suffix in TEXT and not SKIP.intersection(p.relative_to(ROOT).parts)
    )


def markdown_of(p: Path) -> str:
    if p.suffix == ".md":
        return p.read_text(encoding="utf-8", errors="ignore")
    if p.suffix == ".ipynb":
        try:
            nb = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return ""
        return "\n".join(
            "".join(c.get("source", [])) for c in nb.get("cells", [])
            if c.get("cell_type") == "markdown"
        )
    return ""


def main() -> int:
    fs = files()
    for p in fs:
        rel = p.relative_to(ROOT).as_posix()
        md = markdown_of(p)
        for target in MD_LINK.findall(md) + IMG_TAG.findall(md):
            if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#)", target, re.I):
                continue
            path = urllib.parse.unquote(target.split("#")[0].split("?")[0])
            if not path:
                continue
            resolved = (p.parent / path).resolve()
            if ROOT.resolve() not in resolved.parents and resolved != ROOT.resolve():
                failures.append(f"{rel}: link leaves the repository -> {target}")
            elif not resolved.exists():
                failures.append(f"{rel}: broken link -> {target}")
        if rel == "scripts/check_links.py":
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        if ABSOLUTE.search(text):
            failures.append(f"{rel}: absolute workstation path -> {ABSOLUTE.search(text).group(0)}")
        m = MONOREPO.search(text)
        if m and not (rel in PROVENANCE_OK or rel.startswith("docs/")):
            failures.append(f"{rel}: path into the old monorepo layout -> {m.group(0)}")
    for f in failures:
        print(f"FAIL  {f}")
    print(f"{len(fs)} files checked, {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
