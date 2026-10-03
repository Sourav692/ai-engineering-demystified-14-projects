# RAG Systems Projects

Five applied RAG builds with LangChain, ordered from a retrieval-only search engine to a multimodal RAG system. The
source was an unordered bucket of notebooks; here each notebook is an ordered module of one project, and the shared
PDFs sit in `data/`.

## Course context

Project 05 of **group 01 (foundational projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 03 (LangChain fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-03-langchain-fundamentals), [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag).
- **What it integrates:** LangChain loaders, splitters, OpenAI embeddings, Chroma and LCEL chains, applied in five progressively larger builds.
- **External services and expected cost:** OpenAI (embeddings + GPT-4o/4o-mini); each notebook costs cents. Notebook 05 also uses Unstructured to partition a PDF into text, tables and images.
- **Tests / offline demo:** no tests; notebooks only (live, need OpenAI).
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
uv sync                 # creates .venv from pyproject.toml / uv.lock in this folder
cp .env.example .env    # add OPENAI_API_KEY (or paste it when a notebook asks)
uv run jupyter lab notebooks/
```

Dependencies live in this folder's `pyproject.toml` / `uv.lock` (`requirements.txt` is exported from the lock); the
notebooks no longer install packages themselves. Notebook 05 reads `data/IF10244.pdf`, which you download first: `https://sgp.fas.org/crs/misc/IF10244.pdf` (the notebook's own commented `wget` cell).

## Modules

| # | Notebook | What you build |
|---|---|---|
| 01 | [01_build_document_retriever_search_engine.ipynb](notebooks/01_build_document_retriever_search_engine.ipynb) | A document search engine: load JSON and PDF documents, chunk, embed into Chroma, query with similarity search (no generation yet) |
| 02 | [02_rag_system_for_question_answering.ipynb](notebooks/02_rag_system_for_question_answering.ipynb) | Question answering over the three papers in `data/` — the first full retrieve-then-generate pipeline |
| 03 | [03_simple_conversational_and_multi_user_rag.ipynb](notebooks/03_simple_conversational_and_multi_user_rag.ipynb) | Three steps in one notebook: basic RAG, conversational RAG with question contextualisation, then per-user chat histories |
| 04 | [04_multi_user_conversational_rag_system.ipynb](notebooks/04_multi_user_conversational_rag_system.ipynb) | The multi-user conversational system as a standalone build (history-aware retriever + session-keyed message stores) |
| 05 | [05_multimodal_rag_with_gpt_4o.ipynb](notebooks/05_multimodal_rag_with_gpt_4o.ipynb) | Multimodal RAG: partition a PDF into text, tables and images, summarise each, index with a multi-vector retriever, answer with GPT-4o |

**Why this order.** Retrieval alone (01) before generation (02); single-turn (02) before conversation and multiple
users (03, 04); text before images and tables (05). Notebook 03 introduces the three conversational steps together and
04 rebuilds the multi-user case on its own, so 04 doubles as a self-check after 03.

`data/` holds *Attention Is All You Need* (`1706.03762v7.pdf`), the RAG paper (`2005.11401v4.pdf`), the GPT-3 paper
(`2005.14165v4.pdf`) and a small Wikipedia sample (`wikidata_rag_demo.jsonl`).
