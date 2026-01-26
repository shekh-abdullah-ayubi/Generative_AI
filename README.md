# LangGraph RAG Agent API

A production-ready FastAPI application that combines LangGraph, Retrieval-Augmented Generation (RAG), and multiple LLM integrations (Groq, web search via Tavily) with Pinecone vector database.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Installation & Setup](#installation--setup)
  - [Option 1: Docker with Colima (macOS older than Sonoma)](#option-1-docker-with-colima-macos-older-than-sonoma)
  - [Option 2: Docker Desktop (macOS Sonoma+/Windows/Linux)](#option-2-docker-desktop-macos-sonoma-windowslinux)
  - [Option 3: Local Development (No Docker)](#option-3-local-development-no-docker)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Management Commands](#management-commands)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [For Other Developers](#for-other-developers)

---

## Features

✨ **LangGraph Integration**: State machine-based agentic workflows
🔍 **RAG System**: Document upload and semantic search via Pinecone
🌐 **Web Search**: Real-time information retrieval using Tavily
🤖 **Multi-LLM Support**: Groq for fast LLM inference
📊 **Structured Output**: Pydantic models for API contracts
🏥 **Health Checks**: Built-in health monitoring
📝 **Session Management**: In-memory checkpoint persistence

---

## Prerequisites

### Common Requirements (All Platforms)

- **Git** - Version control
- **Python 3.12+** - For local development option
- **API Keys** (required):
  - [Groq API Key](https://console.groq.com)
  - [Pinecone API Key](https://www.pinecone.io)
  - [Tavily API Key](https://tavily.com)

### Platform-Specific Requirements

#### macOS
- **Option A (Colima)**: Homebrew installed, Colima
- **Option B (Docker Desktop)**: macOS Sonoma or later, Docker Desktop

#### Linux
- Docker or Podman
- Docker Compose

#### Windows
- Docker Desktop for Windows
- Windows Subsystem for Linux 2 (WSL2) recommended

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

# 2. Copy environment template
cp example_dotenv .env

# 3. Edit .env and add your API keys
nano .env

# 4. Build and run with Docker
docker compose up -d --build

# 5. Verify it's running
curl http://localhost:8000/health
```

---

## Installation & Setup

### Option 1: Docker with Colima (macOS older than Sonoma)

**Use this if you're on macOS older than Sonoma.**

#### Step 1: Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install Colima

```bash
brew install colima
```

#### Step 3: Start Colima

```bash
colima start
```

**Note**: First start takes a few minutes. You can verify it's running with:

```bash
colima status
```

#### Step 4: Verify Docker Installation

```bash
docker --version
docker ps
```

#### Step 5: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
```

#### Step 6: Configure Environment

Copy the example environment file and add your API keys:

```bash
cp example_dotenv .env
```

Edit `.env` with your API keys:

```bash
nano .env
```

Add the following variables:

```env
GROQ_API_KEY="your_groq_api_key"
PINECONE_API_KEY="your_pinecone_api_key"
PINECONE_ENVIRONMENT="us-east-1"
PINECONE_PROJECT_NAME="Agent-AI"
TAVILY_API_KEY="your_tavily_api_key"
FASTAPI_BASE_URL="http://localhost:8000"
```

#### Step 7: Build and Run

Execute the following command to build the image and start the container:

```bash
docker compose up -d --build
```

The `-d` flag runs the container in the background. The `--build` flag ensures any changes to the Dockerfile are applied.

#### Step 8: Verify Application

```bash
curl http://localhost:8000/health
# Expected response: {"status": "ok"}
```

---

### Option 2: Docker Desktop (macOS Sonoma+/Windows/Linux)

#### Step 1: Install Docker Desktop

**macOS**: 
- Requires **macOS Sonoma or later**
- Download from [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop)

**Windows**:
- Download [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
- Enable WSL 2 during installation

**Linux** (Ubuntu example):
```bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
sudo usermod -aG docker $USER
# Log out and back in to apply changes
```

#### Step 2: Start Docker Desktop

- **macOS/Windows**: Open Docker Desktop application
- **Linux**: Docker daemon should start automatically

#### Step 3: Verify Installation

```bash
docker --version
docker ps
```

#### Step 4: Clone the Repository

```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
```

#### Step 5: Configure Environment

```bash
cp example_dotenv .env
```

Edit `.env` and add your API keys (see Option 1, Step 6).

#### Step 6: Build and Run

```bash
docker compose up -d --build
```

#### Step 7: Verify Application

```bash
curl http://localhost:8000/health
# Expected response: {"status": "ok"}
```

---

### Option 3: Local Development (No Docker)

**Use this for development without containerization.**

#### Step 1: Clone Repository

```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
```

#### Step 2: Create Python Virtual Environment

```bash
python3.12 -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```

#### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**If you get timeout errors**, try:
```bash
pip install --default-timeout=1000 -r requirements.txt
```

#### Step 4: Configure Environment

```bash
cp example_dotenv .env
```

Edit `.env` and add your API keys (see Option 1, Step 6).

#### Step 5: Run FastAPI Application

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output**:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

#### Step 6: Access API Documentation

Open your browser and navigate to:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🖥️ Usage

Once the container is running, you can access the application at:

| Service | URL |
|---------|-----|
| **Live App** | http://localhost:8000 |
| **Interactive API Docs (Swagger)** | http://localhost:8000/docs |
| **Alternative API Docs (ReDoc)** | http://localhost:8000/redoc |
| **Health Check** | http://localhost:8000/health |

---

## 🛑 Management Commands

| Action | Command |
|--------|---------|
| **Stop containers** | `docker compose stop` |
| **Start existing containers** | `docker compose start` |
| **View logs** | `docker compose logs -f` |
| **View app logs only** | `docker compose logs -f app` |
| **Remove containers & networks** | `docker compose down` |
| **Rebuild after code changes** | `docker compose up -d --build` |
| **Check running containers** | `docker ps` |
| **Check all containers** | `docker ps -a` |

---

## API Endpoints

### 1. Health Check

**Endpoint**: `GET /health`

```bash
curl http://localhost:8000/health
```

**Response**:
```json
{"status": "ok"}
```

---

### 2. Upload Document

**Endpoint**: `POST /upload-document/`

Upload a PDF document to the knowledge base.

```bash
curl -X POST http://localhost:8000/upload-document/ \
  -F "file=@/path/to/your/document.pdf"
```

**Response**:
```json
{
  "message": "PDF 'document.pdf' successfully uploaded and indexed.",
  "filename": "document.pdf",
  "processed_chunks": 5
}
```

**Supported Formats**: PDF (.pdf)

---

### 3. Chat with Agent

**Endpoint**: `POST /chat/`

Send a query to the agent with optional web search toggle.

```bash
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "user-session-123",
    "query": "What is the treatment for diabetes?",
    "enable_web_search": true
  }'
```

**Request Body**:
```json
{
  "session_id": "string",
  "query": "string",
  "enable_web_search": boolean
}
```

---

## Testing

### 1. Test Health Endpoint

```bash
curl http://localhost:8000/health
```

### 2. Test with Swagger UI

Open browser: **http://localhost:8000/docs**

- Expand endpoints
- Click "Try it out"
- Enter parameters
- Click "Execute"

### 3. Test Chat Endpoint

```bash
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "test-session",
    "query": "Who are you?",
    "enable_web_search": false
  }'
```

### 4. Test Document Upload

```bash
curl -X POST http://localhost:8000/upload-document/ \
  -F "file=@document.pdf"
```

### 5. Integration Test Script

Create `test_api.sh`:

```bash
#!/bin/bash

BASE_URL="http://localhost:8000"

echo "=== Testing Health Endpoint ==="
curl -s "$BASE_URL/health" | jq .

echo -e "\n=== Testing Chat Endpoint ==="
curl -s -X POST "$BASE_URL/chat/" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "test-1",
    "query": "What is artificial intelligence?",
    "enable_web_search": false
  }' | jq .

echo -e "\n=== Tests Complete ==="
```

Run the test:

```bash
chmod +x test_api.sh
./test_api.sh
```

---

## Troubleshooting

### Issue: `docker: command not found` (macOS)

**Solution 1**: Use Colima
```bash
brew install colima
colima start
```

**Solution 2**: Upgrade macOS to Sonoma and install Docker Desktop

---

### Issue: `ModuleNotFoundError: No module named 'rag'`

**Solution**: Ensure all `__init__.py` files exist:
```bash
touch app/__init__.py
touch app/rag/__init__.py
touch app/core/__init__.py
```

Rebuild Docker image:
```bash
docker compose up -d --build
```

---

### Issue: `pip: command not found`

**Solution**:
```bash
# Use python3 -m pip instead
python3 -m pip install -r requirements.txt
```

---

### Issue: Timeout during pip install

**Solution**:
```bash
pip install --default-timeout=1000 -r requirements.txt
```

Or use alternative PyPI mirror:
```bash
pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
```

---

### Issue: `PINECONE_API_KEY` not recognized

**Solution**: 
1. Check `.env` file exists and has correct values
2. Verify environment variables are loaded:
   ```bash
   # In Docker
   docker exec <container-id> env | grep PINECONE
   
   # In local development
   echo $PINECONE_API_KEY
   ```

---

### Issue: Connection refused to `localhost:8000`

**Solution**:
```bash
# Check if container is running
docker ps

# Check logs
docker compose logs app

# Restart services
docker compose restart
```

---

### Issue: Out of Memory (Docker)

**Solution**: Increase Docker memory limit:
- **Docker Desktop**: Preferences → Resources → Memory (increase to 4GB+)
- **Colima**: `colima start --memory 4`

---

## For Other Developers

### Quick Start Guide for Team Members

#### Prerequisites Check

```bash
# Verify Git
git --version

# Verify Docker or Colima
docker --version          # Docker Desktop
colima status            # Colima
```

#### Clone & Setup (5 minutes)

```bash
# 1. Clone repository
git clone <repository-url>
cd <repo-name>

# 2. Copy environment template
cp example_dotenv .env

# 3. Add API keys to .env
nano .env
```

#### Choose Your Setup Path

**Path A: Docker (Recommended)**
```bash
docker compose up -d --build
# Visit: http://localhost:8000/docs
```

**Path B: Local Development**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
# Visit: http://localhost:8000/docs
```

#### Verify Setup

```bash
# Test health endpoint
curl http://localhost:8000/health

# View API documentation in browser
# http://localhost:8000/docs
```

---

### Common Developer Tasks

#### Adding New Dependencies

```bash
# 1. Add to requirements.txt
# 2. Reinstall
pip install -r requirements.txt

# OR in Docker
docker compose up -d --build
```

#### Viewing Logs

```bash
# Docker
docker compose logs -f app

# Local development
# Logs appear in terminal running uvicorn
```

#### Stopping Services

```bash
# Docker
docker compose down

# Local
# Press Ctrl+C
```

#### Git Workflow

```bash
# Pull latest changes
git pull origin main

# Create feature branch
git checkout -b feature/new-feature

# Make changes, then commit
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

---

## Support & Resources

- **Groq Documentation**: https://console.groq.com/docs
- **Pinecone Documentation**: https://docs.pinecone.io
- **Tavily Documentation**: https://docs.tavily.com
- **FastAPI Documentation**: https://fastapi.tiangolo.com
- **LangGraph Documentation**: https://langchain-ai.github.io/langgraph/
- **Docker Documentation**: https://docs.docker.com
- **Colima Documentation**: https://github.com/abiosoft/colima

---

## License

[Add your license information here]

---

**Last Updated**: January 27, 2026
