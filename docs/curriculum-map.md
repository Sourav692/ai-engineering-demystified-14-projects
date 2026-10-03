# Curriculum map

Every project, what it builds, the notebooks it contains, and whether it ships automated tests or a deterministic
demo. Tests listed here belong to the project and run in the project's own environment; the root `uv run pytest` only
runs the repository-wide structural checks. No tests were added during the migration.


## 01 · Foundational projects


### 01 · [Agent Tool-Calling Foundations](../projects/01_foundational_projects/01_agent_tool_calling_foundations/)

- **Objective:** Build a ReAct tool-calling loop from scratch and again as a LangGraph StateGraph, with robustness and logging.
- **Tests / deterministic demo:** **yes** — 12 offline pytest cases (`tests/test_agent.py`); the rule-based brain makes every run deterministic.
- **Notebooks:**
  - [`notebooks/agent_tool_calling_demo.ipynb`](../projects/01_foundational_projects/01_agent_tool_calling_foundations/notebooks/agent_tool_calling_demo.ipynb) — 🤖 Agent Tool-Calling Loop — Guided Demo
  - [`notebooks/robust_langgraph_tool_calling_agent.ipynb`](../projects/01_foundational_projects/01_agent_tool_calling_foundations/notebooks/robust_langgraph_tool_calling_agent.ipynb) — 🤖 Native LangGraph Tool Calling Agent (Idiomatic @tool Pattern)
  - [`notebooks/agent_tool_calling_demo_openai.ipynb`](../projects/01_foundational_projects/01_agent_tool_calling_foundations/notebooks/agent_tool_calling_demo_openai.ipynb) — 🤖 Agent Tool-Calling Loop — Single-Notebook Demo (Real LLM)
  - [`notebooks/langgraph_react_agent.ipynb`](../projects/01_foundational_projects/01_agent_tool_calling_foundations/notebooks/langgraph_react_agent.ipynb) — 🕸️ LangGraph ReAct Agent — Production-Shaped Reference (+ DevRev Prep Pointers)

### 02 · [Automated Candidate Interview & Evaluation System](../projects/01_foundational_projects/02_automated_candidate_interview_evaluation/)

- **Objective:** Run an AutoGen interviewer/candidate/evaluator team behind a FastAPI WebSocket UI.
- **Tests / deterministic demo:** none — no automated tests; `agent.ipynb` runs the same interview loop (live, needs Groq; scripted candidate answers by default, set `INTERACTIVE = True` to type your own).
- **Notebooks:**
  - [`agent.ipynb`](../projects/01_foundational_projects/02_automated_candidate_interview_evaluation/agent.ipynb) — 🎯 Automated Candidate Interview & Evaluation System

### 03 · [Personalized Holiday Management Agent](../projects/01_foundational_projects/03_personalized_holiday_management_agent/)

- **Objective:** Serve an AutoGen planner + researcher team as a FastAPI holiday-planning API.
- **Tests / deterministic demo:** none — no tests; `python main.py` runs one plan end to end (live, needs OpenAI).
- **Notebooks:** none (application code only).

### 04 · [Resume Genie](../projects/01_foundational_projects/04_resume_genie/)

- **Objective:** Build a Streamlit career suite whose LangGraph agent routes and chains resume tools.
- **Tests / deterministic demo:** none — no automated tests; `notebooks/Agent_Testing.ipynb` exercises the agent manually (live, needs OpenAI: it builds the graph on `gpt-4o-mini` via `aied_helpers`; uses the sample résumé in `content/`).
- **Notebooks:**
  - [`notebooks/Resume_Checker.ipynb`](../projects/01_foundational_projects/04_resume_genie/notebooks/Resume_Checker.ipynb) — 🔍 Resume Checker
  - [`notebooks/Resume_Scorer.ipynb`](../projects/01_foundational_projects/04_resume_genie/notebooks/Resume_Scorer.ipynb) — 🧮 Resume Scorer
  - [`notebooks/Cover_Letter_Generator.ipynb`](../projects/01_foundational_projects/04_resume_genie/notebooks/Cover_Letter_Generator.ipynb) — ✉️ Cover Letter Generator
  - [`notebooks/AI_Career_Coach.ipynb`](../projects/01_foundational_projects/04_resume_genie/notebooks/AI_Career_Coach.ipynb) — 🎯 AI Career Coach
  - [`notebooks/Agent_Testing.ipynb`](../projects/01_foundational_projects/04_resume_genie/notebooks/Agent_Testing.ipynb) — 🧪 Resume Genie Agent — Testing Notebook

### 05 · [RAG Systems Projects](../projects/01_foundational_projects/05_rag_systems_projects/)

- **Objective:** Apply LangChain RAG end to end: search engine, Q&A, conversational, multi-user and multimodal RAG.
- **Tests / deterministic demo:** none — no tests; notebooks only (live, need OpenAI).
- **Notebooks:**
  - [`notebooks/01_build_document_retriever_search_engine.ipynb`](../projects/01_foundational_projects/05_rag_systems_projects/notebooks/01_build_document_retriever_search_engine.ipynb) — 🔎 Build a Document Retriever Search Engine
  - [`notebooks/02_rag_system_for_question_answering.ipynb`](../projects/01_foundational_projects/05_rag_systems_projects/notebooks/02_rag_system_for_question_answering.ipynb) — ❓ RAG System for Question Answering
  - [`notebooks/03_conversational_rag.ipynb`](../projects/01_foundational_projects/05_rag_systems_projects/notebooks/03_conversational_rag.ipynb) — 💬 Conversational RAG with Chat History
  - [`notebooks/04_multi_user_conversational_rag_system.ipynb`](../projects/01_foundational_projects/05_rag_systems_projects/notebooks/04_multi_user_conversational_rag_system.ipynb) — 👥 Multi-User Conversational RAG System
  - [`notebooks/05_multimodal_rag_with_gpt_4o.ipynb`](../projects/01_foundational_projects/05_rag_systems_projects/notebooks/05_multimodal_rag_with_gpt_4o.ipynb) — 🖼️ Multimodal RAG with GPT-4o-Family Models

## 02 · Retrieval and agent projects


### 01 · [Building Adaptive RAG](../projects/02_retrieval_agent_projects/01_building_adaptive_rag/)

- **Objective:** Package adaptive RAG (routing, grading, web fallback, self-correction) as a tested CLI application.
- **Tests / deterministic demo:** **yes** — `tests/test_chains.py` — live tests: they build the retriever and call Gemini, so they need keys and cost cents.
- **Notebooks:** none (application code only).

### 02 · [ShopUNow Agentic RAG Capstone](../projects/02_retrieval_agent_projects/02_shopunow_agentic_rag/)

- **Objective:** Build a multi-department, multi-user agentic RAG assistant with LangGraph, Chroma and conversation memory.
- **Tests / deterministic demo:** none — no tests; the two notebooks build and query the system (live).
- **Notebooks:**
  - [`01_create_vector_databases.ipynb`](../projects/02_retrieval_agent_projects/02_shopunow_agentic_rag/01_create_vector_databases.ipynb) — 🗄️ ShopUNow — Create Department Vector Databases
  - [`02_agentic_rag_system.ipynb`](../projects/02_retrieval_agent_projects/02_shopunow_agentic_rag/02_agentic_rag_system.ipynb) — 🛍️ ShopUNow — Multi-User Conversational Agentic RAG System (LangGraph)

### 03 · [End-to-End Medical Chatbot](../projects/02_retrieval_agent_projects/03_end_to_end_medical_chatbot/)

- **Objective:** Ship a Pinecone-backed medical RAG chatbot with Flask, Docker and CI/CD.
- **Tests / deterministic demo:** none — no tests; `research/demo.ipynb` is the exploratory build (live).
- **Notebooks:**
  - [`research/demo.ipynb`](../projects/02_retrieval_agent_projects/03_end_to_end_medical_chatbot/research/demo.ipynb) — 🩺 Medical RAG Chatbot — Build the Retrieval Pipeline

### 04 · [Realtime Source Code Analyzer](../projects/02_retrieval_agent_projects/04_realtime_source_code_analyzer/)

- **Objective:** Chat with a GitHub repository through conversational retrieval over its source code.
- **Tests / deterministic demo:** none — no tests; `research/trials.ipynb` is the exploratory build (live).
- **Notebooks:**
  - [`research/trials.ipynb`](../projects/02_retrieval_agent_projects/04_realtime_source_code_analyzer/research/trials.ipynb) — 🔎 Chat with a GitHub Repository: Code-Aware RAG

### 05 · [AI-Powered Customer Support Copilot](../projects/02_retrieval_agent_projects/05_ai_powered_customer_support/)

- **Objective:** Build a support-agent copilot with RAG, Mem0 memory, SQLite tickets, FastAPI, Streamlit and Docker.
- **Tests / deterministic demo:** **yes** — `tests/test_simple.py` — one offline FastAPI health-check test (no keys).
- **Notebooks:**
  - [`notebooks/experiments.ipynb`](../projects/02_retrieval_agent_projects/05_ai_powered_customer_support/notebooks/experiments.ipynb) — 🧠 Experiments: Mem0 Customer Memory and a LangChain Tool Agent

### 06 · [LangGraph Full-Stack Capstone](../projects/02_retrieval_agent_projects/06_langgraph_fullstack_capstone/)

- **Objective:** Ship LangGraph workflows as a FastAPI + Angular + Postgres app, unit-test nodes, and build Streamlit extractors.
- **Tests / deterministic demo:** **yes** — `unit_tests/` — pytest node tests with mocked LLMs (offline); Angular `*.spec.ts` files for the frontend.
- **Notebooks:** none (application code only).

### 07 · [LangChain Microservices Capstone](../projects/02_retrieval_agent_projects/07_langchain_microservices_capstone/)

- **Objective:** Deploy LangChain services, Postgres and a React UI as containers with Kubernetes manifests.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

### 08 · [CrewAI Full-Stack Agents App](../projects/02_retrieval_agent_projects/08_crewai_fullstack_agents_app/)

- **Objective:** Serve eight CrewAI crews behind FastAPI server-sent events and a React UI.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

### 09 · [CrewAI Mock Interviewer](../projects/02_retrieval_agent_projects/09_crewai_mock_interviewer/)

- **Objective:** Run a CrewAI mock-interview crew as a Streamlit app and deploy it to Databricks Apps.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

### 10 · [AutoGen Stock Market Analysis Agent](../projects/02_retrieval_agent_projects/10_autogen_stock_market_analysis_agent/)

- **Objective:** Coordinate AutoGen analyst, strategy and supervisor agents over yfinance data in Streamlit.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

### 11 · [AutoGen Data Analyzer GPT](../projects/02_retrieval_agent_projects/11_autogen_data_analyzer_gpt/)

- **Objective:** Let an AutoGen analyst team write and run code in a Docker sandbox over an uploaded CSV.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

### 12 · [AutoGen Notion MCP Agent](../projects/02_retrieval_agent_projects/12_autogen_notion_mcp_agent/)

- **Objective:** Expose an AutoGen agent that drives Notion through its MCP server as a Flask API.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

## 03 · Enterprise and realtime capstones


### 01 · [Enterprise RAG Platform (Meridian Assist)](../projects/03_enterprise_realtime_capstones/01_enterprise_rag_platform/)

- **Objective:** Build a permission-aware (ABAC) enterprise RAG platform with evaluation, attacks and observability.
- **Tests / deterministic demo:** **yes** — `tests/` — policy, retrieval, pipeline and golden-set tests; the `llm` and `index` markers separate live tests, the rest run offline.
- **Notebooks:**
  - [`notebooks/02-hands-on.ipynb`](../projects/03_enterprise_realtime_capstones/01_enterprise_rag_platform/notebooks/02-hands-on.ipynb) — 🔐 Enterprise RAG with Access Control - Hands On
  - [`notebooks/04-databricks-enterprise-rag.ipynb`](../projects/03_enterprise_realtime_capstones/01_enterprise_rag_platform/notebooks/04-databricks-enterprise-rag.ipynb) — 🏛️ Enterprise RAG with Access Control — on Databricks

### 02 · [Enterprise Agentic Workflow Automation Platform](../projects/03_enterprise_realtime_capstones/02_enterprise_agentic_workflow_platform/)

- **Objective:** Prove guardrail and orchestration properties of a no-code agent workflow platform deterministically.
- **Tests / deterministic demo:** **yes** — 21 deterministic offline tests (`tests/test_platform.py`) plus two scripted demos.
- **Notebooks:**
  - [`notebooks/02-hands-on.ipynb`](../projects/03_enterprise_realtime_capstones/02_enterprise_agentic_workflow_platform/notebooks/02-hands-on.ipynb) — 🤖 Agent Platform — Hands On: a governed, multi-channel workflow engine

### 03 · [Enterprise Multi-Agent AI Research Platform](../projects/03_enterprise_realtime_capstones/03_enterprise_multi_agent_research_platform/)

- **Objective:** Deploy a guarded, cached, evaluated and red-teamed multi-agent research service on AWS.
- **Tests / deterministic demo:** none — no tests; the PyRIT dashboard and LangSmith judge are the runtime checks.
- **Notebooks:** none (application code only).

### 04 · [FDE Delivery Framework](../projects/03_enterprise_realtime_capstones/04_fde_delivery_framework/)

- **Objective:** Model an agent delivery engagement as a gate-enforcing state machine with measurable reuse.
- **Tests / deterministic demo:** **yes** — 17 deterministic offline tests (`tests/test_gates.py`) plus two scripted demos.
- **Notebooks:**
  - [`notebooks/02-hands-on.ipynb`](../projects/03_enterprise_realtime_capstones/04_fde_delivery_framework/notebooks/02-hands-on.ipynb) — 🏗️ Delivery Framework — Hands On: a gated 14-day FDE engagement pipeline

### 05 · [Realtime Voice AI Agent with RAG](../projects/03_enterprise_realtime_capstones/05_realtime_voice_ai_agent_with_rag/)

- **Objective:** Run a Pipecat voice agent with document RAG, a React client and an AWS ECS deployment.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

### 06 · [Pipecat Quickstart](../projects/03_enterprise_realtime_capstones/06_pipecat_quickstart/)

- **Objective:** Run a Pipecat speech-to-speech bot locally and deploy it to Pipecat Cloud.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

### 07 · [Deep Agents App — Memory Command Center](../projects/03_enterprise_realtime_capstones/07_deep_agents_app/)

- **Objective:** Serve a deep-agent orchestrator with long-term memory as a React + FastAPI Databricks App.
- **Tests / deterministic demo:** none — no tests.
- **Notebooks:** none (application code only).

## Tests and demos at a glance

| Project | Automated tests | Offline? |
|---|---|---|
| 01·01 Agent tool-calling foundations | 12 pytest cases | yes |
| 02·01 Building adaptive RAG | `tests/test_chains.py` | no — calls Gemini |
| 02·05 AI-powered customer support | 1 FastAPI health test | yes |
| 02·06 LangGraph full-stack capstone | node tests with mocked LLMs; Angular specs | yes |
| 03·01 Enterprise RAG platform | policy/retrieval/pipeline/golden-set suites | partly — `-m "not llm and not index"` is offline |
| 03·02 Enterprise agentic workflow platform | 21 tests + two scripted demos | yes, fully deterministic |
| 03·04 FDE delivery framework | 17 tests + two scripted demos | yes, fully deterministic |

The other 17 projects ship no automated tests; their notebooks, CLI entry points (`main.py`) or apps are the demos,
and all of them call paid or free-tier model APIs.
