# 🤖 Agent Tool-Calling Loop — Demo Project

## Course context

Project 01 of **group 01 (foundational projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 01 (foundations)](https://github.com/Sourav692/ai-engineering-demystified-01-foundations), [repository 02 (prompt and context engineering)](https://github.com/Sourav692/ai-engineering-demystified-02-prompt-context-engineering), [repository 04 (LangGraph fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-04-langgraph-fundamentals), [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals).
- **What it integrates:** the single-agent loop (tool registry, routing, max-iteration guard, confirmation gate, retry, memoisation, fallback, tool-call logging) written twice: as a plain Python `while` loop and as a two-node LangGraph `StateGraph`.
- **External services and expected cost:** none for the core agent, the tests or the main notebook — the "brain" is a deterministic rule-based router. The optional real-LLM notebooks call OpenAI (`agent_tool_calling_demo_openai.ipynb`) or Anthropic (`langgraph_react_agent.ipynb`); a full run costs cents.
- **Tests / offline demo:** 12 offline pytest cases (`tests/test_agent.py`); the rule-based brain makes every run deterministic.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
uv sync                            # creates .venv from pyproject.toml / uv.lock
uv run pytest -q                   # 12 offline tests
uv run jupyter lab notebooks/
```


> **DevRev Technical Round · Section 3.** A minimal, DevRev-flavored **ReAct agent** that
> routes a query to tools, loops over observations, and synthesizes an answer — with a
> **max-iteration guard**, **confirmation gate**, **memoization**, **retry**, **fallback**,
> and full **observability**. Built **two ways**: from scratch *and* with **LangGraph**.

The prep note lists "tool-calling loop, coded from scratch" as a top-3 focus and says it
"maps directly to DevRev's AI-native agent product surface." This project is the study aid.

---

## Why two implementations?

| | `src/scratch_agent.py` | `src/langgraph_agent.py` |
|---|---|---|
| Dependencies | **none** (pure Python) | LangGraph |
| Purpose | prove you understand the **mechanics** (the interview ask) | show you can express it in the **framework the team uses** |
| The loop | an explicit `while` loop | a two-node `StateGraph` with a conditional edge |

Both share the *same* tools, brain, robustness, and observability modules — only the
orchestration differs.

---

## The loop in one picture

```
query ─▶ [ THINK: brain picks a tool or finishes ]
             │ tool call
             ▼
        [ ACT: execute_tool ]  ← confirmation gate · memo cache · retry
             │ result
             ▼
        [ OBSERVE ] ─▶ back to THINK   (until final answer or max-iteration guard)
```

---

## Run it

```bash
cd agent_tool_calling_demo
uv sync                                  # (the from-scratch agent needs nothing installed)

uv run pytest -q                          # 12 tests, all green
uv run python -c "import sys; sys.path.insert(0,'.'); \
  from src.tools import TicketStore, build_registry; \
  from src.scratch_agent import Agent; from src.robustness import always_approve; \
  print(Agent(build_registry(TicketStore()), confirm=always_approve).run('close the ticket about login').answer)"

uv run jupyter lab notebooks/agent_tool_calling_demo.ipynb   # the guided walkthrough
```

> **No API key needed.** The "brain" is a deterministic rule-based router
> (`src/brain.py`) that mimics an LLM's tool selection. To use a real LLM instead,
> implement the same `.decide()` contract — `make_llm_brain()` shows the wiring.

---

## Project layout

```
agent_tool_calling_demo/
├── README.md                 ← you are here
├── requirements.txt
├── src/
│   ├── tools.py              ← Tool + ToolRegistry + in-memory DevRev ticket backend
│   ├── brain.py              ← RuleBasedBrain (offline) + make_llm_brain() hook
│   ├── robustness.py         ← retry · memoization · fallback · confirmation gate · disambiguation
│   ├── observability.py      ← ToolCallLogger + trace table
│   ├── scratch_agent.py      ← the ReAct loop, coded from scratch  (+ Session for multi-turn state)
│   └── langgraph_agent.py    ← the same loop as a LangGraph StateGraph
├── notebooks/
│   └── agent_tool_calling_demo.ipynb   ← guided, runnable walkthrough of every concept
├── tests/
│   └── test_agent.py         ← 12 pytest cases
└── docs/
    └── DESIGN.md             ← state, observability, and parallel-vs-sequential tradeoffs
```

---

## What each interview bullet maps to

| Prep bullet (Section 3) | Where it lives |
|---|---|
| Minimal ReAct loop from a tool registry | `scratch_agent.Agent.run` + `tools.ToolRegistry` |
| Route a query to the right tool | `brain.RuleBasedBrain.decide` |
| Synthesize a final answer | the `decision.is_final` branch |
| Max-iteration guard | the `while iterations < self.max_iterations` guard |
| Tool error → retry / fallback / escalate | `robustness.execute_tool`, `with_fallback` |
| Memoize repeated calls | `robustness.execute_tool` (memo cache) + `Session.memo` |
| Disambiguate two plausible tools | `robustness.disambiguate` |
| Confirmation gate before destructive tools | `robustness` confirmation policy + `Tool.destructive` |
| State across turns | `scratch_agent.Session` |
| Logging/observability | `observability.ToolCallLogger` |

The theory behind this code is Handbook chapter 01 (`Handbook/01_LLM_Systems_Foundations/`) in the separate `Forward-Deployed-Engineer-Interview-Prep` repo — this project is its runnable lab, moved here 2026-09-29.
