# ----------------------------------------
# Python Strings
# ----------------------------------------
# A string is a series of characters enclosed in single or double quotes.

# Basic string methods
name = "fahad hossain babor"

print(name.title())  # Capitalizes the first letter of each word: "Fahad Hossain Babor"
print(name.upper())  # Converts all letters to uppercase: "FAHAD HOSSAIN BABOR"
print(name.lower())  # Converts all letters to lowercase: "fahad hossain babor"
# .lower() is often used for storing or comparing data consistently

# -----------------------------
# Using Variables in Strings
# -----------------------------
first_name = "ada"
last_name = "lovelace"

# f-strings allow easy formatting of strings
full_name = f"{first_name} {last_name}"
print(full_name)  # "ada lovelace"
print(f"Hello, {full_name.title()}")  # "Hello, Ada Lovelace"

# -----------------------------
# Escape Characters
# -----------------------------
# \t -> tab, \n -> new line
print("Python")        # Output: Python
print("\tPython")      # Output:     Python (tabbed)

print("Languages:\nPython\nC\nJavascript")
# Output:
# Languages:
# Python
# C
# Javascript

print("Languages:\n\tPython\n\tC\n\tJavascript")
# Output with indentation:
# Languages:
#     Python
#     C
#     Javascript

# -----------------------------
# Stripping Whitespace
# -----------------------------
lang = "  Python  "

print(lang.strip())   # Removes spaces from both sides: "Python"
print(lang.rstrip())  # Removes spaces from the right side: "  Python"
print(lang.lstrip())  # Removes spaces from the left side: "Python"