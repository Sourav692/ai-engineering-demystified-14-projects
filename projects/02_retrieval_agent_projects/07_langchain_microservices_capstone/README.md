# LangChain Microservices Capstone

## Course context

Project 07 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 03 (LangChain fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-03-langchain-fundamentals), [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag), [repository 13 (production and observability)](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability).
- **What it integrates:** two Python services (a LangChain service and a Postgres-backed FAQ service), a Postgres image, a React (Vite) frontend, Dockerfiles, a local registry script and Kubernetes manifests (deployments, ingress, init SQL).
- **External services and expected cost:** OpenAI; Docker and a local Kubernetes cluster (no cloud cost).
- **Tests / offline demo:** no tests.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
./deployment.sh    # builds the four images, pushes them to a local registry on :5000,
                   # then applies all-deployments.yaml / ingress.yaml (see the script)
```

Create the `openai-secret` and Postgres secrets the manifests reference before applying them.


**Status:** ✅ Built.

Deploying LangChain as microservices — Docker, k8s-style manifests, frontend. Merged from `LangChain_Demystified`'s `12_MicroServices` module.
