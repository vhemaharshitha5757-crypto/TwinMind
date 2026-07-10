from pydantic import BaseModel, Field
from typing import List


class TimelineEvent(BaseModel):
    time: str
    event: str


class ProcessedSections(BaseModel):

    symptoms: List[str] = Field(default_factory=list)

    timeline: List[TimelineEvent] = Field(default_factory=list)

    root_causes: List[str] = Field(default_factory=list)

    resolutions: List[str] = Field(default_factory=list)

    sops: List[str] = Field(default_factory=list)
