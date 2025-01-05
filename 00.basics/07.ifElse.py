"""
Python If-Else Statements with Examples

The if-else statement in Python is used for conditional execution. Based on the condition, different blocks of code can be executed.
"""

# Basic Syntax of If-Else:
# if condition:
#     # Code to execute if the condition is True
# else:
#     # Code to execute if the condition is False

# Example 1: Checking if a number is positive or negative
number = int(input("Enter a number: "))
if number >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# Example 2: Checking even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Example 3: Nested If-Else
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")

# Example 4: Using Elif (Else If)
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Example 5: Ternary If-Else (Single-Line If-Else)
number = int(input("Enter a number: "))
result = "Positive" if number >= 0 else "Negative"
print("The number is:", result)

# Example 6: Multiple Conditions with Logical Operators
# Checking if a number lies in a specific range
number = int(input("Enter a number: "))
if number > 0 and number < 10:
    print("The number is a single-digit positive number.")
else:
    print("The number is not a single-digit positive number.")

# Example 7: Using Boolean Conditions Directly
# A direct boolean condition in if-else
is_raining = True
if is_raining:
    print("Take an umbrella.")
else:
    print("Enjoy your day!")

"""
This file demonstrates various ways to use if-else statements in Python.
It covers basic usage, nested conditions, elif, ternary statements, and logical operators.
NO SWITCH CASE IN PYTHON
"""
