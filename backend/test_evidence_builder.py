from services.evidence_builder import EvidenceBuilder

builder = EvidenceBuilder()

doc = builder.build(
    modality="document",
    source_file="incident_report.pdf",
    raw_text="Database server crashed because disk reached 100%"
)

image = builder.build(
    modality="image",
    source_file="server_dashboard.png",
    raw_text="CPU Usage 98%, Disk Usage 100%"
)

audio = builder.build(
    modality="audio",
    source_file="meeting.mp3",
    raw_text="John confirmed disk saturation caused outage"
)

print(doc)
print()
print(image)
print()
print(audio)
