import re


class SOPProcessor:

    def process(self, sop_text: str):

        sops = re.findall(
            r"SOP-[A-Z]+-\d+",
            sop_text
        )

        return sops
