from parsers.document_parser import DocumentParser

from entity.knowledge_extractor import KnowledgeExtractor


parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

extractor = KnowledgeExtractor()

knowledge = extractor.extract(
    evidence.raw_text
)

print(knowledge)
