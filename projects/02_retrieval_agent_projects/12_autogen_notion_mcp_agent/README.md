# AutoGen Notion MCP Agent

Ask for something in plain English ("list my pages about X", "create a page") and an AutoGen agent carries it out in your Notion workspace through Notion's MCP server. `HLD Project.pdf` and `System_Architecture.png` show the design; `MCP with AutoGen Integrating AI Agents with Notion.pdf` is the course deck.

## Course context

Project 12 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals), [repository 10 (agent protocols)](https://github.com/Sourav692/ai-engineering-demystified-10-agent-protocols), [repository 11 (alternative agent frameworks)](https://github.com/Sourav692/ai-engineering-demystified-11-alternative-agent-frameworks).
- **What it integrates:** an AutoGen AgentChat agent whose tools come from Notion's hosted MCP server (reached through `npx mcp-remote`), wrapped in a Flask API and exposed publicly with an ngrok tunnel.
- **External services and expected cost:** OpenAI (`o4-mini`), a Notion workspace (free), an ngrok account (free tier); Node.js for `npx`.
- **Tests / offline demo:** no tests.
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
pip install autogen-agentchat "autogen-ext[openai,mcp]" flask flask-cors pyngrok
cp .env.example .env    # add OPENAI_API_KEY, NOTION_API_KEY, NGROK_AUTH_TOKEN
python final.py          # Flask on :7001 + ngrok public URL
```

`port.py` and `Pre-requisite - MCP/` are the warm-up steps (a bare Flask + ngrok tunnel, an MCP client). [Reference.md](Reference.md) links the course this follows.
