# Build context: this project folder.
# Run: docker build -t deep-agent .

FROM node:20-slim AS frontend-build

WORKDIR /frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build


FROM python:3.12-slim

WORKDIR /app

# Backend deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Backend source
COPY backend/ ./backend/

# Skills (loaded by the deep agent at runtime)
COPY skills/ ./skills/

# Built frontend (served as static files by FastAPI)
COPY --from=frontend-build /frontend/build ./frontend/build/

EXPOSE 8000

CMD ["uvicorn", "deep_agent.main:app", "--app-dir", "backend/src", "--host", "0.0.0.0", "--port", "8000"]
