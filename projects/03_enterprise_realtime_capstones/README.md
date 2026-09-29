# 03 · Enterprise and realtime capstones

The most operationally demanding systems: enterprise platforms, multi-agent research, delivery frameworks, voice/realtime systems and deployment-focused capstones.

Every project is an independent application with its own README, `.env.example` and (where it has one) its own
dependency manifest. Install and run each inside its own folder and environment; nothing here shares a runtime.

| # | Project | What you build | Prerequisite repositories | Tests |
|---|---|---|---|---|
| 01 | [Enterprise RAG Platform (Meridian Assist)](01_enterprise_rag_platform/) | Build a permission-aware (ABAC) enterprise RAG platform with evaluation, attacks and observability | 04, 05, 08, 09, 13 | yes |
| 02 | [Enterprise Agentic Workflow Automation Platform](02_enterprise_agentic_workflow_platform/) | Prove guardrail and orchestration properties of a no-code agent workflow platform deterministically | 06, 08, 13 | yes |
| 03 | [Enterprise Multi-Agent AI Research Platform](03_enterprise_multi_agent_research_platform/) | Deploy a guarded, cached, evaluated and red-teamed multi-agent research service on AWS | 08, 09, 13 | no |
| 04 | [FDE Delivery Framework](04_fde_delivery_framework/) | Model an agent delivery engagement as a gate-enforcing state machine with measurable reuse | 06, 13 | yes |
| 05 | [Realtime Voice AI Agent with RAG](05_realtime_voice_ai_agent_with_rag/) | Run a Pipecat voice agent with document RAG, a React client and an AWS ECS deployment | 05, 06, 13 | no |
| 06 | [Pipecat Quickstart](06_pipecat_quickstart/) | Run a Pipecat speech-to-speech bot locally and deploy it to Pipecat Cloud | 01, 06 | no |
| 07 | [Deep Agents App — Memory Command Center](07_deep_agents_app/) | Serve a deep-agent orchestrator with long-term memory as a React + FastAPI Databricks App | 04, 08, 13 | no |

**Why this order.** The three enterprise platforms (01–03) and the delivery framework (04) come first — 02 and 04 are fully deterministic and make good offline starting points. The realtime voice projects (05–06) and the deep-agent Databricks App (07) close the sequence.

Prerequisite numbers refer to the course repositories listed in [the learning path](../../docs/learning-path.md);
each project README links them. [docs/curriculum-map.md](../../docs/curriculum-map.md) lists, per project, the tests
or deterministic demo it ships.
