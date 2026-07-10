from models.processed_sections import ProcessedSections, TimelineEvent

from entity.processors.symptom_processor import SymptomProcessor
from entity.processors.timeline_processor import TimelineProcessor
from entity.processors.rootcause_processor import RootCauseProcessor
from entity.processors.resolution_processor import ResolutionProcessor
from entity.processors.sop_processor import SOPProcessor


class ProcessorPipeline:

    def __init__(self):

        self.symptom = SymptomProcessor()
        self.timeline = TimelineProcessor()
        self.root = RootCauseProcessor()
        self.resolution = ResolutionProcessor()
        self.sop = SOPProcessor()

    def process(self, sections):

        processed = ProcessedSections()

        # Symptoms
        processed.symptoms = self.symptom.process(
            sections["symptoms"]
        )

        # Timeline
        events = self.timeline.process(
            sections["timeline"]
        )

        processed.timeline = [
            TimelineEvent(**event)
            for event in events
        ]

        # Root Cause
        processed.root_causes = self.root.process(
            sections["root_cause"]
        )

        # Resolution
        processed.resolutions = self.resolution.process(
            sections["resolution"]
        )

        # SOPs
        processed.sops = self.sop.process(
            sections["sops"]
        )

        return processed
