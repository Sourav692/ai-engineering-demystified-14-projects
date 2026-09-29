# 01 · Foundational projects

Small and medium applications that mainly reinforce repositories 01–07 and 11: one agent loop, one multi-agent team or one RAG pipeline, wrapped in a runnable app or notebook set.

Every project is an independent application with its own README, `.env.example` and (where it has one) its own
dependency manifest. Install and run each inside its own folder and environment; nothing here shares a runtime.

| # | Project | What you build | Prerequisite repositories | Tests |
|---|---|---|---|---|
| 01 | [Agent Tool-Calling Foundations](01_agent_tool_calling_foundations/) | Build a ReAct tool-calling loop from scratch and again as a LangGraph StateGraph, with robustness and logging | 01, 02, 04, 06 | yes |
| 02 | [Automated Candidate Interview & Evaluation System](02_automated_candidate_interview_evaluation/) | Run an AutoGen interviewer/candidate/evaluator team behind a FastAPI WebSocket UI | 01, 02, 06, 11 | no |
| 03 | [Personalized Holiday Management Agent](03_personalized_holiday_management_agent/) | Serve an AutoGen planner + researcher team as a FastAPI holiday-planning API | 01, 06, 11 | no |
| 04 | [Resume Genie](04_resume_genie/) | Build a Streamlit career suite whose LangGraph agent routes and chains resume tools | 01, 02, 04, 05, 06 | no |
| 05 | [RAG Systems Projects](05_rag_systems_projects/) | Apply LangChain RAG end to end: search engine, Q&A, conversational, multi-user and multimodal RAG | 03, 05 | no |

**Why this order.** Start here. Each project exercises one idea from the earlier repositories in a complete, runnable form; the last one (RAG systems) is a notebook sequence that bridges into the retrieval projects of group 02.

Prerequisite numbers refer to the course repositories listed in [the learning path](../../docs/learning-path.md);
each project README links them. [docs/curriculum-map.md](../../docs/curriculum-map.md) lists, per project, the tests
or deterministic demo it ships.
