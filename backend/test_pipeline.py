from parsers.document_parser import DocumentParser

from entity.section_extractor import SectionExtractor
from entity.processor_pipeline import ProcessorPipeline


parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

sections = SectionExtractor().extract(
    evidence.raw_text
)

pipeline = ProcessorPipeline()

processed = pipeline.process(sections)

print(processed)
