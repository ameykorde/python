# exception_handling_example.py

# 1. Basic Try and Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.

try:
    num1 = 10
    num2 = 0
    result = num1 / num2  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero!")
    print("Exception details:", e)

# 2. Catching Multiple Exceptions
# You can catch multiple exceptions by using multiple except blocks.

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2  # May raise a ZeroDivisionError or ValueError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter valid numbers.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("The result of the division is:", result)

# 3. Finally Block
# The finally block will run no matter what, even if an exception occurs.
try:
    num1 = 10
    num2 = 0
    result = num1 / num2  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("This block always runs. if in function return is above finally STILL ITS GOING TO BE EXECUTED")

# 4. Raising an Exception
# You can raise your own exceptions using the `raise` keyword.
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print(f"Age is valid: {age}")

try:
    validate_age(-5)  # This will raise a ValueError
except ValueError as e:
    print("Caught an exception:", e)

# 5. Creating a Custom Exception
# You can define your own exception class by subclassing the built-in Exception class.

class CustomError(Exception):
    """A custom exception class"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom error message")
except CustomError as e:
    print("Caught custom exception:", e)

# 6. Exception Hierarchy
# All exceptions in Python are instances of the `BaseException` class.

try:
    raise TypeError("This is a TypeError!")
except TypeError as e:
    print("Caught a TypeError:", e)
except Exception as e:  # This will catch other general exceptions
    print("Caught some other error:", e)
finally:
    print("Exception handling completed.")
