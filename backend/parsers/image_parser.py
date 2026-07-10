import json
import os

from models.evidence import Evidence


class ImageParser:

    def parse(self, path: str):

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        text = []

        text.append(data.get("caption", ""))
        text.append(data.get("scene_description", ""))

        text.extend(data.get("ocr_text", []))
        text.extend(data.get("detected_objects", []))

        return Evidence(
            evidence_id="IMG001",
            modality="image",
            source_file=os.path.basename(path),
            raw_text="\n".join(text),
            metadata=data
        )
