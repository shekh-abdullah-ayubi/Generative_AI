# Agentic RAG: Modular Search Intelligence Platform

A modular, agent-driven RAG platform built with FastAPI that combines contextual document retrieval and real-time web search to deliver accurate and scalable AI-powered reponses.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Installation & Setup](#installation--setup)
  - [Docker with Colima (macOS older than Sonoma)](#docker-with-colima-macos-older-than-sonoma)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Management Commands](#management-commands)
- [Testing](#testing)

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

### Docker with Colima (macOS older than Sonoma)

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


## Usage

Once the container is running, you can access the application at:

| Service | URL |
|---------|-----|
| **Live App** | http://localhost:8000 |
| **Interactive API Docs (Swagger)** | http://localhost:8000/docs |
| **Alternative API Docs (ReDoc)** | http://localhost:8000/redoc |
| **Health Check** | http://localhost:8000/health |

---

## Management Commands

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

