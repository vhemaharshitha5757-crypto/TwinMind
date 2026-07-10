from parsers.document_parser import DocumentParser
from entity.knowledge_extractor import KnowledgeExtractor

from parsers.image_parser import ImageParser
from entity.image_knowledge_extractor import ImageKnowledgeExtractor

from parsers.audio_parser import AudioParser
from entity.audio_knowledge_extractor import AudioKnowledgeExtractor

from fusion.fusion_engine import FusionEngine
from fusion.graph_builder import GraphBuilder


DATASET = "../datasets/TwinMind-Dataset/incidents/INC001"


# Document
doc = DocumentParser().parse(
    f"{DATASET}/incident_report.txt"
)
doc_k = KnowledgeExtractor().extract(doc.raw_text)

# Image
img = ImageParser().parse(
    f"{DATASET}/image_metadata.json"
)
img_k = ImageKnowledgeExtractor().extract(img)

# Audio
aud = AudioParser().parse(
    f"{DATASET}/meeting_transcript.txt"
)
aud_k = AudioKnowledgeExtractor().extract(aud)

incident = FusionEngine().fuse(
    doc_k,
    img_k,
    aud_k
)

graph = GraphBuilder().build(incident)

print("\nNODES\n")

for n in graph.nodes:
    print(n)

print("\nRELATIONS\n")

for r in graph.relations:
    print(r)
