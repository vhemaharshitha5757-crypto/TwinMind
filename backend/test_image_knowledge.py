from parsers.image_parser import ImageParser

from entity.image_knowledge_extractor import ImageKnowledgeExtractor


parser = ImageParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/image_metadata.json"
)

extractor = ImageKnowledgeExtractor()

knowledge = extractor.extract(evidence)

print(knowledge)
