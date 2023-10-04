import re

# Open the Username.txt file for reading
with open("/alu_regex-data-extraction-group13/txt_vault/Username.txt", "r") as f:
    # Read the entire file contents into a string
    text = f.read()

# Compile the regular expression for extracting usernames
username_regex = re.compile(r"@[^\s]+")

# Extract all of the usernames from the text
usernames = username_regex.findall(text)

# Print the extracted usernames
for username in usernames:
    print(username)

