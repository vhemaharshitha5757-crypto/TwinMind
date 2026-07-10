class ConfidenceScorer:

    def score(self, document, image, audio):

        score = 0.50

        # Multiple modalities present
        score += 0.15

        # Root cause confirmed by document + audio
        if document.root_causes and audio.root_causes:
            score += 0.15

        # Image supports symptoms
        if image.symptoms:
            score += 0.10

        # Timeline exists
        if document.timestamps:
            score += 0.10

        return min(score, 1.0)
