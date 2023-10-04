import re

# Open the Event-Date-Time.txt file for reading
with open("/alu_regex-data-extraction-group13/txt_vault/Event-Date-Time.txt", "r") as f:
    # Read the entire file contents into a string
    text = f.read()

# Compile the regular expression for extracting event-date-times
event_date_time_regex = re.compile(r"(?P<month>\w{3}) (?P<day>\d{2}), (?P<year>\d{4}) - (?P<hour>\d{2}):(?P<minute>\d{2}) (?P<am_pm>\w{2})")

# Extract all of the event-date-times from the text
event_date_times = event_date_time_regex.findall(text)

# Format the extracted event-date-times in the specified format
formatted_event_date_times = []
for event_date_time in event_date_times:
    formatted_event_date_time = f"{event_date_time[0]} {event_date_time[1]}, {event_date_time[2]} - {event_date_time[3]}:{event_date_time[4]} {event_date_time[5]}"
    formatted_event_date_times.append(formatted_event_date_time)

# Print the formatted event-date-times
for formatted_event_date_time in formatted_event_date_times:
    print(formatted_event_date_time)

