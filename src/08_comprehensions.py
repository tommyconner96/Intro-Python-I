"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [i for i in range(6)]

print("Write a list comprehension to produce the array [1, 2, 3, 4, 5]:")
print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [i**3 for i in range(10)]

print("Write a list comprehension to produce the cubes of the numbers 0-9:")
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

# each.upper() changes case to uppercase
y = [each.upper() for each in a]

print("Write a list comprehension to produce the uppercase version of all the elements in array a.")
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

print("Use a list comprehension to create a list containing only the _even_ elements:")

x = input("Enter comma-separated numbers: ").split(',')
print("original input:", x)

# What do you need between the square brackets to make it work?

# if i % 2 == 0 then it will be an even number. odd numbers % 2 wil have a remainder so that number would not be 0.
y = [int(i) for i in x if int(i) % 2 == 0]

print(y)
