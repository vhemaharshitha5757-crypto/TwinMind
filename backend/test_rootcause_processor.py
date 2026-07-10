from parsers.document_parser import DocumentParser
from entity.section_extractor import SectionExtractor
from entity.processors.rootcause_processor import RootCauseProcessor


parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

sections = SectionExtractor().extract(
    evidence.raw_text
)

processor = RootCauseProcessor()

causes = processor.process(
    sections["root_cause"]
)

print()

print("=" * 60)
print("ROOT CAUSE")
print("=" * 60)

for cause in causes:
    print("-", cause)
