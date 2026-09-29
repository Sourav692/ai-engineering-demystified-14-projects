# Deep Agent — Memory Command Center

## Course context

Project 07 of **group 03 (enterprise and realtime capstones)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 04 (LangGraph fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-04-langgraph-fundamentals), [repository 08 (advanced agent systems)](https://github.com/Sourav692/ai-engineering-demystified-08-advanced-agent-systems), [repository 13 (production and observability)](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability).
- **What it integrates:** the deep-agent orchestrator from repository 08 (eight skill-driven subagents: memory, coding, review, research, four Genie analytics agents) with Lakebase long-term memory, a LangGraph checkpointer, SSE streaming, a React UI and a Databricks Apps deployment.
- **External services and expected cost:** Databricks (model serving, Lakebase Postgres, Genie spaces, Unity Catalog volumes) and Tavily search; Databricks Apps compute bills by uptime.
- **Tests / offline demo:** no tests.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn deep_agent.main:app --app-dir backend/src --port 8000   # the command app.yaml and the Dockerfile run
cd frontend && npm install && npm run dev
# or: docker compose up
```

The subagents load their instructions from `skills/` at runtime; those SKILL.md files are copied here from repository 08 so the app is self-contained. The Databricks bundle and CI workflow mentioned in `app.yaml` and below lived at the source repository's root and are not part of this project.


A React + FastAPI web application for the Deep Agent multi-agent orchestrator with long-term memory backed by Databricks SQL (Unity Catalog).

## Architecture

```
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────┐
│  React Frontend  │     │   FastAPI Backend     │     │  Databricks      │
│                  │     │                       │     │                  │
│  Thread Sidebar  │────>│  POST /api/chat (SSE) │────>│  Claude Opus 4.6 │
│  Chat Area       │     │  GET  /api/memories   │────>│  Unity Catalog   │
│  Memory Panel    │     │  POST /api/threads    │────>│  Genie Spaces    │
│  Agent Topology  │     │  GET  /api/threads/:id│────>│  SQL Warehouse   │
│  Toast Notifs    │     │       /messages       │     │                  │
└──────────────────┘     └──────────────────────┘     └──────────────────┘
```

## Features

- **Multi-agent orchestration** — 8 specialized subagents (memory, coding, research, 4x analytics)
- **Long-term memory** — persisted to a Databricks Lakebase (Postgres) instance, table `public.agent_memories`
- **SSE streaming** — real-time agent responses with node/subagent indicators
- **Markdown rendering** — AI responses render with syntax-highlighted code blocks, tables, lists
- **Memory panel** — view, search, create, and delete stored memories in the sidebar
- **Thread management** — create, rename, and delete conversation threads
- **Thread history** — message history loads from the LangGraph checkpointer when switching threads
- **Error toasts** — non-blocking notification toasts for errors and status updates
- **Agent topology** — live visualization of which subagent is active

## Memory Storage

Memories are stored in a Databricks Lakebase (Postgres) instance:

```
{LAKEBASE_DATABASE}.public.agent_memories
├── id         UUID         (primary key)
├── user_id    TEXT         (default-user)
├── content    TEXT         (the memory text)
├── category   TEXT         (preference, fact, decision, project, feedback)
└── saved_at   TIMESTAMPTZ
```

The table is auto-created on first startup. Requires the following env vars:

- `LAKEBASE_INSTANCE_NAME` — Lakebase database instance name (required)
- `LAKEBASE_DATABASE` — Postgres database name (default: `databricks_postgres`)

Connections use short-lived OAuth tokens issued via the Databricks SDK
(`WorkspaceClient.database.generate_database_credential`); no static password
is configured.

## Local Development

### Prerequisites

- Node.js 20+
- Python 3.12+
- Databricks workspace credentials configured (`~/.databrickscfg` or env vars)
- `.env` file at repo root with `TAVILY_API_KEY`

### Start the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Start the frontend (with API proxy)

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000. The Vite dev server proxies `/api/*` to the backend at port 8000.

## Docker

Build from this project folder (the image also copies `skills/`):

```bash
docker build -t deep-agent .
docker run -p 8000:8000 --env-file .env deep-agent
```

Or use Docker Compose:

```bash
docker compose up
```

## Deploy to Databricks Apps

### 1. Build the frontend

```bash
cd frontend
npm run build
```

### 2. Deploy

```bash
databricks apps deploy deep-agent-memory --source-code-path .
```

The `app.yaml` configures the uvicorn command and environment variables. The built React app is served as static files by FastAPI.

## Branch-based CI/CD deployment

This repository includes `.github/workflows/databricks-app-deploy.yml` to deploy the same source code to three Databricks Apps in the same workspace.

| Branch | GitHub Environment | Databricks App Name |
|---|---|---|
| `dev` | `dev` | `deep-agent-memory-dev` |
| `stage` | `staging` | `deep-agent-memory-staging` |
| `main` | `prod` | `deep-agent-memory-prod` |

### Required GitHub configuration

Create these GitHub **Environments**: `dev`, `staging`, `prod`.

For each environment, set secrets:

- `DATABRICKS_CLIENT_ID`
- `DATABRICKS_CLIENT_SECRET`

Also set repository variable:

- `DATABRICKS_HOST` (same Databricks workspace host for all environments)

When code is pushed to `dev`, `stage`, or `main`, the workflow creates the corresponding app (if missing) and deploys the latest app code.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/chat` | Send message, stream response (SSE) |
| `POST` | `/api/threads` | Create a new thread |
| `GET` | `/api/threads` | List all threads |
| `GET` | `/api/threads/{id}/messages` | Get message history for a thread |
| `PATCH` | `/api/threads/{id}` | Rename a thread |
| `DELETE` | `/api/threads/{id}` | Delete a thread |
| `GET` | `/api/memories` | List all stored memories |
| `POST` | `/api/memories` | Manually save a memory |
| `DELETE` | `/api/memories/{substring}` | Delete a memory by content match |
