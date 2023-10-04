#!/usr/bin/python3
import re

# Raw API response containing news headlines
raw_data = """Here are some news headlines:
       Headline: Breaking News - The outbreak of Covid-19
       Headline: New Updates - The creation of new AI
       Headline: Sports News - Match Results
        """

pattern = r'Headline: (.*?) - (.*?)'
matches = re.finditer(pattern, raw_data)
structured_headlines = []

for match in matches:
    headline = match.group(1)
    subheader = match.group(2)
    structured_headlines.append({"Headline": headline, "Subheader": subheader})


for item in structured_headlines:
    print(item)                                        