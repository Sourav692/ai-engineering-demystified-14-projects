# Chapter 6: Production — How Do I Ship It?

## Course context

Project 06 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 03 (LangChain fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-03-langchain-fundamentals), [repository 04 (LangGraph fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-04-langgraph-fundamentals), [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals), [repository 13 (production and observability)](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability).
- **What it integrates:** LangGraph workflows (including a human-approval step) behind an async FastAPI backend with an Angular frontend and PostgreSQL, node-level pytest with mocked LLMs, and two LangExtract Streamlit apps.
- **External services and expected cost:** OpenAI (backend workflows), Google Gemini (Streamlit apps); Postgres runs locally in Docker. Cents per session.
- **Tests / offline demo:** `unit_tests/` — pytest node tests with mocked LLMs (offline); Angular `*.spec.ts` files for the frontend.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
cp .env.example .env
cd fullstackapp && docker compose up      # backend :8000, frontend :5555, postgres :5433
cd unit_tests && pytest                   # mocked-LLM node tests
cd streamlit_apps/doc-entity-extractor && pip install -r requirements.txt && streamlit run app.py
```


> Deploy your agents as full-stack apps, test them, and build interactive UIs.

## What You'll Learn

- Build a **full-stack agent app** with FastAPI, Angular, and PostgreSQL
- Write **unit tests** for LangGraph nodes with pytest
- Ship **interactive Streamlit apps** for document analysis and knowledge graphs

## Prerequisites

- LangGraph and agent fundamentals: [repository 04 (LangGraph fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-04-langgraph-fundamentals) through [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals)
- Docker (for full-stack app)
- Google API key (for Streamlit apps)

## Content

### Full-Stack App (`fullstackapp/`)

A production application demonstrating human-in-the-loop agent workflows:

```
fullstackapp/
├── backend/            # FastAPI (async) + LangGraph workflows
│   └── workflows/      # Football stats, news, text generation, human approval
├── frontend/           # Angular UI
└── docker-compose.yml  # One-command deployment with PostgreSQL
```

```bash
cd fullstackapp
docker compose up
# Backend: http://localhost:8000 | Frontend: http://localhost:5555
```

### Unit Testing (`unit_tests/`)

Test LangGraph agents with pytest:

```bash
cd unit_tests
pytest
```

Covers: pytest fixtures, mocked LLMs, node-level testing, structured assertions.

### Streamlit Apps (`streamlit_apps/`)

| App | What It Does | Run With |
|---|---|---|
| `doc-entity-extractor/` | Extract entities from documents | `cd doc-entity-extractor && streamlit run app.py` |
| `knowledge-graphs-with-langextract/` | Build knowledge graphs from text | `cd knowledge-graphs-with-langextract && streamlit run app.py` |

## What's Next?

Deep agents and multi-agent systems with code execution are taught in [repository 08 (advanced agent systems)](https://github.com/Sourav692/ai-engineering-demystified-08-advanced-agent-systems).
