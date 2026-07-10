from pydantic import BaseModel, Field
from typing import List, Dict, Any


class UnifiedIncident(BaseModel):
    incident_id: str
    title: str
    summary: str
    severity: str

    department: str = ""

    systems: List[str] = Field(default_factory=list)
    engineers: List[str] = Field(default_factory=list)
    symptoms: List[str] = Field(default_factory=list)

    root_cause: str = ""
    resolution: str = ""

    timeline: List[Dict[str, Any]] = Field(default_factory=list)

    evidence: List[str] = Field(default_factory=list)

    confidence: float = 0.0
