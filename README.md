# 14 · Projects

The course's integration stage: 24 independent applications and capstones that combine what repositories 01–13 teach, arranged in three ordered groups from single-idea builds to enterprise and realtime systems.

## You are here

[← 13 Production and Observability](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability) · **14 Projects** · end of the course — this is the final repository.

The full 14-repository path is in [docs/learning-path.md](docs/learning-path.md).

## Prerequisites

This repository applies earlier material rather than teaching it. Each project names the repositories it assumes (details in [docs/prerequisites.md](docs/prerequisites.md)); across all projects you will use:

- Python, `.env` files and provider APIs (repository 01) and prompt design (repository 02).
- LangChain chains and LangGraph graphs (repositories 03 and 04).
- Standard RAG — loading, chunking, embeddings, vector stores (repository 05) — and agentic/adaptive RAG (repository 09).
- The single-agent loop, tools and ReAct (repository 06); memory and multi-agent systems, deep agents (repository 08).
- MCP (repository 10) and the CrewAI/AutoGen frameworks (repository 11) for the framework apps in group 02.
- Tracing, cost, guardrails, testing and deployment (repository 13) for the full-stack and enterprise projects.
- Comfort with Docker, and for the web front ends Node.js and npm.

## Learning outcomes

After working through these projects you can:

1. Turn a notebook-level agent or RAG idea into a runnable application with its own environment, configuration and entry point.
2. Build RAG applications end to end — from a CLI and notebooks to Flask, Streamlit and full-stack FastAPI + React/Angular apps.
3. Serve CrewAI and AutoGen teams, MCP-connected agents and deep agents behind web APIs with streaming responses.
4. Package and deploy AI applications with Docker, Docker Compose, Kubernetes manifests, AWS (ECS, EC2, CloudFormation, Terraform), Databricks Apps and Pipecat Cloud.
5. Design enterprise-grade properties — permission-aware retrieval, guardrails, evaluation gates, red teaming, delivery gates — and prove them with deterministic tests.
6. Build realtime voice agents that combine speech-to-text, an LLM, text-to-speech and retrieval.

## Projects

Every project is copied whole, with its own structure, README, `.env.example`, and — where it ships one — its own dependency manifest, lockfile, tests, front end and deployment files. The group folders set a recommended progression; they never share a runtime.

### [01 · Foundational projects](projects/01_foundational_projects/)

Small and medium applications that mainly reinforce repositories 01–07 and 11: one agent loop, one multi-agent team or one RAG pipeline, wrapped in a runnable app or notebook set.

| # | Project | What you build | Prerequisite repos | Tests |
|---|---|---|---|---|
| 01 | [Agent Tool-Calling Foundations](projects/01_foundational_projects/01_agent_tool_calling_foundations/) | Build a ReAct tool-calling loop from scratch and again as a LangGraph StateGraph, with robustness and logging | 01, 02, 04, 06 | yes |
| 02 | [Automated Candidate Interview & Evaluation System](projects/01_foundational_projects/02_automated_candidate_interview_evaluation/) | Run an AutoGen interviewer/candidate/evaluator team behind a FastAPI WebSocket UI | 01, 02, 06, 11 | — |
| 03 | [Personalized Holiday Management Agent](projects/01_foundational_projects/03_personalized_holiday_management_agent/) | Serve an AutoGen planner + researcher team as a FastAPI holiday-planning API | 01, 06, 11 | — |
| 04 | [Resume Genie](projects/01_foundational_projects/04_resume_genie/) | Build a Streamlit career suite whose LangGraph agent routes and chains resume tools | 01, 02, 04, 05, 06 | — |
| 05 | [RAG Systems Projects](projects/01_foundational_projects/05_rag_systems_projects/) | Apply LangChain RAG end to end: search engine, Q&A, conversational, multi-user and multimodal RAG | 03, 05 | — |

### [02 · Retrieval and agent projects](projects/02_retrieval_agent_projects/)

Integrated RAG, agentic-RAG, knowledge-base and full-stack agent applications that mainly reinforce repositories 05–11.

| # | Project | What you build | Prerequisite repos | Tests |
|---|---|---|---|---|
| 01 | [Building Adaptive RAG](projects/02_retrieval_agent_projects/01_building_adaptive_rag/) | Package adaptive RAG (routing, grading, web fallback, self-correction) as a tested CLI application | 04, 05, 09 | yes |
| 02 | [ShopUNow Agentic RAG Capstone](projects/02_retrieval_agent_projects/02_shopunow_agentic_rag/) | Build a multi-department, multi-user agentic RAG assistant with LangGraph, Chroma and conversation memory | 04, 05, 08, 09 | — |
| 03 | [End-to-End Medical Chatbot](projects/02_retrieval_agent_projects/03_end_to_end_medical_chatbot/) | Ship a Pinecone-backed medical RAG chatbot with Flask, Docker and CI/CD | 03, 05, 13 | — |
| 04 | [Realtime Source Code Analyzer](projects/02_retrieval_agent_projects/04_realtime_source_code_analyzer/) | Chat with a GitHub repository through conversational retrieval over its source code | 03, 05 | — |
| 05 | [AI-Powered Customer Support Copilot](projects/02_retrieval_agent_projects/05_ai_powered_customer_support/) | Build a support-agent copilot with RAG, Mem0 memory, SQLite tickets, FastAPI, Streamlit and Docker | 05, 06, 08, 13 | yes |
| 06 | [LangGraph Full-Stack Capstone](projects/02_retrieval_agent_projects/06_langgraph_fullstack_capstone/) | Ship LangGraph workflows as a FastAPI + Angular + Postgres app, unit-test nodes, and build Streamlit extractors | 03, 04, 06, 13 | yes |
| 07 | [LangChain Microservices Capstone](projects/02_retrieval_agent_projects/07_langchain_microservices_capstone/) | Deploy LangChain services, Postgres and a React UI as containers with Kubernetes manifests | 03, 05, 13 | — |
| 08 | [CrewAI Full-Stack Agents App](projects/02_retrieval_agent_projects/08_crewai_fullstack_agents_app/) | Serve eight CrewAI crews behind FastAPI server-sent events and a React UI | 06, 11 | — |
| 09 | [CrewAI Mock Interviewer](projects/02_retrieval_agent_projects/09_crewai_mock_interviewer/) | Run a CrewAI mock-interview crew as a Streamlit app and deploy it to Databricks Apps | 06, 11 | — |
| 10 | [AutoGen Stock Market Analysis Agent](projects/02_retrieval_agent_projects/10_autogen_stock_market_analysis_agent/) | Coordinate AutoGen analyst, strategy and supervisor agents over yfinance data in Streamlit | 06, 11 | — |
| 11 | [AutoGen Data Analyzer GPT](projects/02_retrieval_agent_projects/11_autogen_data_analyzer_gpt/) | Let an AutoGen analyst team write and run code in a Docker sandbox over an uploaded CSV | 06, 11 | — |
| 12 | [AutoGen Notion MCP Agent](projects/02_retrieval_agent_projects/12_autogen_notion_mcp_agent/) | Expose an AutoGen agent that drives Notion through its MCP server as a Flask API | 06, 10, 11 | — |

### [03 · Enterprise and realtime capstones](projects/03_enterprise_realtime_capstones/)

The most operationally demanding systems: enterprise platforms, multi-agent research, delivery frameworks, voice/realtime systems and deployment-focused capstones.

| # | Project | What you build | Prerequisite repos | Tests |
|---|---|---|---|---|
| 01 | [Enterprise RAG Platform (Meridian Assist)](projects/03_enterprise_realtime_capstones/01_enterprise_rag_platform/) | Build a permission-aware (ABAC) enterprise RAG platform with evaluation, attacks and observability | 04, 05, 08, 09, 13 | yes |
| 02 | [Enterprise Agentic Workflow Automation Platform](projects/03_enterprise_realtime_capstones/02_enterprise_agentic_workflow_platform/) | Prove guardrail and orchestration properties of a no-code agent workflow platform deterministically | 06, 08, 13 | yes |
| 03 | [Enterprise Multi-Agent AI Research Platform](projects/03_enterprise_realtime_capstones/03_enterprise_multi_agent_research_platform/) | Deploy a guarded, cached, evaluated and red-teamed multi-agent research service on AWS | 08, 09, 13 | — |
| 04 | [FDE Delivery Framework](projects/03_enterprise_realtime_capstones/04_fde_delivery_framework/) | Model an agent delivery engagement as a gate-enforcing state machine with measurable reuse | 06, 13 | yes |
| 05 | [Realtime Voice AI Agent with RAG](projects/03_enterprise_realtime_capstones/05_realtime_voice_ai_agent_with_rag/) | Run a Pipecat voice agent with document RAG, a React client and an AWS ECS deployment | 05, 06, 13 | — |
| 06 | [Pipecat Quickstart](projects/03_enterprise_realtime_capstones/06_pipecat_quickstart/) | Run a Pipecat speech-to-speech bot locally and deploy it to Pipecat Cloud | 01, 06 | — |
| 07 | [Deep Agents App — Memory Command Center](projects/03_enterprise_realtime_capstones/07_deep_agents_app/) | Serve a deep-agent orchestrator with long-term memory as a React + FastAPI Databricks App | 04, 08, 13 | — |

**Why this order.** Group 01 exercises one idea at a time; group 02 integrates retrieval, agents and full-stack delivery, then shows the CrewAI and AutoGen lessons of repository 11 as deployable products; group 03 finishes with systems whose hard part is operational — access control, guardrails, delivery gates, realtime audio and platform deployment. Within each group the order runs from smaller to larger systems. The catalog planned 18 projects; the six framework and deep-agent apps (group 02 projects 08–12, group 03 project 07) arrived from repositories 08 and 11, which kept the teaching and deferred the deployable products here. [docs/curriculum-map.md](docs/curriculum-map.md) lists every project's notebooks, tests and deterministic demos.

## Setup

Requires [uv](https://docs.astral.sh/uv/). The root environment holds only the repository checks — there is deliberately no environment that pretends the 24 projects share compatible dependencies (CrewAI, for example, pins `chromadb<1.2` while other projects need newer Chroma releases).

```bash
git clone https://github.com/Sourav692/ai-engineering-demystified-14-projects.git
cd ai-engineering-demystified-14-projects
uv sync                  # dev tools only: pytest, ruff, pre-commit, nbstripout, jupyterlab
cp .env.example .env     # the root checks need no keys; each project has its own .env.example
uv run pytest            # offline: notebook structure, links, self-containment, Python compiles
uv run jupyter lab       # browse any project's notebooks (run them in that project's environment)
```

Then pick a project, `cd` into its folder and follow its README: every README starts with a **Course context** section giving prerequisites, services and cost, and the exact install and run commands. [docs/setup.md](docs/setup.md) summarises each project's manifest and runtime needs (Python version, Docker, Node.js). Activate the git hooks once with `uv run pre-commit install`.

## Environment variables

The root checks read no environment variables. Each project documents its own in its `.env.example` (names only) — copy it to `.env` inside that project folder. Across the projects you will meet keys for OpenAI, Groq, Anthropic, Google Gemini, Databricks, Pinecone, Tavily, Serper, Mem0, Notion, ngrok, Deepgram, Cartesia, ElevenLabs, MongoDB, AWS and LangSmith; each project's README says which it needs and roughly what a run costs. Group 03 projects 02 and 04 need no keys at all.

## Out of scope

This repository integrates; it does not introduce concepts. First instruction lives in the owning repositories:

- Python, provider APIs, prompting → [repository 01 (foundations)](https://github.com/Sourav692/ai-engineering-demystified-01-foundations), [repository 02 (prompt and context engineering)](https://github.com/Sourav692/ai-engineering-demystified-02-prompt-context-engineering).
- LangChain and LangGraph mechanics → [repository 03 (LangChain fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-03-langchain-fundamentals), [repository 04 (LangGraph fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-04-langgraph-fundamentals).
- Retrieval and standard RAG → [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag); agentic, corrective and adaptive RAG → [repository 09 (advanced RAG)](https://github.com/Sourav692/ai-engineering-demystified-09-advanced-rag).
- Agent loops and tools → [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals); provider agent SDKs → [repository 07 (first-party agent SDKs)](https://github.com/Sourav692/ai-engineering-demystified-07-first-party-agent-sdks); memory, multi-agent and deep agents → [repository 08 (advanced agent systems)](https://github.com/Sourav692/ai-engineering-demystified-08-advanced-agent-systems).
- MCP, A2A, ACP → [repository 10 (agent protocols)](https://github.com/Sourav692/ai-engineering-demystified-10-agent-protocols); CrewAI, AutoGen, DSPy, PydanticAI → [repository 11 (alternative agent frameworks)](https://github.com/Sourav692/ai-engineering-demystified-11-alternative-agent-frameworks).
- AI coding tools → repository 12 (AI coding tools, not yet published).
- Tracing, cost, caching, safety and deployment as topics → [repository 13 (production and observability)](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability).
- Agent and RAG evaluation curricula live in the separate `Agent_Evaluation_Demystified` repository.

## License and acknowledgements

MIT — see [LICENSE](LICENSE). Some projects carry their own licence file from their upstream source (Apache 2.0 for the candidate-interview, medical-chatbot and holiday-agent apps; MIT for the source-code analyzer); those apply to that project folder.

Extracted from [`Sourav692/AI-ENGINEERING-DEMYSTIFIED`](https://github.com/Sourav692/AI-ENGINEERING-DEMYSTIFIED) at tag `pre-multirepo-split-2026-09` (source folder `05_Projects/`, plus six apps deferred here by repositories 08 and 11); [docs/content-inventory.csv](docs/content-inventory.csv) maps every source file to its new path or records why it was not migrated. Several projects adapt public tutorials and courses, credited in their own READMEs and reference files (for example the Pipecat quickstart, entbappy's medical chatbot, the adaptive-RAG refactor of Marco's LangGraph course, data-guru0's AI-Security project, and Krish Naik's MCP-with-AutoGen course). Third-party documents (papers, articles, course slides) are kept as found in the source repository and listed with their hashes in [docs/data-sources.md](docs/data-sources.md).
