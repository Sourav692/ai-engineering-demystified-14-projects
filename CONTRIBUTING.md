# Contributing

1. `uv sync` then `uv run pre-commit install` — the hooks strip notebook outputs and run the structural checks.
2. Each project stays self-contained: its own manifest, `.env.example` and README with a Course context section; never make one project import another. Keep every lesson inside the topic this repository owns. The boundary rules are listed under **Out of scope** in the README; content owned by a later repository goes there, not here.
3. Notebooks: first markdown cell is a `# Title`, outputs cleared, and any file a notebook reads sits inside this repository at a path relative to the notebook.
4. New sample data needs an entry in `docs/data-sources.md` (source, license, SHA-256).
5. Before opening a PR: `uv run pytest` must pass offline, with no API keys set, and the project's own tests (if it has them) must pass in its own environment.
