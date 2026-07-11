# TwinMind

TwinMind is an incident intelligence platform that transforms multi-modal incident evidence into a structured incident summary, a timeline, a knowledge graph view, and an AI-powered assistant for investigation.

## What TwinMind does

TwinMind helps operations, support, and SRE teams analyze incident evidence from multiple sources:

- incident reports in text form
- screenshot metadata or image-based evidence
- meeting transcripts or audio-derived evidence

The system parses these assets, extracts structured knowledge, fuses the information into a single incident object, and presents it through a web dashboard.

## Proposed solution

TwinMind provides a practical incident-response workflow:

1. Upload one or more evidence artifacts.
2. The backend parses and extracts facts from each modality.
3. The system fuses the extracted knowledge into a unified incident profile.
4. The frontend displays the summary, timeline, and AI assistant experience.
5. Users can ask questions such as root cause, resolution steps, symptoms, and SOP references.

## Target users

TwinMind is intended for:

- Site Reliability Engineers (SREs)
- DevOps and operations teams
- Incident managers and support engineers
- Organizations handling complex multi-step incidents

## System architecture

The application is split into a frontend and a backend service:

- Frontend: React + Vite dashboard for upload, visualization, and chat
- Backend: FastAPI service for processing uploaded evidence and exposing API endpoints
- AI layer: LLM-based assistant using OpenRouter-compatible models
- Knowledge processing: parsers, extractors, and fusion engine for combining evidence from text, image, and audio inputs
- Optional graph capability: Neo4j integration is included for graph-based storage and relationship insights

### High-level flow

```text
User uploads incident artifacts
        ↓
FastAPI backend receives files
        ↓
Document / image / audio parsers extract evidence
        ↓
Knowledge extractors structure the findings
        ↓
Fusion engine combines evidence into one incident model
        ↓
React dashboard renders summary, timeline, and AI assistant
```

## Tech stack

### Frontend
- React 19
- Vite
- Axios
- Lucide React

### Backend
- Python
- FastAPI
- Pydantic
- Python multipart
- Uvicorn
- OpenAI-compatible client
- Neo4j driver

### AI / inference
- OpenRouter-compatible LLM access
- Fallback model chain for free public models

## Project structure

```text
backend/
  app.py                 # FastAPI application and API routes
  ai/                    # AI service layer
  entity/                # knowledge extraction and normalization logic
  fusion/                # fusion and confidence scoring logic
  parsers/               # parsers for document, image, and audio data
  services/              # supporting services such as Neo4j integration
  tests/                 # backend test suite
frontend/
  src/
    components/          # UI components including upload and AI assistant
    pages/               # dashboard page
    services/            # frontend API hooks and service modules
```

## Environment requirements

- Python 3.10+ recommended
- Node.js 18+ recommended
- Access to an OpenRouter API key for the AI chat assistant

## How to run the project

### 1. Backend

From the project root:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create or update the backend environment file if needed:

```text
backend/.env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Start the backend:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

The API will be available at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

### 2. Frontend

In a new terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend will typically run at:

- http://localhost:5173/

## How to use the application

1. Open the frontend in your browser.
2. Upload an incident report, screenshot metadata file, or meeting transcript.
3. Click Analyze Incident.
4. Review the generated incident summary, timeline, and confidence information.
5. Use the TwinMind AI Copilot panel to ask questions about the incident.

## Expected output

After analysis, the app can produce:

- a structured incident summary
- affected systems and components
- severity and confidence score
- timeline of key events
- root cause and resolution information
- a chat-based AI assistant response grounded in the parsed incident data

## Notes

- The current AI chat experience uses an OpenRouter-compatible model chain and is designed to answer only from the incident context provided.
- The Neo4j graph service is available as an optional persistence layer for knowledge graph storage.
- Sample incident data is available under the datasets folder for experimentation.
