# Setup

## The root environment

```bash
uv sync               # dev tools only (pytest, ruff, pre-commit, nbstripout, jupyterlab)
uv run pytest         # offline checks across the whole repository
uv run ruff check .   # lints root scripts; projects/ is excluded (each project keeps its own style)
uv run pre-commit install
```

`uv run pytest` runs three checks, all offline: every notebook is valid, titled, output-free and its relative paths
resolve (paths a notebook *creates*, or names that are not paths, are listed with a reason in
`scripts/path_allowlist.txt`); every Markdown link resolves inside the repository and nothing points at an absolute
workstation path or the old monorepo layout; every Python file compiles. It does **not** install or run the projects.

## Per-project environments

Install each project inside its own folder, following its README's **Course context → How to run**. The tool differs
by project because the manifests were kept exactly as they shipped:

| Group·# | Project | Manifest(s) |
|---|---|---|
| 01·01 | [Agent Tool-Calling Foundations](../projects/01_foundational_projects/01_agent_tool_calling_foundations/) | requirements.txt |
| 01·02 | [Automated Candidate Interview & Evaluation System](../projects/01_foundational_projects/02_automated_candidate_interview_evaluation/) | requirements.txt |
| 01·03 | [Personalized Holiday Management Agent](../projects/01_foundational_projects/03_personalized_holiday_management_agent/) | requirements.txt, pyproject.toml, setup.py |
| 01·04 | [Resume Genie](../projects/01_foundational_projects/04_resume_genie/) | pyproject.toml, uv.lock, requirements.txt |
| 01·05 | [RAG Systems Projects](../projects/01_foundational_projects/05_rag_systems_projects/) | none — each notebook pip-installs its own dependencies |
| 02·01 | [Building Adaptive RAG](../projects/02_retrieval_agent_projects/01_building_adaptive_rag/) | requirements.txt |
| 02·02 | [ShopUNow Agentic RAG Capstone](../projects/02_retrieval_agent_projects/02_shopunow_agentic_rag/) | none — dependencies listed above |
| 02·03 | [End-to-End Medical Chatbot](../projects/02_retrieval_agent_projects/03_end_to_end_medical_chatbot/) | requirements.txt, pyproject.toml, uv.lock, setup.py |
| 02·04 | [Realtime Source Code Analyzer](../projects/02_retrieval_agent_projects/04_realtime_source_code_analyzer/) | requirements.txt, setup.py |
| 02·05 | [AI-Powered Customer Support Copilot](../projects/02_retrieval_agent_projects/05_ai_powered_customer_support/) | pyproject.toml, uv.lock, Dockerfile, docker-compose.yml |
| 02·06 | [LangGraph Full-Stack Capstone](../projects/02_retrieval_agent_projects/06_langgraph_fullstack_capstone/) | per app: backend/requirements.txt, frontend/package.json (+ lock), streamlit_apps/*/requirements.txt, docker-compose.yaml |
| 02·07 | [LangChain Microservices Capstone](../projects/02_retrieval_agent_projects/07_langchain_microservices_capstone/) | Dockerfiles per service, frontend/package.json (+ lock), Kubernetes YAML |
| 02·08 | [CrewAI Full-Stack Agents App](../projects/02_retrieval_agent_projects/08_crewai_fullstack_agents_app/) | backend/requirements.txt, frontend/package.json (+ lock) |
| 02·09 | [CrewAI Mock Interviewer](../projects/02_retrieval_agent_projects/09_crewai_mock_interviewer/) | pyproject.toml, requirements.txt, ruff.toml, databricks.yml, app.yaml |
| 02·10 | [AutoGen Stock Market Analysis Agent](../projects/02_retrieval_agent_projects/10_autogen_stock_market_analysis_agent/) | none loose — requirements.txt inside Autogen_Stock_Analysis-main.zip |
| 02·11 | [AutoGen Data Analyzer GPT](../projects/02_retrieval_agent_projects/11_autogen_data_analyzer_gpt/) | none — dependencies listed above |
| 02·12 | [AutoGen Notion MCP Agent](../projects/02_retrieval_agent_projects/12_autogen_notion_mcp_agent/) | none — dependencies listed above |
| 03·01 | [Enterprise RAG Platform (Meridian Assist)](../projects/03_enterprise_realtime_capstones/01_enterprise_rag_platform/) | none — dependencies listed above (pytest.ini only) |
| 03·02 | [Enterprise Agentic Workflow Automation Platform](../projects/03_enterprise_realtime_capstones/02_enterprise_agentic_workflow_platform/) | none needed — standard library (pytest for tests) |
| 03·03 | [Enterprise Multi-Agent AI Research Platform](../projects/03_enterprise_realtime_capstones/03_enterprise_multi_agent_research_platform/) | CODE/requirements.txt, CODE/pyrit_dashboard/requirements.txt, Dockerfiles, Terraform |
| 03·04 | [FDE Delivery Framework](../projects/03_enterprise_realtime_capstones/04_fde_delivery_framework/) | none needed — standard library (pytest for tests) |
| 03·05 | [Realtime Voice AI Agent with RAG](../projects/03_enterprise_realtime_capstones/05_realtime_voice_ai_agent_with_rag/) | backend/pyproject.toml + uv.lock, frontend/package.json (+ lock), docker-compose.yml |
| 03·06 | [Pipecat Quickstart](../projects/03_enterprise_realtime_capstones/06_pipecat_quickstart/) | pyproject.toml, Dockerfile, pcc-deploy.toml |
| 03·07 | [Deep Agents App — Memory Command Center](../projects/03_enterprise_realtime_capstones/07_deep_agents_app/) | requirements.txt, frontend/package.json (+ lock), Dockerfile, docker-compose.yaml, app.yaml |

Notes:

- **Python version.** Most projects target 3.12; `AI_Powered_Customer_Support` pins `>=3.11,<3.12` in its own
  `pyproject.toml` and ships a `uv.lock` for 3.11. `uv` installs the right interpreter for projects that declare it.
- **Nested `.github/workflows/`** folders (customer support, medical chatbot, voice agent, multi-agent research
  platform) are kept as deployment references. GitHub only runs workflows from a repository's root, so copy one to a
  standalone repository if you want the CI/CD to run.
- **Nested `.gitignore` files** are the projects' own and stay in place; they keep each project's generated state
  (vector stores, SQLite files, `runs/`, `node_modules/`) out of git.
- **Docker.** Required for the full-stack, microservices, voice and Data Analyzer GPT projects (the last uses Docker
  as its code-execution sandbox).
- **Front ends.** `npm install` inside each `frontend/` folder; nothing under `node_modules/` is committed.
