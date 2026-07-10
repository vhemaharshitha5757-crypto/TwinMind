from parsers.document_parser import DocumentParser

from entity.section_extractor import SectionExtractor

from entity.processors.symptom_processor import SymptomProcessor


parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

sections = SectionExtractor().extract(
    evidence.raw_text
)

processor = SymptomProcessor()

symptoms = processor.process(
    sections["symptoms"]
)

print()

print("=" * 60)

print("SYMPTOMS")

print("=" * 60)

for symptom in symptoms:

    print("-", symptom)
