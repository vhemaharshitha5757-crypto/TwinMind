from pydantic import BaseModel
from typing import List


class GraphNode(BaseModel):
    label: str
    name: str


class GraphRelation(BaseModel):
    source: str
    target: str
    relation: str


class GraphData(BaseModel):
    nodes: List[GraphNode] = []
    relations: List[GraphRelation] = []
