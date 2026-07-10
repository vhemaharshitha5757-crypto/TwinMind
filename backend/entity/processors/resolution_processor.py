import re


class ResolutionProcessor:

    def process(self, resolution_text: str):

        resolutions = []

        match = re.search(
            r"The incident was resolved by the following actions:\s*(.*?)(?:\n\n|$)",
            resolution_text,
            re.DOTALL
        )

        if match:
            resolutions.append(
                match.group(1).strip()
            )

        return resolutions
