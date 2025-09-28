# --------------------------------------
# Tuples (immutable lists)
# --------------------------------------
dimensions = (200, 50)
print(dimensions[0])   # Accessing elements
print(dimensions[1])

# Tuples are immutable (cannot be changed directly)
# dimensions[0] = 250  # ❌ This would cause an error

# You can reassign the variable to a new tuple
dimensions = (400, 100)
print(dimensions)

#tuples with one element
my_tuple = (3,)  # Note the comma
print(my_tuple)
#tuples with one element need the comma to differentiate from a regular parentheses expression

