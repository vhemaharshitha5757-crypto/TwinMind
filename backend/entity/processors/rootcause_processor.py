import re


class RootCauseProcessor:

    def process(self, root_cause_text: str):

        causes = []

        # Remove heading sentence if present
        text = root_cause_text.replace(
            "The root cause of this incident was determined to be:",
            ""
        ).strip()

        # Take the first meaningful sentence
        sentences = re.split(r"\.\s+", text)

        if sentences:
            first = sentences[0].strip()

            if first:
                causes.append(first)

        return causes
