from parsers.document_parser import DocumentParser
from entity.section_extractor import SectionExtractor
from entity.processors.timeline_processor import TimelineProcessor


parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

sections = SectionExtractor().extract(evidence.raw_text)

processor = TimelineProcessor()

timeline = processor.process(sections["timeline"])

print("\n" + "=" * 60)
print("TIMELINE")
print("=" * 60)

for item in timeline:
    print(f"{item['time']}  ->  {item['event']}")
