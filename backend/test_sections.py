from parsers.document_parser import DocumentParser
from entity.section_extractor import SectionExtractor

parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

extractor = SectionExtractor()

sections = extractor.extract(evidence.raw_text)

for name, value in sections.items():

    print("=" * 80)
    print(name.upper())
    print("=" * 80)

    print(value[:300])      # Preview first 300 chars
    print()
