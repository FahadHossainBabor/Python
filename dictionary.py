"""
Python Dictionary Notes
-----------------------

A dictionary is a collection of key-value pairs.
- Keys must be unique and immutable (string, number, tuple).
- Values can be any data type.
- Dictionaries are unordered (Python 3.7+ preserves insertion order).
- Defined with curly braces {}.

This file demonstrates:
- Creating dictionaries
- Accessing values
- Adding and modifying key-value pairs
- Removing items
- Looping through dictionaries
- Checking membership
- Dictionary methods
- Nesting (dictionaries in lists, lists in dictionaries, etc.)
- Real-world examples
"""

# --------------------------------------
# Creating a dictionary
# --------------------------------------
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)


# --------------------------------------
# Accessing values
# --------------------------------------
print(person["name"])   # Access value by key
print(person.get("age"))  # Access using get()

# Using .get() avoids errors if the key is missing
print(person.get("country", "Not Found"))


# --------------------------------------
# Adding new key-value pairs
# --------------------------------------
person["profession"] = "Engineer"
print(person)


# --------------------------------------
# Modifying values
# --------------------------------------
person["age"] = 26
print(person)


# --------------------------------------
# Removing key-value pairs
# --------------------------------------
del person["city"]        # Delete by key
print(person)

profession = person.pop("profession")  # Remove and return value
print(f"Removed: {profession}")
print(person)


# --------------------------------------
# Looping through a dictionary
# --------------------------------------
user = {
    "username": "fahad123",
    "email": "fahad@example.com",
    "location": "Bangladesh"
}

# Loop through keys
for key in user.keys():
    print(f"Key: {key}")

# Loop through values
for value in user.values():
    print(f"Value: {value}")

# Loop through key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")


# --------------------------------------
# Checking if a key exists
# --------------------------------------
if "email" in user:
    print("Email exists in dictionary")


# --------------------------------------
# Length of dictionary
# --------------------------------------
print(f"Number of items: {len(user)}")


# --------------------------------------
# Dictionary methods
# --------------------------------------
car = {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2022
}

print(car.keys())    # All keys
print(car.values())  # All values
print(car.items())   # All key-value pairs

car_copy = car.copy()  # Shallow copy
print(car_copy)

car.update({"color": "red"})  # Add/update multiple items
print(car)

car.clear()   # Remove everything
print(car)


# --------------------------------------
# Nesting Examples
# --------------------------------------

# List of dictionaries
users = [
    {"username": "alice", "age": 25},
    {"username": "bob", "age": 30},
    {"username": "charlie", "age": 22}
]

for user in users:
    print(user)

# Dictionary with lists as values
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese", "olives"]
}

print(f"You ordered a {pizza['crust']}-crust pizza with these toppings:")
for topping in pizza["toppings"]:
    print(f"- {topping}")

# Dictionary inside a dictionary
students = {
    "s101": {"name": "Fahad", "dept": "CSE"},
    "s102": {"name": "Rafi", "dept": "EEE"}
}

for student_id, details in students.items():
    print(f"ID: {student_id}")
    for key, value in details.items():
        print(f"  {key}: {value}")


# --------------------------------------
# Real-life examples
# --------------------------------------

# Example 1: Contact book
contacts = {
    "Alice": {"phone": "123-4567", "email": "alice@example.com"},
    "Bob": {"phone": "987-6543", "email": "bob@example.com"},
}

for name, info in contacts.items():
    print(f"{name} -> Phone: {info['phone']}, Email: {info['email']}")

# Example 2: Inventory system
inventory = {
    "apple": 50,
    "banana": 20,
    "orange": 75
}

# Selling some bananas
inventory["banana"] -= 5
print(f"Updated inventory: {inventory}")

# Example 3: Student grades
grades = {
    "Fahad": [85, 90, 92],
    "Rafi": [78, 80, 85],
    "Nusrat": [88, 76, 91]
}

for student, marks in grades.items():
    avg = sum(marks) / len(marks)
    print(f"{student}'s average grade: {avg:.2f}")

# Example 4: Country capitals
capitals = {
    "Bangladesh": "Dhaka",
    "USA": "Washington D.C.",
    "Japan": "Tokyo"
}
print(capitals["Japan"])

# Example 5: Word frequency counter
sentence = "python is fun and python is powerful"
word_counts = {}

for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)