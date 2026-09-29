# Realtime Voice AI Agent with RAG

A voice agent you can talk to about your own documents. Upload PDFs or Word files; they are chunked, embedded and stored in MongoDB; during a WebRTC voice session the Pipecat pipeline retrieves relevant chunks and answers out loud.

```
React frontend (Pipecat client, Tailwind)  --WebRTC-->  FastAPI backend
   Pipecat pipeline: Deepgram STT -> Groq LLM (+ RAG context) -> ElevenLabs TTS
   RAG service: pypdf / python-docx -> chunks -> embeddings -> MongoDB vector search
```

| Layer | Technologies |
|---|---|
| Frontend | React 18, TypeScript, Vite, Tailwind, `@pipecat-ai/client-react` |
| Backend | FastAPI, Pipecat, LangChain, Motor (async MongoDB) |
| Voice pipeline | Deepgram (STT), Groq (LLM), ElevenLabs (TTS) |
| Documents | pypdf, python-docx |
| Infrastructure | AWS ECS Fargate, CloudFormation, Docker Compose |

The application is in `Codes/rag_voice_ai_agent-deployment_live/` (`backend/app/` holds the pipeline in `bot.py`, routers, models and the RAG/embedding/text-extraction services); `Docs/` has the report, deployment guide, assignments and the architecture diagram.

## Course context

Project 05 of **group 03 (enterprise and realtime capstones)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag), [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals), [repository 13 (production and observability)](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability).
- **What it integrates:** a Pipecat voice pipeline (Deepgram speech-to-text, Groq LLM, ElevenLabs text-to-speech) with retrieval over uploaded PDF/DOCX documents stored in MongoDB, a React + TypeScript Pipecat client, Docker Compose, and an AWS ECS Fargate deployment (CloudFormation, ECR, GitHub Actions).
- **External services and expected cost:** Deepgram, Groq, ElevenLabs and Google (embeddings) — usage-billed, cents per conversation; MongoDB (Atlas free tier works); AWS Fargate bills by uptime if you deploy — `infrastructure/destroy-aws.sh` tears it down.
- **Tests / offline demo:** no tests.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
cd Codes/rag_voice_ai_agent-deployment_live
cp ../../.env.example backend/.env    # fill in the keys
docker compose up --build                 # backend :8000, frontend :3000
```

[Docs/DEPLOYMENT.md](Docs/DEPLOYMENT.md) covers the AWS deployment and [Docs/PROJECT_REPORT.md](Docs/PROJECT_REPORT.md) the design. The `.github/workflows/` files are kept as reference: GitHub only runs workflows from a repository's root.
