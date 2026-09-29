# Autogen_Stock_Analysis

## Course context

Project 10 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals), [repository 11 (alternative agent frameworks)](https://github.com/Sourav692/ai-engineering-demystified-11-alternative-agent-frameworks).
- **What it integrates:** AG2/AutoGen assistant and user-proxy agents (finance-report analyst, technical analyst, strategy agent, supervisor) with yfinance tools and a local code executor, behind a Streamlit UI; the course slides (`Module 1`–`Module 5`, `PDFs/`) walk through the build.
- **External services and expected cost:** OpenAI (`gpt-4.1-nano` — a fraction of a cent per analysis); yfinance is free.
- **Tests / offline demo:** no tests.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
pip install streamlit openai python-dotenv yfinance ag2   # the list in Autogen_Stock_Analysis-main.zip's requirements.txt
cp .env.example .env    # add OPENAI_API_KEY
streamlit run app.py
```

`Autogen_Stock_Analysis-main.zip` is the upstream download of this same code (CRLF line endings) plus its `requirements.txt`, which lists `autogen` — the AG2 package that provides `autogen.agentchat`.
