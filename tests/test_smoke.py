"""Offline smoke tests. `uv run pytest` must pass on a clean clone with no API keys."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _run(script: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script)], capture_output=True, text=True
    )


def test_notebooks_are_structurally_valid():
    r = _run("check_notebooks.py")
    assert r.returncode == 0, r.stdout


def test_links_resolve_and_repo_is_self_contained():
    r = _run("check_links.py")
    assert r.returncode == 0, r.stdout


def test_smoke():
    r = _run("smoke_test.py")
    assert r.returncode == 0, r.stdout
