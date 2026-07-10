import os

from models.evidence import Evidence


class AudioParser:

    def parse(self, path: str):

        with open(path, "r", encoding="utf-8") as f:
            transcript = f.read()

        return Evidence(
            evidence_id="AUD001",
            modality="audio",
            source_file=os.path.basename(path),
            raw_text=transcript,
            confidence=0.95
        )
