from pathlib import Path

from services.evidence_builder import EvidenceBuilder


class DocumentParser:

    def __init__(self):
        self.builder = EvidenceBuilder()

    def parse(self, filepath: str):

        path = Path(filepath)

        suffix = path.suffix.lower()

        if suffix == ".txt":
            text = self._read_txt(path)

        elif suffix == ".pdf":
            text = self._read_pdf(path)

        else:
            raise ValueError(f"Unsupported document type: {suffix}")

        return self.builder.build(
            modality="document",
            source_file=path.name,
            raw_text=text,
        )

    def _read_txt(self, path):

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def _read_pdf(self, path):

        raise NotImplementedError(
            "PDF support will be added next."
        )
