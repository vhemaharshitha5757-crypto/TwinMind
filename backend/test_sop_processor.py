from parsers.document_parser import DocumentParser
from entity.section_extractor import SectionExtractor
from entity.processors.sop_processor import SOPProcessor

parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

sections = SectionExtractor().extract(evidence.raw_text)

processor = SOPProcessor()

sops = processor.process(
    sections["sops"]
)

print("\n" + "=" * 60)
print("STANDARD OPERATING PROCEDURES")
print("=" * 60)

for sop in sops:
    print("-", sop)
