# docstring_example.py

# 1. Module Docstring
"""
This module demonstrates how to use docstrings in Python.
Docstrings are used to document modules, classes, and functions.
"""


# 2. Function Docstring
def greet(name):
    """
    This function greets the person passed in as the 'name' parameter.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message with the person's name.

    Example:
    greet("Alice")
    Output: "Hello, Alice!"
    """
    return f"Hello, {name}!"


# Calling the function to demonstrate it
print(greet("Alice"))


# 3. Class Docstring
class Person:
    """
    This class represents a person with a name and age.

    Attributes:
    name (str): The name of the person.
    age (int): The age of the person.

    Methods:
    __str__: Returns a string representation of the person.
    """

    def __init__(self, name, age):
        """
        Initializes a new instance of the Person class.

        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        Returns a string representation of the person.

        Returns:
        str: A formatted string containing the person's name and age.
        """
        return f"{self.name}, Age: {self.age}"


# Creating an instance of the Person class
person = Person("Bob", 30)
print(person)  # Output: Bob, Age: 30


# 4. Docstring for Methods Inside a Class
def calculate_area(radius):
    """
    This function calculates the area of a circle with the given radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.

    Example:
    calculate_area(5)
    Output: 78.53975
    """
    import math
    return math.pi * radius ** 2


# Calling the calculate_area function
print(calculate_area(5))  # Output: 78.53975


# 5. Docstring with a Nested Function Example
def outer_function():
    """
    This function demonstrates the use of docstrings with nested functions.

    It contains an inner function that performs a specific operation.
    """

    def inner_function(a, b):
        """
        This inner function adds two numbers.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The sum of the two numbers.
        """
        return a + b

    return inner_function(5, 7)


# Calling the outer_function which uses the inner_function
print(outer_function())  # Output: 12
