from pydantic import BaseModel, Field
from typing import List


class UnifiedIncident(BaseModel):

    incident_id: str = ""

    title: str = ""

    severity: str = ""

    systems: List[str] = Field(default_factory=list)

    components: List[str] = Field(default_factory=list)

    engineers: List[str] = Field(default_factory=list)

    departments: List[str] = Field(default_factory=list)

    locations: List[str] = Field(default_factory=list)

    symptoms: List[str] = Field(default_factory=list)

    root_causes: List[str] = Field(default_factory=list)

    resolutions: List[str] = Field(default_factory=list)

    sops: List[str] = Field(default_factory=list)

    timeline: List[str] = Field(default_factory=list)

    confidence: float = 0.0

    sources: List[str] = Field(default_factory=list)
