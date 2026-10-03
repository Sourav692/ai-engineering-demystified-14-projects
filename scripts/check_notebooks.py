#!/usr/bin/env python3
"""Structural checks for every notebook in this repository.

Run:  uv run python scripts/check_notebooks.py
Exit 0 = all good; exit 1 = at least one failure, each printed with its file.

Checks:
  1. valid nbformat-4 JSON with at least one cell
  2. the first markdown cell is a `# Title`
  3. saved outputs, when present, come from one clean top-to-bottom run: execution counts
     1..n in cell order, no error outputs, no workstation paths, notebook <= 2 MB
  4. no key-like strings (API keys, tokens) anywhere in the notebook
  5. every relative file path named in a code cell resolves, relative to the
     notebook's own folder (Jupyter's working directory) or the repository root
Tracked notebooks are judged by their staged (index) copy - what a commit would ship -
so a local run in progress never fails the check; untracked notebooks are read from disk.
Paths a notebook *creates* rather than reads go in scripts/path_allowlist.txt,
one `notebook-relative-path :: literal :: reason` per line.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# .tracker is the local, git-ignored cleanup tracker
SKIP = {".venv", ".git", ".ipynb_checkpoints", "node_modules", "__pycache__", ".tracker"}
FILE_EXT = (
    "csv", "tsv", "json", "jsonl", "txt", "pdf", "png", "jpg", "jpeg", "gif", "svg",
    "md", "docx", "xlsx", "xls", "parquet", "db", "sqlite", "mp3", "wav", "mp4",
    "yaml", "yml", "html", "pkl", "faiss", "pptx", "zip", "ipynb", "py",
)
EXT_ALT = "|".join(FILE_EXT)
PATH_LITERAL = re.compile(
    r"""(?P<q>['"])(?P<p>(?:\.{1,2}/)?[\w .\-/]+\.(?:""" + EXT_ALT + r"""))(?P=q)"""
)

MAX_BYTES = 2 * 1024 * 1024
# Anchored so URL slugs such as ".../elon-musk-backs-..." don't match the `sk-` prefix.
KEY_LIKE = re.compile(
    r"(?<![\w-])(?:sk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}|gsk_[A-Za-z0-9]{20,}|pcsk_[A-Za-z0-9_]{20,}"
    r"|dapi[0-9a-f]{32}|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{30,}|hf_[A-Za-z0-9]{30,}"
    r"|AIza[0-9A-Za-z_-]{35}|xox[abprs]-[A-Za-z0-9-]{10,}|lsv2_[A-Za-z0-9_]{20,})"
)
WORKSTATION_PATH = re.compile(r"(?:/Users/|/home/)[A-Za-z0-9._-]+/|[A-Za-z]:\\{1,2}Users\\{1,2}")

failures: list[str] = []


def staged_texts(paths: list[Path]) -> dict[Path, str]:
    """Index copy of every tracked notebook, read in one `git cat-file --batch` call."""
    rels = [p.relative_to(ROOT).as_posix() for p in paths]
    try:
        r = subprocess.run(["git", "ls-files", "-s", "--", *rels], cwd=ROOT,
                           capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return {}
    blobs = {}
    for line in r.stdout.splitlines():
        meta, rel = line.split("\t", 1)
        blobs[rel] = meta.split()[1]
    if not blobs:
        return {}
    order = list(blobs)
    out = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT, check=True, capture_output=True,
                         input="".join(blobs[rel] + "\n" for rel in order).encode()).stdout
    texts, pos = {}, 0
    for rel in order:
        header_end = out.index(b"\n", pos)
        size = int(out[pos:header_end].split()[2])
        body = out[header_end + 1: header_end + 1 + size]
        texts[ROOT / rel] = body.decode("utf-8", "replace")
        pos = header_end + 1 + size + 1
    return texts


def check_outputs(rel: str, nb: dict, size: int) -> None:
    code = [c for c in nb["cells"] if c.get("cell_type") == "code"]
    counts = [c.get("execution_count") for c in code if c.get("execution_count") is not None]
    has_outputs = any(c.get("outputs") for c in code)
    if not counts and not has_outputs:
        return  # not executed: nothing to judge
    if size > MAX_BYTES:
        failures.append(f"{rel}: {size / 1e6:.1f} MB with outputs (limit 2 MB) - trim them")
    if counts != list(range(1, len(counts) + 1)):
        failures.append(f"{rel}: execution counts {counts[:8]}... are not 1..n in order - "
                        "commit outputs from one clean top-to-bottom run")
    for i, c in enumerate(code):
        for o in c.get("outputs", []):
            if o.get("output_type") == "error":
                failures.append(f"{rel}: code cell {i} has an error output ({o.get('ename')})")
            blob = json.dumps(o, ensure_ascii=False)
            m = WORKSTATION_PATH.search(blob)
            if m:
                failures.append(
                    f"{rel}: code cell {i} output contains a workstation path ({m.group(0)}...)"
                )


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
    staged = staged_texts(nbs)
    for nb_path in nbs:
        rel = nb_path.relative_to(ROOT).as_posix()
        try:
            text = staged.get(nb_path)
            if text is None:
                text = nb_path.read_text(encoding="utf-8")
            nb = json.loads(text)
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
        check_outputs(rel, nb, len(text.encode("utf-8")))
        if KEY_LIKE.search(text):
            failures.append(f"{rel}: contains a key-like string - remove it and rotate the key")
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
