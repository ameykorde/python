"""
Python Input Examples

The `input()` function in Python is used to accept user input as a string. This file demonstrates various examples of input handling, including conversion to different data types, and validation.
"""

# 1. Basic Input
name = input("Enter your name: ")
print("Hello,", name)

# 2. Numeric Input (Integer)
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# 3. Numeric Input (Float)
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# 4. Multiple Inputs (Split Method)
# Accept multiple values in one line and split them into a list.
try:
    numbers = input("Enter three numbers separated by spaces: ").split() # split() method breaks this string into a list of substrings, using spaces as the delimiter by default.
    if len(numbers) != 3:
        raise ValueError("Please enter exactly three numbers.")
    num1, num2, num3 = map(int, numbers)
    print("The sum of the numbers is:", num1 + num2 + num3)
except ValueError as e:
    print("Error:", e)

# 5. Input Validation with Try-Except
try:
    score = int(input("Enter your test score: "))
    if 0 <= score <= 100:
        print("Your score is:", score)
    else:
        print("Score must be between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# 6. Input for Lists
# Collect multiple items into a list.
items = input("Enter items separated by commas: ").split(',')
print("You entered the following items:", [item.strip() for item in items])

# 7. Input as a Boolean Value
# Use case-insensitive input for Boolean interpretation.
response = input("Do you like Python? (yes/no): ").strip().lower()
is_liking_python = response == "yes"
print("Likes Python?", is_liking_python)

# 8. Input for Tuples
# Convert comma-separated input into a tuple.
tuple_input = tuple(input("Enter values separated by commas: ").split(','))
print("Tuple of values:", tuple_input)

# 9. Raw Input as String
# No type conversion applied.
raw_input = input("Enter anything: ")
print("You entered:", raw_input)

# 10. Password Input (Using getpass for hidden input)
from getpass import getpass
password = getpass("Enter your password: ")
print("Password successfully set (hidden).")

"""
Summary:
- Use `input()` to get user input as a string.
- Use typecasting (e.g., `int()`, `float()`) for numeric inputs.
- Handle input errors using try-except blocks.
- `getpass` can be used for sensitive inputs like passwords.
"""
