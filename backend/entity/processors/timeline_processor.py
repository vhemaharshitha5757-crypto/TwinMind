import re


class TimelineProcessor:

    def process(self, timeline_text: str):

        timeline = []

        pattern = r"\[(.*?)\]\s*(.*)"

        matches = re.findall(pattern, timeline_text)

        for time, event in matches:

            timeline.append({
                "time": time.strip(),
                "event": event.strip()
            })

        return timeline
