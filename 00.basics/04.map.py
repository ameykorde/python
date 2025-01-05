"""
Python's `map()` Function Examples

The `map()` function applies a specified function to each item in an iterable and returns a map object (an iterator). It is useful for transforming data efficiently and cleanly.

Syntax:
    map(function, iterable, ...)
Parameters:
    - function: A function to apply to each element of the iterable(s).
    - iterable(s): One or more iterables whose elements will be passed to the function.
Returns:
    - A map object (iterator) containing the results of applying the function.
"""

# 1. Applying a Function to a Single Iterable
# Function to double a number
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
# Applying the `double` function to each element of the list using map
result = map(double, numbers)
print("Doubled numbers:", list(result))  # Output: [2, 4, 6, 8, 10]

# 2. Using a Lambda Function with `map()`
# Using a lambda to square each number in the list
result = map(lambda x: x ** 2, numbers)
print("Squared numbers:", list(result))  # Output: [1, 4, 9, 16, 25]

# 3. Mapping Multiple Iterables
# Adding corresponding elements from two lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
result = map(lambda x, y: x + y, list_a, list_b)
print("Sum of corresponding elements:", list(result))  # Output: [5, 7, 9]

# 4. Converting Strings to Integers
# Using map to convert a list of strings to a list of integers
string_numbers = ["10", "20", "30"]
result = map(int, string_numbers)
print("Converted integers:", list(result))  # Output: [10, 20, 30]

# 5. Lazy Evaluation of `map()`
# Demonstrating that `map()` returns an iterator
result = map(double, [6, 7, 8])
print("Map object:", result)  # Output: <map object at some_memory_address>
print("Evaluated results:", list(result))  # Output: [12, 14, 16]

# 6. Using map() for String Operations
# Converting a list of words to uppercase
words = ["hello", "world", "python"]
result = map(str.upper, words)
print("Uppercase words:", list(result))  # Output: ['HELLO', 'WORLD', 'PYTHON']

# 7. Handling Multiple Iterables of Different Lengths
# Shortest iterable determines the length of the result
list_x = [1, 2, 3]
list_y = [4, 5]
result = map(lambda x, y: x * y, list_x, list_y)
print("Product of corresponding elements:", list(result))  # Output: [4, 10]

# 8. Complex Transformations with map()
# Combining map with other functions for advanced transformations
names = ["Alice", "Bob", "Charlie"]
# Creating a list of dictionaries with name length
result = map(lambda name: {"name": name, "length": len(name)}, names)
print("Name details:", list(result))

"""
Summary:
- `map()` is a functional programming tool for applying a function to elements in one or more iterables.
- It returns a map object (iterator) which can be converted to a list, tuple, or other collections.
- Useful for clean and efficient transformations but may sacrifice readability for complex operations.
"""
