from parsers.document_parser import DocumentParser

parser = DocumentParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/incident_report.txt"
)

print(evidence)

