from models.evidence import Evidence


class EvidenceBuilder:

    def __init__(self):
        self.counter = 1

    def build(
        self,
        modality: str,
        source_file: str,
        raw_text: str,
        metadata: dict | None = None,
    ) -> Evidence:

        evidence = Evidence(
            evidence_id=f"EV{self.counter:03d}",
            modality=modality,
            source_file=source_file,
            raw_text=raw_text,
            metadata=metadata or {},
            confidence=1.0
        )

        self.counter += 1

        return evidence
