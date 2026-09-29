# Personalized Holiday Management Agent

## Course context

Project 03 of **group 01 (foundational projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 01 (foundations)](https://github.com/Sourav692/ai-engineering-demystified-01-foundations), [repository 06 (agent fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-06-agent-fundamentals), [repository 11 (alternative agent frameworks)](https://github.com/Sourav692/ai-engineering-demystified-11-alternative-agent-frameworks).
- **What it integrates:** an AutoGen AgentChat planner + researcher round-robin team served by a FastAPI endpoint with a static web page.
- **External services and expected cost:** OpenAI (`gpt-4o`); one plan costs a few cents.
- **Tests / offline demo:** no tests; `python main.py` runs one plan end to end (live, needs OpenAI).
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
pip install -r requirements.txt   # also installs this package (-e .)
cp .env.example .env              # add OPENAI_API_KEY
uvicorn app:app --reload          # http://localhost:8000
python main.py                    # one plan in the terminal
```


FastAPI + AutoGen AgentChat (planner + researcher round-robin) for personalized holiday plans. Distinct from CrewAI's travel-advisor notebooks in repository 11 (alternative agent frameworks).

# Personalized-Holiday-Management-Agent 


1. Create a Virtual Environment
   ```bash
   conda create -n holiday_agent python=3.12 -y
   ```

2. Activate the Virtual Environment
   ```bash 
    conda activate holiday_agent
    ```

3. Install Required Packages
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI Application
    ```bash
      uvicorn app:app --reload

      ```