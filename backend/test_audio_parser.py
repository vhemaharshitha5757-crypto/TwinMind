from parsers.audio_parser import AudioParser

parser = AudioParser()

evidence = parser.parse(
    "../datasets/TwinMind-Dataset/incidents/INC001/meeting_transcript.txt"
)

print(evidence)
