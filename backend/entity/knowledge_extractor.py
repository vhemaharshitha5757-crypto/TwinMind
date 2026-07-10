from entity.header_extractor import HeaderExtractor
from entity.section_extractor import SectionExtractor
from entity.processor_pipeline import ProcessorPipeline
from entity.knowledge_builder import KnowledgeBuilder


class KnowledgeExtractor:

    def __init__(self):

        self.header_extractor = HeaderExtractor()
        self.section_extractor = SectionExtractor()
        self.processor_pipeline = ProcessorPipeline()
        self.knowledge_builder = KnowledgeBuilder()

    def extract(self, evidence):

        # ---------------------------------
        # Get raw text from Evidence object
        # ---------------------------------
        text = evidence.raw_text

        # ---------------------------------
        # Extract metadata
        # ---------------------------------
        metadata = self.header_extractor.extract(text)

        # ---------------------------------
        # Extract sections
        # ---------------------------------
        sections = self.section_extractor.extract(text)

        # ---------------------------------
        # Process sections
        # ---------------------------------
        processed = self.processor_pipeline.process(sections)

        # ---------------------------------
        # Build Operational Knowledge
        # ---------------------------------
        knowledge = self.knowledge_builder.build(
            metadata,
            processed
        )

        return knowledge
