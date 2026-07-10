import re


class HeaderExtractor:

    PATTERNS = {
        "incident_id": r"Incident ID:\s*(.*)",
        "title": r"Title:\s*(.*)",
        "severity": r"Severity:\s*(.*)",
        "department": r"Department:\s*(.*)",
        "system": r"System:\s*(.*)",
        "component": r"Component:\s*(.*)",
        "location": r"Location:\s*(.*)",
        "engineer": r"Assigned Engineer:\s*(.*)"
    }

    def extract(self, text: str):

        metadata = {}

        for key, pattern in self.PATTERNS.items():

            match = re.search(pattern, text)

            if match:
                metadata[key] = match.group(1).strip()

        return metadata
