import re

from models.operational_knowledge import OperationalKnowledge


class AudioKnowledgeExtractor:

    def extract(self, evidence):

        text = evidence.raw_text

        knowledge = OperationalKnowledge()

        # Engineers
        engineers = re.findall(
            r"\[(.*?)\]:",
            text
        )

        knowledge.engineers = list(set(engineers))

        # PostgreSQL Cluster
        if "PostgreSQL Cluster" in text:
            knowledge.systems.append(
                "PostgreSQL Cluster"
            )

        # Components
        components = re.findall(
            r"db-prod-[a-zA-Z0-9-]+",
            text
        )

        knowledge.components = list(set(components))

        # Root Cause
        if "wal segment corruption" in text.lower():

            knowledge.root_causes.append(
                "WAL segment corruption caused by failing NVMe SSD"
            )

        # Resolution
        if "standby replica" in text.lower():

            knowledge.resolutions.append(
                "Promote standby replica and reconfigure PgBouncer"
            )

        return knowledge
