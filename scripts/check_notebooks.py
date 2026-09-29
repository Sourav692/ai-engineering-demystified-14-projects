#!/usr/bin/env python3
"""Structural checks for every notebook in this repository.

Run:  uv run python scripts/check_notebooks.py
Exit 0 = all good; exit 1 = at least one failure, each printed with its file.

Checks:
  1. valid nbformat-4 JSON with at least one cell
  2. the first markdown cell is a `# Title`
  3. outputs are cleared (notebooks ship clean; nbstripout enforces it on commit)
  4. every relative file path named in a code cell resolves, relative to the
     notebook's own folder (Jupyter's working directory) or the repository root
Paths a notebook *creates* rather than reads go in scripts/path_allowlist.txt,
one `notebook-relative-path :: literal :: reason` per line.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".venv", ".git", ".ipynb_checkpoints", "node_modules", "__pycache__"}
FILE_EXT = (
    "csv", "tsv", "json", "jsonl", "txt", "pdf", "png", "jpg", "jpeg", "gif", "svg",
    "md", "docx", "xlsx", "xls", "parquet", "db", "sqlite", "mp3", "wav", "mp4",
    "yaml", "yml", "html", "pkl", "faiss", "pptx", "zip", "ipynb", "py",
)
EXT_ALT = "|".join(FILE_EXT)
PATH_LITERAL = re.compile(
    r"""(?P<q>['"])(?P<p>(?:\.{1,2}/)?[\w .\-/]+\.(?:""" + EXT_ALT + r"""))(?P=q)"""
)

failures: list[str] = []


def notebooks() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.ipynb") if not SKIP.intersection(p.relative_to(ROOT).parts)
    )


def allowlist() -> set[tuple[str, str]]:
    f = ROOT / "scripts" / "path_allowlist.txt"
    out: set[tuple[str, str]] = set()
    if f.exists():
        for line in f.read_text().splitlines():
            if line.strip() and not line.startswith("#"):
                parts = [x.strip() for x in line.split("::")]
                if len(parts) >= 3 and parts[2]:
                    out.add((parts[0], parts[1]))
    return out


def main() -> int:
    allowed = allowlist()
    nbs = notebooks()
    for nb_path in nbs:
        rel = nb_path.relative_to(ROOT).as_posix()
        try:
            nb = json.loads(nb_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            failures.append(f"{rel}: invalid JSON ({e})")
            continue
        cells = nb.get("cells") or []
        if nb.get("nbformat") != 4 or not cells:
            failures.append(f"{rel}: not nbformat 4 or has no cells")
            continue
        md = [c for c in cells if c.get("cell_type") == "markdown"]
        first = "".join(md[0].get("source", [])).lstrip() if md else ""
        if not first.startswith("# "):
            failures.append(f"{rel}: first markdown cell is not a `# Title`")
        for c in cells:
            if c.get("cell_type") == "code" and (c.get("outputs") or c.get("execution_count")):
                failures.append(f"{rel}: has saved outputs (run nbstripout)")
                break
        for c in cells:
            if c.get("cell_type") != "code":
                continue
            src = "".join(c.get("source", []))
            for m in PATH_LITERAL.finditer(src):
                lit = m.group("p")
                if lit.startswith(("http", "/")) or (rel, lit) in allowed:
                    continue
                if not ((nb_path.parent / lit).exists() or (ROOT / lit).exists()):
                    failures.append(f"{rel}: path does not resolve -> {lit}")
    for f in failures:
        print(f"FAIL  {f}")
    print(f"{len(nbs)} notebooks checked, {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
