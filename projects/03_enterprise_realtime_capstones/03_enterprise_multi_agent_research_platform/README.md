# Enterprise Multi-Agent AI Research Platform

Give it a topic and it researches, writes a report, safety-checks it, caches it and remembers it — an AWS-hosted multi-agent service with guardrails, evaluation and red teaming on every request. The application lives in [CODE/](CODE/README.md); `ARCHITECTURE DIAGRAMS/` holds the Mermaid diagrams, rendered architecture pages and a layer-by-layer explanation (`LAYERS_EXPLAINED.md`), and `EXCALIDRAW FILES/` the security architecture sketch.

## Course context

Project 03 of **group 03 (enterprise and realtime capstones)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 08 (advanced agent systems)](https://github.com/Sourav692/ai-engineering-demystified-08-advanced-agent-systems), [repository 09 (advanced RAG)](https://github.com/Sourav692/ai-engineering-demystified-09-advanced-rag), [repository 13 (production and observability)](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability).
- **What it integrates:** a four-agent LangGraph research pipeline (search, summarise, write, verify) behind FastAPI, a TensorZero LLM gateway with fallback, AWS Bedrock Guardrails, Redis semantic cache and job queue, pgvector long-term memory, LangSmith LLM-as-judge evaluation, a PyRIT red-team dashboard, Terraform infrastructure and a GitHub Actions deployment to ECS.
- **External services and expected cost:** real AWS infrastructure (ECS, RDS Postgres, ElastiCache, Bedrock, Secrets Manager) that bills by the hour — run `terraform destroy` when done; OpenAI and Groq via TensorZero; LangSmith.
- **Tests / offline demo:** no tests; the PyRIT dashboard and LangSmith judge are the runtime checks.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

Follow [CODE/README.md](CODE/README.md): configure the AWS CLI, run `bootstrap.sh` once, then `terraform apply` in `CODE/terraform/`; GitHub Actions builds and deploys the images. Upstream project: the link in `GITHUB LINK/`.
