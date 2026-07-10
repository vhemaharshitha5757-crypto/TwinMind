import re

from models.operational_knowledge import OperationalKnowledge


class ImageKnowledgeExtractor:

    def extract(self, evidence):

        metadata = evidence.metadata

        knowledge = OperationalKnowledge()

        # -----------------------------
        # System
        # -----------------------------
        system = metadata.get("source_system", "")
        if system:
            knowledge.systems.append(system)

        # -----------------------------
        # OCR Processing
        # -----------------------------
        ocr = metadata.get("ocr_text", [])

        for line in ocr:

            if "Node:" in line:
                knowledge.components.append(
                    line.split(":", 1)[1].strip()
                )

            elif "Status:" in line:
                knowledge.symptoms.append(
                    line.strip()
                )

            elif "Errors" in line:
                knowledge.symptoms.append(
                    line.strip()
                )

            elif "Latency" in line:
                knowledge.symptoms.append(
                    line.strip()
                )

            elif "Connections" in line:
                knowledge.symptoms.append(
                    line.strip()
                )

        # -----------------------------
        # Caption
        # -----------------------------
        caption = metadata.get("caption", "")

        if "WAL" in caption:
            knowledge.root_causes.append(
                "Possible WAL related failure"
            )

        return knowledge
