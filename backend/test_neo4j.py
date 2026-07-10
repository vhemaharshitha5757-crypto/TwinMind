from parsers.document_parser import DocumentParser
from parsers.image_parser import ImageParser
from parsers.audio_parser import AudioParser

from entity.knowledge_extractor import KnowledgeExtractor
from entity.image_knowledge_extractor import ImageKnowledgeExtractor
from entity.audio_knowledge_extractor import AudioKnowledgeExtractor

from fusion.fusion_engine import FusionEngine
from fusion.graph_builder import GraphBuilder

from services.neo4j_service import Neo4jService


# =====================================================
# DATASET PATH
# =====================================================

BASE_PATH = "../datasets/TwinMind-Dataset/incidents/INC001/"


# =====================================================
# PARSERS
# =====================================================

document_parser = DocumentParser()
image_parser = ImageParser()
audio_parser = AudioParser()


# =====================================================
# DOCUMENT
# =====================================================

document = document_parser.parse(
    BASE_PATH + "incident_report.txt"
)

document_knowledge = KnowledgeExtractor().extract(document)


# =====================================================
# IMAGE
# =====================================================

image = image_parser.parse(
    BASE_PATH + "image_metadata.json"
)

image_knowledge = ImageKnowledgeExtractor().extract(image)


# =====================================================
# AUDIO
# =====================================================

audio = audio_parser.parse(
    BASE_PATH + "meeting_transcript.txt"
)

audio_knowledge = AudioKnowledgeExtractor().extract(audio)


# =====================================================
# FUSION
# =====================================================

fusion_engine = FusionEngine()

incident = fusion_engine.fuse(
    document_knowledge,
    image_knowledge,
    audio_knowledge
)

print("\n==============================")
print("UNIFIED INCIDENT")
print("==============================")
print(incident)


# =====================================================
# GRAPH BUILDING
# =====================================================

graph_builder = GraphBuilder()

graph = graph_builder.build(incident)

print("\n==============================")
print("GRAPH")
print("==============================")

print(f"Nodes : {len(graph.nodes)}")
print(f"Relations : {len(graph.relations)}")


# =====================================================
# STORE IN NEO4J
# =====================================================

neo4j = Neo4jService(
    uri="bolt://127.0.0.1:7687",
    user="neo4j",
    password="password"
)

neo4j.store_graph(graph)

neo4j.close()

print("\n✅ Graph stored successfully in Neo4j.")
