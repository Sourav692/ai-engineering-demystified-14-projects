# CrewAI Full-Stack Agents App

A web front end for eight small CrewAI crews. Each crew is a FastAPI router that runs the crew and streams its console output to the browser as server-sent events; the React app has one page per crew.

## Course context

Project 08 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals), [repository 11 (alternative agent frameworks)](https://github.com/Sourav692/ai-engineering-demystified-11-alternative-agent-frameworks).
- **What it integrates:** the eight simple CrewAI crews taught in repository 11 (fitness, travel, image generation, books with Mem0, data analyst, fraud, onboarding, summariser) as FastAPI routers streaming server-sent events to a React + Vite + Tailwind UI.
- **External services and expected cost:** a Databricks-served model through LiteLLM (`databricks/databricks-gpt-5-4`), OpenAI DALL-E 3 for images (about $0.04 per image), Serper web search, Mem0.
- **Tests / offline demo:** no tests.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
cd backend && pip install -r requirements.txt && uvicorn main:app --port 8000
cd frontend && npm install && npm run dev    # Vite proxies /api and /outputs to :8000
```
