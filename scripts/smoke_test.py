#!/usr/bin/env python3
"""Offline smoke test: no API keys, no network, no paid calls.

Run:  uv run python scripts/smoke_test.py   (also run by `uv run pytest`)

1. every Python file in the repository compiles
2. the local `helpers` package imports, when this repository ships one
3. the notebook and link checks pass
"""
from __future__ import annotations

import importlib.util
import py_compile
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".venv", ".git", ".ipynb_checkpoints", "node_modules", "__pycache__"}


def main() -> int:
    bad = []
    for p in sorted(ROOT.rglob("*.py")):
        if SKIP.intersection(p.relative_to(ROOT).parts):
            continue
        try:
            py_compile.compile(str(p), doraise=True, cfile=None)
        except py_compile.PyCompileError as e:
            bad.append(f"{p.relative_to(ROOT)}: {e.msg.strip().splitlines()[-1]}")
    for b in bad:
        print(f"FAIL  does not compile: {b}")

    if (ROOT / "src" / "helpers").is_dir() and importlib.util.find_spec("helpers") is None:
        bad.append("helpers")
        print("FAIL  src/helpers exists but is not importable - run `uv sync`")

    for script in ("check_notebooks.py", "check_links.py"):
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / script)])
        if r.returncode:
            bad.append(script)
    print("smoke test:", "FAILED" if bad else "passed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
