# AI-Powered Customer Support Copilot

A copilot for customer-support agents: tickets arrive through a FastAPI API, the copilot retrieves policy snippets from the `knowledge_base/` Markdown files, recalls what it knows about the customer from Mem0 memory, and drafts a reply for the human agent to approve in a Streamlit dashboard. `docs/AI-Powered Customer Support Agent Copilot.pdf` is the project brief, [docs/Assignments_and_Quizzes_Customer_Support_Agent.md](docs/Assignments_and_Quizzes_Customer_Support_Agent.md) has exercises, and `diagrams/architecturediagram.png` the architecture.

## Course context

Project 05 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag), [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals), [repository 08 (advanced agent systems)](https://github.com/Sourav692/ai-engineering-demystified-08-advanced-agent-systems), [repository 13 (production and observability)](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability).
- **What it integrates:** a FastAPI service (tickets, drafts, knowledge, memory routers) over SQLite, Chroma RAG on a Markdown knowledge base, Mem0 customer memory, Groq-drafted replies, a Streamlit agent dashboard, Docker Compose, and a GitHub Actions EC2 deployment.
- **External services and expected cost:** Groq (drafts), Google Gemini embeddings (`gemini-embedding-001`); AWS EC2 only if you deploy.
- **Tests / offline demo:** `tests/test_simple.py` — one offline FastAPI health-check test (no keys).
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
uv sync                         # Python 3.11, from pyproject.toml + uv.lock
cp .env.example .env            # add GROQ_API_KEY and GOOGLE_API_KEY
uv run python main.py           # API on http://localhost:8000
uv run streamlit run app.py     # dashboard on http://localhost:8501
uv run pytest                   # offline health-check test
# or both services at once:
docker compose up --build
```

[docs/EC2_deployment_flow.md](docs/EC2_deployment_flow.md) walks through the deployment. The `.github/workflows/` files are kept as reference: GitHub only runs workflows from a repository's root.
