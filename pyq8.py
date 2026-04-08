import re

# Sample mixed text
text = ["Agra", "123", "Elephant", "Tomato", "Delhi", "apple", "Ramesh", "Orange", "456", "Patna", "Goa", "egg"]

# 1. Filter all the numbers
def filter_numbers(data):
    return [item for item in data if item.isdigit()]

# 2. Filter strings starting with a vowel
def filter_vowel_start(data):
    return [item for item in data if isinstance(item, str) and item[0].lower() in 'aeiou']

# 3. Filter strings containing certain nouns
def filter_nouns(data, nouns):
    return [item for item in data if item in nouns]

# Apply filters
numbers = filter_numbers(text)
vowel_strings = filter_vowel_start(text)
nouns = ["Agra", "Ramesh", "Tomato", "Patna"]
matched_nouns = filter_nouns(text, nouns)

# Display results
print("1. Numbers:", numbers)
print("2. Strings starting with a vowel:", vowel_strings)
print("3. Strings containing specific nouns:", matched_nouns)
