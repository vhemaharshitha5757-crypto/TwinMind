from models.evidence import Evidence
from models.incident import UnifiedIncident

evidence = Evidence(
    evidence_id="EV001",
    modality="document",
    source_file="incident.pdf",
    raw_text="Database server crashed because disk usage reached 100%"
)

print(evidence)

incident = UnifiedIncident(
    incident_id="INC001",
    title="Database Crash",
    summary="Production database outage",
    severity="Critical"
)

print(incident)
