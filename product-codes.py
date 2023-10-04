import re

Product_Codes_API = "Jan 25, 2023 - 04:30 PM, Feb 28, 2023 - 00:00 AM, Sept 01, 2023 - 06:00 PM,  rgb(255, 0, 255), rgb(0, 255, 0), rgb(255, 255, 255), rgb(0, 0, 0), Breaking News: The outbreak of Covid-19, New Updates: Breaking News: The outbreak of Covid-19, Sports News:  Match Results, ABC123, , DEF250, ACE247, m@user.com, l@user.com, k@user.com"

# Define the regex pattern to match product codes
pattern = r'\b[A-Z]{3}\d{3}\b'I

# Use re.findall to extract all matching product codes from Product_Codes_API
product_codes = re.findall(pattern, Product_Codes_API)

# Print the extracted product codes
for code in product_codes:
    print(code)
