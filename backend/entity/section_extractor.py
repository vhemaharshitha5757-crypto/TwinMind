import re


class SectionExtractor:
    """
    Extracts logical sections from an enterprise incident report.

    Example:
        SUMMARY
        BUSINESS IMPACT
        SYMPTOMS OBSERVED
        TIMELINE OF EVENTS
        INVESTIGATION
        ROOT CAUSE ANALYSIS
        RESOLUTION
        PREVENTIVE ACTIONS
        RELATED STANDARD OPERATING PROCEDURES
        LESSONS LEARNED
    """

    SECTION_PATTERNS = {
        "summary":
            r"1\.\s*SUMMARY\s*=+\s*(.*?)=+\s*2\.\s*BUSINESS IMPACT",

        "business_impact":
            r"2\.\s*BUSINESS IMPACT\s*=+\s*(.*?)=+\s*3\.\s*SYMPTOMS OBSERVED",

        "symptoms":
            r"3\.\s*SYMPTOMS OBSERVED\s*=+\s*(.*?)=+\s*4\.\s*TIMELINE OF EVENTS",

        "timeline":
            r"4\.\s*TIMELINE OF EVENTS\s*=+\s*(.*?)=+\s*5\.\s*INVESTIGATION",

        "investigation":
            r"5\.\s*INVESTIGATION\s*=+\s*(.*?)=+\s*6\.\s*ROOT CAUSE ANALYSIS",

        "root_cause":
            r"6\.\s*ROOT CAUSE ANALYSIS\s*=+\s*(.*?)=+\s*7\.\s*RESOLUTION",

        "resolution":
            r"7\.\s*RESOLUTION\s*=+\s*(.*?)=+\s*8\.\s*PREVENTIVE ACTIONS",

        "preventive_actions":
            r"8\.\s*PREVENTIVE ACTIONS\s*=+\s*(.*?)=+\s*9\.\s*RELATED STANDARD OPERATING PROCEDURES",

        "sops":
            r"9\.\s*RELATED STANDARD OPERATING PROCEDURES\s*=+\s*(.*?)=+\s*10\.\s*LESSONS LEARNED",

        "lessons_learned":
            r"10\.\s*LESSONS LEARNED\s*=+\s*(.*?)=+\s*Report generated",
    }

    def extract(self, text: str):

        sections = {}

        for section_name, pattern in self.SECTION_PATTERNS.items():

            match = re.search(
                pattern,
                text,
                re.DOTALL | re.IGNORECASE
            )

            if match:
                sections[section_name] = match.group(1).strip()
            else:
                sections[section_name] = ""

        return sections
