# Python List Operations - Example Code

# -----------------------------
# Working with Bicycles List
# -----------------------------
bicycles = ['trek', 'cannondale', 'veloce', 'slayer', 'redline']

# Print the entire list
print("Bicycles list:", bicycles)

# Accessing elements
print("First bicycle:", bicycles[0])

# Applying string methods
print("First bicycle (title case):", bicycles[0].title())

# Modifying an element
bicycles[0] = 'ducati'
print("After modifying first element:", bicycles)

# Adding elements to the end of the list
bicycles.append('hero')
print("After appending a new bicycle:", bicycles)

# -----------------------------
# Working with Motorcycles List
# -----------------------------
motorcycle = []  # defining an empty list

# Adding new elements to the list
motorcycle.append('Honda')
motorcycle.append('BMW')
motorcycle.append('Suzuki')
motorcycle.append('Royal Enfield')
print("Motorcycle list:", motorcycle)

# Insert an element at a specific position
motorcycle.insert(0, 'Ducati')
print("After inserting at position 0:", motorcycle)

# Removing elements
# Using 'del' to remove by index
del motorcycle[0]
print("After deleting first element:", motorcycle)

# Using 'pop' to remove and return last item
last_motorcycle = motorcycle.pop()
print("Popped last motorcycle:", last_motorcycle)
print("Motorcycle list now:", motorcycle)
print(f"The last motorcycle I owned was a {last_motorcycle.title()}")

# Popping from a specific position
first_owned = motorcycle.pop(0)
print(f"First owned motorcycle was {first_owned.title()}")

# Removing by value
motorcycle.remove("BMW")
print("After removing BMW:", motorcycle)

# -----------------------------
# Organizing Lists
# -----------------------------
# Sorting a list alphabetically
cars = ['bmw', 'audi', 'toyota', 'mercedes', 'jaguar']
cars.sort()
print("Cars sorted alphabetically:", cars)

# Sorting in reverse alphabetical order
cars.sort(reverse=True)
print("Cars sorted in reverse:", cars)

# Reversing a list (without sorting)
names = ['Fahad', 'Hossain', 'Babor']
names.reverse()
print("Names reversed:", names)

# Finding length of a list
print("Number of cars:", len(cars))

# -----------------------------
# Additional Useful List Operations
# -----------------------------
# Temporary sorting without changing original list
print("Temporarily sorted cars:", sorted(cars))
print("Cars list remains unchanged:", cars)

# Finding the position of an element
position = cars.index('audi')  # returns index of first occurrence
print("Position of 'audi' in cars list:", position)

# Counting occurrences of an element
count_toyota = cars.count('toyota')
print("Count of 'toyota' in cars list:", count_toyota)