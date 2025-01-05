# lambda_map_filter_reduce.py

# Lambda Functions
# ----------------
# A lambda function is a small anonymous function defined using the `lambda` keyword.
# It can take any number of arguments but has only one expression.

# Example of a lambda function:
square = lambda x: x ** 2  # Lambda function to calculate the square of a number
print(square(5))  # Output: 25

# Another example:
multiply = lambda x, y: x * y  # Lambda function to multiply two numbers
print(multiply(3, 4))  # Output: 12

# Map
# ----
# The `map()` function applies a given function to all items in an iterable (e.g., list, tuple).

# Example with lambda and map:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example with a regular function and map:
def double(x):
    return x * 2

doubled_numbers = list(map(double, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# Filter
# ------
# The `filter()` function filters elements in an iterable based on a function that returns `True` or `False`.

# Example with lambda and filter:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Example with a regular function and filter:
def is_odd(x):
    return x % 2 != 0

odd_numbers = list(filter(is_odd, numbers))
print(odd_numbers)  # Output: [1, 3, 5]

# Reduce
# ------
# The `reduce()` function applies a rolling computation to sequential pairs of values in an iterable.
# It is part of the `functools` module.

from functools import reduce

# Example with lambda and reduce:
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15 (1 + 2 + 3 + 4 + 5)

# Example with a regular function and reduce:
def multiply(x, y):
    return x * y

product_of_numbers = reduce(multiply, numbers)
print(product_of_numbers)  # Output: 120 (1 * 2 * 3 * 4 * 5)

# Summary
# -------
# - `lambda`: Creates anonymous functions.
# - `map`: Applies a function to all elements in an iterable.
# - `filter`: Filters elements in an iterable based on a condition.
# - `reduce`: Performs a rolling computation on an iterable.

# Output:
# -------
# 25
# 12
# [1, 4, 9, 16, 25]
# [2, 4, 6, 8, 10]
# [2, 4]
# [1, 3, 5]
# 15
# 120
