from ai.gemini_service import GeminiService
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

import os
import shutil
from typing import Optional

from parsers.document_parser import DocumentParser
from parsers.image_parser import ImageParser
from parsers.audio_parser import AudioParser

from entity.knowledge_extractor import KnowledgeExtractor
from entity.image_knowledge_extractor import ImageKnowledgeExtractor
from entity.audio_knowledge_extractor import AudioKnowledgeExtractor

from fusion.fusion_engine import FusionEngine
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="TwinMind API",
    version="1.0.0",
    description="Multi-modal Incident Intelligence Backend"
)
gemini = GeminiService()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "TwinMind Backend Running Successfully"
    }


@app.post("/process")
async def process_incident(
    document: Optional[UploadFile] = File(None),
    image: Optional[UploadFile] = File(None),
    audio: Optional[UploadFile] = File(None),
):

    if document is None and image is None and audio is None:
        raise HTTPException(
            status_code=400,
            detail="Upload at least one file."
        )

    knowledge_list = []

    # -------------------------------
    # Document
    # -------------------------------
    if document:

        document_path = os.path.join(
            UPLOAD_FOLDER,
            document.filename
        )

        with open(document_path, "wb") as buffer:
            shutil.copyfileobj(document.file, buffer)

        evidence = DocumentParser().parse(document_path)

        knowledge = KnowledgeExtractor().extract(evidence)

        knowledge_list.append(knowledge)

    # -------------------------------
    # Image
    # -------------------------------
    if image:

        image_path = os.path.join(
            UPLOAD_FOLDER,
            image.filename
        )

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        evidence = ImageParser().parse(image_path)

        knowledge = ImageKnowledgeExtractor().extract(evidence)

        knowledge_list.append(knowledge)

    # -------------------------------
    # Audio
    # -------------------------------
    if audio:

        audio_path = os.path.join(
            UPLOAD_FOLDER,
            audio.filename
        )

        with open(audio_path, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        evidence = AudioParser().parse(audio_path)

        knowledge = AudioKnowledgeExtractor().extract(evidence)

        knowledge_list.append(knowledge)

    # -------------------------------
    # Fusion
    # -------------------------------
    if len(knowledge_list) == 1:

        incident = knowledge_list[0]

    else:

        incident = FusionEngine().fuse(*knowledge_list)

    return JSONResponse(
        content=incident.model_dump()
    )
from pydantic import BaseModel

class ChatRequest(BaseModel):
    incident: dict
    question: str

from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
    incident: dict

from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
    incident: dict

@app.post("/chat")
async def chat(data: ChatRequest):

    answer = gemini.ask(
        data.question,
        data.incident
    )

    return {
        "answer": answer
    }
