from models.operational_knowledge import OperationalKnowledge
from models.processed_sections import ProcessedSections


class KnowledgeBuilder:

    def build(self, metadata: dict, processed: ProcessedSections):

        knowledge = OperationalKnowledge()

        # ---------------- Metadata ----------------

        knowledge.incident_id = metadata.get("incident_id", "")
        knowledge.title = metadata.get("title", "")
        knowledge.severity = metadata.get("severity", "")

        if "system" in metadata:
            knowledge.systems.append(metadata["system"])

        if "component" in metadata:
            knowledge.components.append(metadata["component"])

        if "engineer" in metadata:
            knowledge.engineers.append(metadata["engineer"])

        if "department" in metadata:
            knowledge.departments.append(metadata["department"])

        if "location" in metadata:
            knowledge.locations.append(metadata["location"])

        # ---------------- Processed Sections ----------------

        knowledge.symptoms = processed.symptoms

        knowledge.root_causes = processed.root_causes

        knowledge.resolutions = processed.resolutions

        knowledge.sops = processed.sops

        knowledge.timestamps = [
            f"{event.time} -> {event.event}"
            for event in processed.timeline
        ]

        return knowledge
