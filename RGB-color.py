#!/usr/bin/python3
import re

Product_Codes_API = "Jan 25, 2023 - 04:30 PM, Feb 28, 2023 - 00:00 AM, Sept 01, 2023 - 06:00 PM,  rgb(255, 0, 255), rgb(0, 255, 0), rgb(255, 255, 255), rgb(0, 0, 0), Breaking News: The outbreak of Covid-19, New Updates: Breaking News: The outbreak of Covid-19, Sports News:  Match Results, ABC123, , DEF250, ACE247, m@user.com, l@user.com, k@user.com"

pattern = r"rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)"
matches = re.findall(pattern, API_sample)
for match in matches:
    color_0, color_1, color_2 = map(int, match)
    print(f"RGB Color: rgb({color_0}, {color_1}, {color_2})")