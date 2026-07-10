
from fusion.similarity_matcher import SimilarityMatcher
from fusion.confidence_scorer import ConfidenceScorer
from models.unified_incident import UnifiedIncident


class FusionEngine:

    def __init__(self):
        self.matcher = SimilarityMatcher()
        self.confidence = ConfidenceScorer()

    def fuse(self, document, image, audio):

        incident = UnifiedIncident()

        # =====================================================
        # Basic Information
        # =====================================================

        incident.incident_id = document.incident_id
        incident.title = document.title
        incident.severity = document.severity

        # =====================================================
        # Systems
        # =====================================================

        incident.systems = list(set(
            document.systems +
            image.systems +
            audio.systems
        ))

        # =====================================================
        # Components
        # =====================================================

        incident.components = list(set(
            document.components +
            image.components +
            audio.components
        ))

        # =====================================================
        # Engineers
        # =====================================================

        incident.engineers = list(set(
            document.engineers +
            image.engineers +
            audio.engineers
        ))

        # =====================================================
        # Departments
        # =====================================================

        incident.departments = list(set(
            document.departments +
            image.departments +
            audio.departments
        ))

        # =====================================================
        # Locations
        # =====================================================

        incident.locations = list(set(
            document.locations +
            image.locations +
            audio.locations
        ))

        # =====================================================
        # Symptoms (Similarity Matching)
        # =====================================================

        symptoms = (
            document.symptoms +
            image.symptoms +
            audio.symptoms
        )

        incident.symptoms = self.matcher.match(symptoms)

        # =====================================================
        # Root Causes (Similarity Matching)
        # =====================================================

        root_causes = (
            document.root_causes +
            image.root_causes +
            audio.root_causes
        )

        incident.root_causes = self.matcher.match(root_causes)

        # =====================================================
        # Resolutions (Similarity Matching)
        # =====================================================

        resolutions = (
            document.resolutions +
            image.resolutions +
            audio.resolutions
        )

        incident.resolutions = self.matcher.match(resolutions)

        # =====================================================
        # SOPs
        # =====================================================

        incident.sops = list(set(
            document.sops +
            image.sops +
            audio.sops
        ))

        # =====================================================
        # Timeline
        # =====================================================

        incident.timeline = document.timestamps

        # =====================================================
        # Sources
        # =====================================================

        incident.sources = [
            "document",
            "image",
            "audio"
        ]

        # =====================================================
        # Confidence Score
        # =====================================================

        incident.confidence = self.confidence.score(
            document,
            image,
            audio
        )

        return incident
