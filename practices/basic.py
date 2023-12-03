
### 1. Introduction to Python: `intro.py`

# intro.py
print("Hello, World!")

### 2. Data Types and Variables: `data_types.py`

# data_types.py
name = "Alice"  # String
age = 25        # Integer
height = 5.5    # Float

print(name, age, height)

### 3. Control Structures: `control_structures.py`

# control_structures.py
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")


### 4. Loops: `loops.py`

# loops.py
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


### 5. Functions: `functions.py`

# functions.py
def add(a, b):
    return a + b

result = add(3, 5)
print(result)


### 6. Data Structures: `data_structures.py`

# data_structures.py
# List
fruits = ["apple", "banana", "cherry"]

# Tuple
numbers = (1, 2, 3)

# Set
colors = {"red", "green", "blue"}

# Dictionary
person = {"name": "Alice", "age": 25}

print(fruits, numbers, colors, person)


### 7. Error and Exceptions: `error_handling.py`

# error_handling.py
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")


### 8. Object-Oriented Programming: `oop.py`

# oop.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.name, person1.age)


### 9. File Handling: `file_handling.py`

# file_handling.py
with open("test.txt", "w") as file:
    file.write("Hello, World!")

### 10. Libraries and Modules: `libraries.py`

# libraries.py
import math

result = math.sqrt(16)
print(result)


### 11. Advanced Topics: `advanced.py`

# advanced.py
# List comprehension
squares = [x**2 for x in range(10)]
print(squares)


### 12. Web Development with Python: `flask_example.py`

# flask_example.py
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"


### 13. Data Science with Python: `data_science.py`

# data_science.py
# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
# df = pd.DataFrame(data)
# print(df)


