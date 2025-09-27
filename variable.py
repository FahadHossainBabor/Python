# ----------------------------------------
# Python Variables
# ----------------------------------------
# Variables store values in memory. You can update their values anytime.

# Assigning a value to a variable
message = 'Hello Python world'
print(message)  # Output: Hello Python world

# Updating the variable
# This replaces the old value with a new one
message = 'I am Fahad Hossain Babor'
print(message)  # Output: I am Fahad Hossain Babor

# -----------------------------
# Variable Naming Rules
# -----------------------------
# - Can contain letters, numbers, and underscores
# - Must start with a letter or underscore
# - Cannot contain spaces
# - Cannot use Python keywords or function names
# - Should be descriptive

message_1 = 'Never gonna give you up'
print(message_1)  # Output: Never gonna give you up

message_2 = 'Never gonna let you down'
print(message_2)  # Output: Never gonna let you down

# Invalid examples (uncommenting these will raise errors):
# 1_message = 'Invalid'      # Cannot start with a number
# message 2 = 'Invalid'      # Cannot contain spaces
# print = 'Invalid'          # Cannot overwrite Python function names

# -----------------------------
# Exercise 2.1: Multi-line String
# -----------------------------
my_message = '''
Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you,
Never gonna make you cry,
Never gonna say goodbye and desert you.
'''
print(my_message)

# -----------------------------
# Exercise 2.2: Reassigning Variables
# -----------------------------
final_message = 'Why are you gay?'
print(final_message)  # Output: Why are you gay?

# Updating the variable
final_message = 'Who said I am gay?'
print(final_message)  # Output: Who said I am gay?