#!/usr/bin/python3
import re

API_sample = "Ingredients: Beans, Potatoes, Mango, Salt, fish, Onion, ginger, Soya saurce, chicken wing"

pattern = r"(\b\w+\b)(?:,|$)"
ingredient_matches = re.findall(pattern, API_sample)
ingredient_list = [ingredient.strip() for ingredient in ingredient_matches]
print(', '.join(ingredient_list))