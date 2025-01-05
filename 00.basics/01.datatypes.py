"""
Python Data Types and Their Examples

In Python, everything is an object. Whether it's a number, a string, a list, or even a function, everything inherits from the base `object` class. This allows for consistent behavior across the language and opens up powerful object-oriented programming capabilities.

This file demonstrates the major data types in Python with examples and type checking.
"""

# 1. Numeric Types
# Numeric types represent numbers and include int, float, and complex.
# Integer (int): Whole numbers, positive or negative, without decimals.
int_example = 42
print("Value:", int_example, "| Type:", type(int_example))  # Type: <class 'int'>

# Floating-point number (float): Numbers with decimals.
float_example = 3.14
print("Value:", float_example, "| Type:", type(float_example))  # Type: <class 'float'>

# Complex number (complex): Numbers with a real and imaginary part.
complex_example = 2 + 3j
print("Value:", complex_example, "| Type:", type(complex_example))  # Type: <class 'complex'>

# 2. Boolean Type
# Boolean (bool): Represents True or False values, often used in conditional expressions.
bool_example = True
print("Value:", bool_example, "| Type:", type(bool_example))  # Type: <class 'bool'>

# 3. Sequence Types
# Sequence types store collections of items in a specific order. Includes str, list, and tuple.

# String (str): Represents text. Strings are immutable.
string_example = "Hello, Python!"
print("Value:", string_example, "| Type:", type(string_example))  # Type: <class 'str'>

# List (list): An ordered, mutable collection of items. Can store mixed types.
list_example = [1, 2, 3, "Python", 3.14]
print("Value:", list_example, "| Type:", type(list_example))  # Type: <class 'list'>

# Tuple (tuple): An ordered, immutable collection of items.
tuple_example = (1, 2, 3, "Python", 3.14)
print("Value:", tuple_example, "| Type:", type(tuple_example))  # Type: <class 'tuple'>

# 4. Mapping Type
# Dictionary (dict): An unordered collection of key-value pairs. Keys must be unique and immutable.
dict_example = {"name": "Python", "type": "Programming Language", "version": 3.10}
print("Value:", dict_example, "| Type:", type(dict_example))  # Type: <class 'dict'>

# 5. Set Types
# Set types represent unordered collections of unique elements.

# Set (set): A mutable, unordered collection of unique elements.
set_example = {1, 2, 3, "Python"}
print("Value:", set_example, "| Type:", type(set_example))  # Type: <class 'set'>

# Frozen Set (frozenset): An immutable version of a set.
frozenset_example = frozenset([1, 2, 3, "Python"])
print("Value:", frozenset_example, "| Type:", type(frozenset_example))  # Type: <class 'frozenset'>

# 6. None Type
# None (NoneType): Represents the absence of a value or a null value.
none_example = None
print("Value:", none_example, "| Type:", type(none_example))  # Type: <class 'NoneType'>

# 7. Bytes and Bytearray
# Bytes (bytes): Immutable sequences of bytes.
bytes_example = b"Hello, Python!"
print("Value:", bytes_example, "| Type:", type(bytes_example))  # Type: <class 'bytes'>

# Bytearray (bytearray): Mutable sequences of bytes.
bytearray_example = bytearray([65, 66, 67])
print("Value:", bytearray_example, "| Type:", type(bytearray_example))  # Type: <class 'bytearray'>

# 8. Memory View
# Memory View (memoryview): Provides a memory-efficient view of binary data.
memoryview_example = memoryview(bytearray_example)
print("Value:", memoryview_example, "| Type:", type(memoryview_example))  # Type: <class 'memoryview'>

# Summary
# Each data type in Python is an object derived from the base `object` class.
# The `type()` function is used to check the type of any object or variable.


