# ###### Printing variable values
# print(f"Hello, {input("Name: ")}!")

# #######  Converting input to integer
# age = int(input("Age: "))
# print(f"You are {age} years old.")

# ###### Sequences
name = "Alice"
print(name[0])  # First character
names = ["Alice", "Bob", "Charlie"] # this is a list
print(names[1])  # Second name
names.append("Diana")  # Adding a name
names.sort()  # Sorting names




coordinates = (10.0, 20.0)  # this is a Tuple of coordinates
print(coordinates[0])  # First coordinate


# create empty set
unique_numbers = set()
unique_numbers.add(1)
unique_numbers.add(2)
unique_numbers.add(2)  # Duplicate, will not be added
print(unique_numbers)  # Output: {1, 2}
unique_numbers.remove(1)
print(unique_numbers)  # Output: {2}
print(f"The set has {len(unique_numbers)} unique numbers.")

# ######Loops
for name in names:
 print(f"Hello, {name}!")
 
# ###### Dictionaries
houses= {"Alice": "Red", "Bob": "Blue", "Charlie": "Green"}
print(houses["Bob"])  # Output: Blue
houses["Diana"] = "Yellow"  # Adding a new key-value pair

# Functions
def square(number):
    return number * number
print(square(5))  # Output: 25

#Import other function file
from math import sqrt
print(sqrt(16))  # Output: 4.0