# End-to-End Medical Chatbot

## Course context

Project 03 of **group 02 (retrieval and agent projects)** in *AI Engineering Demystified — 14 Projects*. This project applies earlier repositories; it does not re-teach them, and it runs in its own environment.

- **Prerequisites (knowledge):** [repository 03 (LangChain fundamentals)](https://github.com/Sourav692/ai-engineering-demystified-03-langchain-fundamentals), [repository 05 (retrieval and RAG)](https://github.com/Sourav692/ai-engineering-demystified-05-retrieval-rag), [repository 13 (production and observability)](https://github.com/Sourav692/ai-engineering-demystified-13-production-observability).
- **What it integrates:** PDF ingestion of a medical encyclopedia, Hugging Face embeddings, a Pinecone index, a Groq-backed LangChain retrieval chain, a Flask chat UI, Docker, and two deployment paths (AWS ECR/EC2 via GitHub Actions, and Databricks Apps).
- **External services and expected cost:** Pinecone (free starter index), Groq; AWS EC2/ECR or Databricks Apps only if you deploy (those bill by uptime).
- **Tests / offline demo:** no tests; `research/demo.ipynb` is the exploratory build (live).
- **Environment variables:** copy [.env.example](.env.example) to `.env` and fill in what you use; never commit `.env`.

### How to run

```bash
uv sync                           # creates .venv from pyproject.toml / uv.lock
cp .env.example .env              # add PINECONE_API_KEY and GROQ_API_KEY
uv run jupyter lab research/demo.ipynb   # exploratory build
uv run python store_index.py      # embed data/Medical_book.pdf into Pinecone
uv run python app.py              # http://localhost:8080
```

The original README below mentions OpenAI; the code now uses Groq. [DATABRICKS_APP_DEPLOYMENT.md](DATABRICKS_APP_DEPLOYMENT.md) covers the Databricks path.


Flask + Pinecone medical RAG chatbot.

# End-to-End-Medical-Chatbot

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-End-Medical-Chatbot
```

### STEP 01- Create the environment after opening the repository

```bash
uv sync
```

### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
uv run python store_index.py
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
- GPT
- Pinecone



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/medicalbot

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - OPENAI_API_KEY
