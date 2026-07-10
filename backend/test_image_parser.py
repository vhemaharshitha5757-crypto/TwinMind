from parsers.image_parser import ImageParser

parser = ImageParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/image_metadata.json"
)

print(evidence)
