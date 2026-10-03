# RAG Systems Projects

Five applied RAG builds with LangChain, ordered from a retrieval-only search engine to a multimodal RAG system. The
source was an unordered bucket of notebooks; here each notebook is an ordered module of one project, and the shared
PDFs sit in `data/`.

## Course context

Project 05 of **group 01 (foundational projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 03 (LangChain fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-03-langchain-fundamentals), [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag).
- **What it integrates:** LangChain loaders, splitters, OpenAI embeddings, Chroma and LCEL chains, applied in five progressively larger builds.
- **External services and expected cost:** OpenAI (embeddings + `gpt-4o-mini` through the course LLM factory `aied_helpers.get_openai_llm`); each notebook costs cents. Notebook 01 downloads the open-source `BAAI/bge-reranker-large` cross-encoder (about 1.3 GB) from Hugging Face. Notebooks 03 and 04 download the Simple English Wikipedia dump from sbert.net. Notebook 05 uses Unstructured to partition a PDF into text, tables and images, which needs the system packages Tesseract and Poppler (`brew install tesseract poppler` or `sudo apt-get install tesseract-ocr poppler-utils`), and a Redis server on `localhost:6379` (`brew install redis && brew services start redis`, or `docker run -d -p 6379:6379 redis/redis-stack-server:latest`).
- **Tests / offline demo:** no tests; notebooks only (live, need OpenAI).
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
uv sync                 # creates .venv from pyproject.toml / uv.lock in this folder
cp .env.example .env    # add OPENAI_API_KEY
uv run jupyter lab notebooks/
```

Dependencies live in this folder's `pyproject.toml` / `uv.lock` (`requirements.txt` is exported from the lock); the
notebooks no longer install packages themselves. Notebook 05 reads `data/IF10244.pdf` and downloads it from `https://sgp.fas.org/crs/misc/IF10244.pdf` on its first run.

## Modules

| # | Notebook | What you build |
|---|---|---|
| 01 | [01_build_document_retriever_search_engine.ipynb](notebooks/01_build_document_retriever_search_engine.ipynb) | A document search engine: load JSON and PDF documents, chunk, embed into Chroma, query with similarity search (no generation yet) |
| 02 | [02_rag_system_for_question_answering.ipynb](notebooks/02_rag_system_for_question_answering.ipynb) | Question answering over the three papers in `data/` — the first full retrieve-then-generate pipeline |
| 03 | [03_conversational_rag.ipynb](notebooks/03_conversational_rag.ipynb) | Basic RAG over a Wikipedia subset, why it fails on follow-up questions, then conversational RAG: a history-aware retriever plus a chat history passed in on every turn |
| 04 | [04_multi_user_conversational_rag_system.ipynb](notebooks/04_multi_user_conversational_rag_system.ipynb) | Multi-user conversational RAG: per-session chat histories in SQLite (`SQLChatMessageHistory`), a last-K message window and `RunnableWithMessageHistory`, checked with two interleaved users |
| 05 | [05_multimodal_rag_with_gpt_4o.ipynb](notebooks/05_multimodal_rag_with_gpt_4o.ipynb) | Multimodal RAG: partition a PDF into text, tables and images, summarise each, index with a multi-vector retriever (Chroma + Redis), answer with `gpt-4o-mini` (multimodal, GPT-4o family) |

**Why this order.** Retrieval alone (01) before generation (02); single-turn (02) before conversation and multiple
users (03, 04); text before images and tables (05). Notebook 03 makes one conversation work; 04 keeps a separate,
SQL-backed history for every user. Each notebook builds its own data and vector store, so any of them runs on its own.

`data/` holds *Attention Is All You Need* (`1706.03762v7.pdf`), the RAG paper (`2005.11401v4.pdf`), the GPT-3 paper
(`2005.14165v4.pdf`) and a small Wikipedia sample (`wikidata_rag_demo.jsonl`).
