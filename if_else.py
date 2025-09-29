"""
Python If-Else Notes
--------------------

This file demonstrates:
- Basic if statements
- if-else
- if-elif-else chains
- Nested if statements
- Logical operators (and, or, not)
- Checking membership (in / not in)
- Boolean values (True/False)
- Real-world examples (pizza toppings, car checks, etc.)
"""

# --------------------------------------
# Basic if statement
# --------------------------------------
age = 18
if age >= 18:   # Condition is True
    print("You are old enough to vote!")


# --------------------------------------
# if-else example
# --------------------------------------
age = 16
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")


# --------------------------------------
# if-elif-else chain
# --------------------------------------
age = 25
if age < 13:
    print("You are a child.")
elif age < 20:   # Only checked if first condition is False
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")


# --------------------------------------
# Multiple conditions with and/or
# --------------------------------------
temperature = 25
is_raining = False

if temperature > 20 and not is_raining:
    print("It's a nice day for a walk!")
    
if temperature < 10 or is_raining:
    print("Better stay indoors!")


# --------------------------------------
# Checking membership with 'in' and 'not in'
# --------------------------------------
fruits = ['apple', 'banana', 'cherry']

if 'apple' in fruits:
    print("Apple is in the list!")

if 'mango' not in fruits:
    print("Mango is not in the list!")


# --------------------------------------
# Boolean values
# --------------------------------------
game_active = True
if game_active:
    print("The game is running.")

game_active = False
if not game_active:
    print("The game is paused.")


# --------------------------------------
# Nested if statements
# --------------------------------------
age = 19
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the club.")
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")


# --------------------------------------
# Real-world Example: Pizza Toppings
# --------------------------------------
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")


# --------------------------------------
# Another Real-world Example: Car Availability
# --------------------------------------
available_cars = ['audi', 'bmw', 'toyota', 'tesla']
requested_car = 'ferrari'

if requested_car in available_cars:
    print(f"{requested_car.title()} is available for rent!")
else:
    print(f"Sorry, {requested_car.title()} is not in our fleet.")


# --------------------------------------
# Example: Empty List Check
# --------------------------------------
requested_toppings = []

if requested_toppings:   # An empty list evaluates to False
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")