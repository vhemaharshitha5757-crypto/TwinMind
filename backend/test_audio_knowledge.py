from parsers.audio_parser import AudioParser

from entity.audio_knowledge_extractor import AudioKnowledgeExtractor


parser = AudioParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/meeting_transcript.txt"
)

extractor = AudioKnowledgeExtractor()

knowledge = extractor.extract(evidence)

print(knowledge)
