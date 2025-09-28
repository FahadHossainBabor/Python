"""
Python Basics Notes
-------------------

This file demonstrates fundamental Python concepts:
- For loops with lists
- Using range()
- Creating number sequences
- List operations (append, min, max, sum)
- List slicing
- Copying lists
- List comprehensions
- Iterating with indexes (enumerate)
- List length
- Sorting lists
- Tuples (immutable lists)
"""

# --------------------------------------
# Looping through a list of magicians
# --------------------------------------
magicians = ['alice','david','carolina']
for magician in magicians:
    # Print a personalized message for each magician
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# This line runs once after the loop is done
print("Thank you, everyone. That was a great magic show!")


# --------------------------------------
# Looping through a list of cats
# --------------------------------------
cats = ['whiskers', 'mittens', 'fluffy']
for cat in cats:
    print(f"{cat.title()} is a great cat!")

# This runs once after the loop ends
print("Any of these cats would make a great pet!")
    

# --------------------------------------
# Using range() to generate numbers
# --------------------------------------
for value in range(1,6):   # Numbers from 1 to 5
    print(value)
    
for value in range(6):     # Numbers from 0 to 5
    print(value)

for i in range(1,11,2):    # Numbers from 1 to 10 with a step of 2
    print(i)
    

# --------------------------------------
# Creating a list from a range of numbers
# --------------------------------------
numbers = list(range(1,11))   # [1,2,3,4,5,6,7,8,9,10]
print(numbers)


# --------------------------------------
# Building a list of squares using a loop
# --------------------------------------
squares = []
for value in range(1,11):
    square = value**2       # Exponentiation (value squared)
    squares.append(square)  # Append square to list

# Another way (direct append without variable)
for value in range(1,11):
    squares.append(value**2)

print(squares)


# --------------------------------------
# Using list comprehension (shortcut way)
# --------------------------------------
squares_comp = [value**2 for value in range(1,11)]
print(squares_comp)


# --------------------------------------
# Basic math functions with lists
# --------------------------------------
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))  # Smallest number in the list
print(max(digits))  # Largest number in the list
print(sum(digits))  # Sum of all numbers in the list


# --------------------------------------
# List slicing examples
# --------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])   # First 3 elements
print(players[1:4])   # Elements at index 1,2,3
print(players[:4])    # First 4 elements
print(players[2:])    # From index 2 to the end
print(players[-3:])   # Last 3 elements


# --------------------------------------
# Copying a list using slicing
# --------------------------------------
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]   # Makes a copy of the list

print("My favorite foods are:")
print(my_foods)

# Adding a new item to my_foods
my_foods.append('cannoli')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)   # friend_foods remains unchanged


# --------------------------------------
# Iterating with indexes using enumerate()
# --------------------------------------
for index, player in enumerate(players):
    print(f"Player {index} is {player.title()}")


# --------------------------------------
# Finding the length of a list
# --------------------------------------
print(f"Number of players: {len(players)}")


# --------------------------------------
# Sorting lists
# --------------------------------------
print(sorted(players))      # Temporary alphabetical sort
print(sorted(players, reverse=True))  # Temporary reverse sort

players.sort()              # Permanent alphabetical sort
print(players)

players.sort(reverse=True)  # Permanent reverse sort
print(players)


