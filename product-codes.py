import re

# Read the text from the file
with open('/alu_regex-data-extraction-group13/txt_vault/Product-Codes.txt', 'r') as file:
    text = file.read()

# Define the regex pattern to match product codes
pattern = r'\b[A-Z]{3}\d{3}\b'

# Use re.findall to extract all matching product codes from the text
product_codes = re.findall(pattern, text)

# Print the extracted product codes
for code in product_codes:
    print(code)

