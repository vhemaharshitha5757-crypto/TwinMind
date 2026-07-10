from parsers.document_parser import DocumentParser
from entity.section_extractor import SectionExtractor
from entity.processors.resolution_processor import ResolutionProcessor

parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

sections = SectionExtractor().extract(evidence.raw_text)

processor = ResolutionProcessor()

resolution = processor.process(
    sections["resolution"]
)

print("\n" + "=" * 60)
print("RESOLUTION")
print("=" * 60)

for item in resolution:
    print("-", item)
