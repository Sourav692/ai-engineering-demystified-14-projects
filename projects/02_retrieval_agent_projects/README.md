# 02 · Retrieval and agent projects

Integrated RAG, agentic-RAG, knowledge-base and full-stack agent applications that mainly reinforce repositories 05–11.

Every project is an independent application with its own README, `.env.example` and (where it has one) its own
dependency manifest. Install and run each inside its own folder and environment; nothing here shares a runtime.

| # | Project | What you build | Prerequisite repositories | Tests |
|---|---|---|---|---|
| 01 | [Building Adaptive RAG](01_building_adaptive_rag/) | Package adaptive RAG (routing, grading, web fallback, self-correction) as a tested CLI application | 04, 05, 09 | yes |
| 02 | [ShopUNow Agentic RAG Capstone](02_shopunow_agentic_rag/) | Build a multi-department, multi-user agentic RAG assistant with LangGraph, Chroma and conversation memory | 04, 05, 08, 09 | no |
| 03 | [End-to-End Medical Chatbot](03_end_to_end_medical_chatbot/) | Ship a Pinecone-backed medical RAG chatbot with Flask, Docker and CI/CD | 03, 05, 13 | no |
| 04 | [Realtime Source Code Analyzer](04_realtime_source_code_analyzer/) | Chat with a GitHub repository through conversational retrieval over its source code | 03, 05 | no |
| 05 | [AI-Powered Customer Support Copilot](05_ai_powered_customer_support/) | Build a support-agent copilot with RAG, Mem0 memory, SQLite tickets, FastAPI, Streamlit and Docker | 05, 06, 08, 13 | yes |
| 06 | [LangGraph Full-Stack Capstone](06_langgraph_fullstack_capstone/) | Ship LangGraph workflows as a FastAPI + Angular + Postgres app, unit-test nodes, and build Streamlit extractors | 03, 04, 06, 13 | yes |
| 07 | [LangChain Microservices Capstone](07_langchain_microservices_capstone/) | Deploy LangChain services, Postgres and a React UI as containers with Kubernetes manifests | 03, 05, 13 | no |
| 08 | [CrewAI Full-Stack Agents App](08_crewai_fullstack_agents_app/) | Serve eight CrewAI crews behind FastAPI server-sent events and a React UI | 06, 11 | no |
| 09 | [CrewAI Mock Interviewer](09_crewai_mock_interviewer/) | Run a CrewAI mock-interview crew as a Streamlit app and deploy it to Databricks Apps | 06, 11 | no |
| 10 | [AutoGen Stock Market Analysis Agent](10_autogen_stock_market_analysis_agent/) | Coordinate AutoGen analyst, strategy and supervisor agents over yfinance data in Streamlit | 06, 11 | no |
| 11 | [AutoGen Data Analyzer GPT](11_autogen_data_analyzer_gpt/) | Let an AutoGen analyst team write and run code in a Docker sandbox over an uploaded CSV | 06, 11 | no |
| 12 | [AutoGen Notion MCP Agent](12_autogen_notion_mcp_agent/) | Expose an AutoGen agent that drives Notion through its MCP server as a Flask API | 06, 10, 11 | no |

**Why this order.** Projects 01–07 are the retrieval and full-stack applications, ordered from a single RAG CLI to multi-service deployments. Projects 08–12 are deployable apps built on the alternative frameworks of repository 11 (CrewAI, AutoGen) — the product forms of lessons whose framework mechanics repository 11 teaches.

Prerequisite numbers refer to the course repositories listed in [the learning path](../../docs/learning-path.md);
each project README links them. [docs/curriculum-map.md](../../docs/curriculum-map.md) lists, per project, the tests
or deterministic demo it ships.
