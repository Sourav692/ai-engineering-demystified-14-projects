# ShopUNow Agentic RAG Capstone

A multi-user, multi-department conversational assistant for the fictional retailer ShopUNow: questions are categorised to one of seven departments, answered from that department's vector store, checked for hallucination, and remembered per user. Built for the "Agentic AI Pioneer" capstone brief (`Capstone Project - Agentic AI Pioneer.pdf`); `ShopUNow_Agentic_RAG_Architecture.pptx` is the architecture deck and `sample_data.py` shows how the department Q&A data was generated.

## Course context

Project 02 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 04 (LangGraph fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-04-langgraph-fundamentals), [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag), [repository 08 (advanced agent systems)](https://github.com/Sourav692/ai-engineering-demystified-08-advanced-agent-systems), [repository 09 (advanced RAG)](https://github.com/Sourav692/ai-engineering-demystified-09-advanced-rag).
- **What it integrates:** seven per-department Chroma vector stores and a LangGraph agentic RAG graph (query categorisation, retrieval, generation, hallucination check) with MemorySaver/SqliteSaver multi-user conversation memory.
- **External services and expected cost:** whichever provider the bundled `helpers` factory selects — Databricks model serving by default (`DATABRICKS_HOST`/`DATABRICKS_TOKEN`), or OpenAI/Groq; a full run costs cents.
- **Tests / offline demo:** no tests; the two notebooks build and query the system (live).
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
uv sync                # creates .venv from pyproject.toml / uv.lock
cp .env.example .env
uv run jupyter lab     # run 01_create_vector_databases.ipynb, then 02_agentic_rag_system.ipynb
```

The notebooks import `helpers.utils` (the course's LLM/embedding factory); a copy ships in `helpers/` beside them. `pyproject.toml` declares what the notebooks and `helpers` import; `uv.lock` pins it (`requirements.txt` is an export of the lock). [WALKTHROUGH.md](WALKTHROUGH.md) explains every node.
