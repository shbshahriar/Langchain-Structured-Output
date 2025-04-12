# This script demonstrates the use of TypedDict to define a structured dictionary type in Python.

# Import TypedDict from the typing module
from typing import TypedDict

# Define a TypedDict class named 'Person' with specific key-value types
class Person(TypedDict):
    name: str  # The 'name' key must have a string value
    age: int   # The 'age' key must have an integer value

# Create an instance of the 'Person' TypedDict with valid data
new_person: Person = {'name': 'shihab', 'age': 25}

# Print the 'new_person' dictionary to the console
print(new_person)