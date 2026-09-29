# AutoGen Data Analyzer GPT

Upload a CSV and ask a question: a data-analyst agent plans and writes Python, a code-executor agent runs it inside a Docker container, and the pair iterate until the answer (and any chart, saved as `temp/output.png`) is ready. `Data Analyst Automation.excalidraw` is the design sketch.

## Course context

Project 11 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals), [repository 11 (alternative agent frameworks)](https://github.com/Sourav692/ai-engineering-demystified-11-alternative-agent-frameworks).
- **What it integrates:** an AutoGen AgentChat team (data-analyst agent + Docker code-executor agent) that plans, writes and runs pandas/matplotlib code against an uploaded CSV, with a Streamlit front end.
- **External services and expected cost:** OpenAI; Docker must be running locally for the code executor.
- **Tests / offline demo:** no tests.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
pip install autogen-agentchat "autogen-ext[openai,docker]" streamlit python-dotenv
cp .env.example "Analyser GPT/.env"    # add OPENAI_API_KEY
cd "Analyser GPT"
streamlit run streamlit_app.py      # upload a CSV; it is saved to temp/data.csv
```

The package list is what the code imports (the project has no manifest). The lesson that explains this project's folder structure (`1. Project Structure.ipynb`) stays with the AutoGen applications module of repository 11; the run outputs that were committed under `temp/` are not shipped — the app recreates the folder.
