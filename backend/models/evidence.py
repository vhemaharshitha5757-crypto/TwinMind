from pydantic import BaseModel, Field
from typing import List, Dict, Any
from datetime import datetime
class Evidence(BaseModel):
    evidence_id: str
    modality: str          # document | image | audio

    source_file: str

    raw_text: str

    entities: Dict[str, List[str]] = Field(default_factory=dict)

    metadata: Dict[str, Any] = Field(default_factory=dict)

    extracted_at: datetime = Field(default_factory=datetime.utcnow)

    confidence: float = 1.0