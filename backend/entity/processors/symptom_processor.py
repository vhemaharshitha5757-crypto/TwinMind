import re


class SymptomProcessor:

    def process(self, symptoms_text: str):

        symptoms = []

        # Extract bullet points
        matches = re.findall(
            r"\*\s*(.+)",
            symptoms_text
        )

        for symptom in matches:

            symptom = symptom.strip()

            if symptom:
                symptoms.append(symptom)

        return symptoms
