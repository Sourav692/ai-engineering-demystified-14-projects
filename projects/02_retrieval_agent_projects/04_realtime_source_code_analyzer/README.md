# Source-Code-Analysis-Project

## Course context

Project 04 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 03 (LangChain fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-03-langchain-fundamentals), [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag).
- **What it integrates:** cloning a GitHub repository, language-aware code splitting, OpenAI embeddings in Chroma and a ConversationalRetrievalChain with summary memory, behind a Flask UI.
- **External services and expected cost:** OpenAI; indexing a small repository and chatting costs cents.
- **Tests / offline demo:** no tests; `research/trials.ipynb` is the exploratory build (live).
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
uv sync
cp .env.example .env    # add OPENAI_API_KEY
uv run python app.py
```



# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```
### STEP 01- Create the environment and install the requirements (from this project's folder)

```bash
uv sync
```


### Create a `.env` file in the root directory and add your OPENAI_API_KEY credentials as follows:

```ini
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Finally run the following command
uv run python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- OpenAI
- GPT 3
- ChoromaDB