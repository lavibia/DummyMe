#classes
from unicodedata import name


class Point():
 def __init__(self, x, y): #constructor
  self.x = x
  self.y = y
  
p=Point(2,3)
print(p.x)
print(p.y)


class Flight():
  def __init__(self, capacity):
   self.capacity = capacity
   self.passengers = []
  def add_passenger(self, name):
   if not self.open_seats():
    return False
   self.passengers.append(name)
   return True
  def open_seats(self):
   return self.capacity - len(self.passengers)
flight=Flight(3)

people=["Alice", "Bob", "Charlie", "Diana"]
for person in people:
 success=flight.add_passenger(person)
 if success:
  print(f"Added {person} to flight successfully.")
 else:
  print(f"No available seats for {person}.")
  
# decorators
def announce(f):
 def wrapper():
  print("About to run the function...")
  f()
  print("Done with the function.")
 return wrapper

@announce
def greet():
 print("Hello, world!")
greet()

# lambda functions
people = [
 {"name": "Alice", "age": 30},
 {"name": "Bob", "age": 25},]
people.sort(key=lambda person: person["age"])
for person in people:
 print(f"{person['name']} is {person['age']} years old.")
 
# Exceptions
def divide(a, b):
 try:
  result = a / b
 except ZeroDivisionError:
  return "Error: Cannot divide by zero."
 else:
  return result
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Cannot divide by zero.