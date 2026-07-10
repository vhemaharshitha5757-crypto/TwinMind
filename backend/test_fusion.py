from parsers.document_parser import DocumentParser
from parsers.image_parser import ImageParser
from parsers.audio_parser import AudioParser

from entity.knowledge_extractor import KnowledgeExtractor
from entity.image_knowledge_extractor import ImageKnowledgeExtractor
from entity.audio_knowledge_extractor import AudioKnowledgeExtractor

from fusion.fusion_engine import FusionEngine


# ============================
# DOCUMENT
# ============================

document_parser = DocumentParser()

document_evidence = document_parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

document_knowledge = KnowledgeExtractor().extract(
    document_evidence.raw_text
)


# ============================
# IMAGE
# ============================

image_parser = ImageParser()

image_evidence = image_parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/image_metadata.json"
)

image_knowledge = ImageKnowledgeExtractor().extract(
    image_evidence
)


# ============================
# AUDIO
# ============================

audio_parser = AudioParser()

audio_evidence = audio_parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/meeting_transcript.txt"
)

audio_knowledge = AudioKnowledgeExtractor().extract(
    audio_evidence
)


# ============================
# FUSION
# ============================

fusion = FusionEngine()

incident = fusion.fuse(
    document_knowledge,
    image_knowledge,
    audio_knowledge
)


# ============================
# OUTPUT
# ============================

print("\n" + "=" * 80)
print("UNIFIED INCIDENT")
print("=" * 80)

print(incident)
