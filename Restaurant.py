import re

# Open the Name-Cuisine.txt file for reading
with open("/alu_regex-data-extraction-group18/texts/ingredient.txt", "r") as f:
    # Read the entire file contents into a string
    text = f.read()

# Compile the regular expression for extracting restaurant names and ingredient
name_cuisine_regex = re.compile(r"^(.) - (.)$")

# Extract all of the restaurant names and cuisines from the text
name_cuisine_lists = name_cuisine_regex.findall(text)

# Print the extracted restaurant names and ingredient
for name_cuisine_list in name_cuisine_lists:
    print(f"{name_cuisine_list[0]}: {name_cuisine_list[1]}")
