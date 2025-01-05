"""
Python Typecasting and Examples

Typecasting is the process of converting one data type into another. Python supports both:

1. Implicit Typecasting: Automatically performed by Python when converting smaller data types to larger compatible types.
2. Explicit Typecasting: Manually converting one data type to another using built-in functions.

This file demonstrates both types of typecasting with examples.
"""

# 1. Implicit Typecasting
# Python automatically converts one data type to another when required.
num_int = 10   # Integer
num_float = 3.14  # Float

# Adding an int and a float results in a float (wider type).
result = num_int + num_float
print("Result (Implicit):", result, "| Type:", type(result))  # Type: <class 'float'>

# 2. Explicit Typecasting
# Done using Python's built-in functions.

# Integer to String
num = 100
num_str = str(num)
print("Value:", num_str, "| Type:", type(num_str))  # Type: <class 'str'>

# String to Integer
num_str = "50"
num_int = int(num_str)
print("Value:", num_int, "| Type:", type(num_int))  # Type: <class 'int'>

# Float to Integer
num_float = 5.99 # .99 will get remove
num_int = int(num_float)  # Fractional part is truncated.
print("Value:", num_int, "| Type:", type(num_int))  # Type: <class 'int'>

# Integer to Float
num_int = 42
num_float = float(num_int)
print("Value:", num_float, "| Type:", type(num_float))  # Type: <class 'float'>

# String to Float
num_str = "3.1415"
num_float = float(num_str)
print("Value:", num_float, "| Type:", type(num_float))  # Type: <class 'float'>

# List to Tuple
list_example = [1, 2, 3, 4]
tuple_example = tuple(list_example)
print("Value:", tuple_example, "| Type:", type(tuple_example))  # Type: <class 'tuple'>

# Tuple to List
tuple_example = (5, 6, 7, 8)
list_example = list(tuple_example)
print("Value:", list_example, "| Type:", type(list_example))  # Type: <class 'list'>

# Integer to Binary, Octal, and Hexadecimal
num = 255
print("Binary:", bin(num))   # Binary representation
print("Octal:", oct(num))    # Octal representation
print("Hexadecimal:", hex(num))  # Hexadecimal representation

# Complex Numbers
# Converting to a complex number.
real = 4
imag = 5
complex_number = complex(real, imag)
print("Value:", complex_number, "| Type:", type(complex_number))  # Type: <class 'complex'>

# Caution: Invalid conversions
# Some conversions can raise errors if the data is incompatible.
# Uncommenting the lines below will raise ValueError.
# invalid_str = "Python"
# int(invalid_str)  # ValueError: invalid literal for int()

"""
Summary:
- Implicit typecasting happens automatically for compatible types.
- Explicit typecasting requires built-in functions like int(), str(), float(), tuple(), list(), etc.
- Always ensure the data being converted is compatible with the target type to avoid runtime errors.
"""
