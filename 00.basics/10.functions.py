# functions_example.py

# 1. Simple Function: A function that takes no arguments and returns nothing
def greet():
    print("Hello, welcome to the functions tutorial!")

# Calling the greet function
print("Calling greet function:")
greet()

# 2. Function with Arguments: A function that takes parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Calling the greet_person function with an argument
print("\nCalling greet_person function:")
greet_person("Alice")
greet_person("Bob")

# 3. Function with Return Value: A function that performs an operation and returns a result
def add(a, b):
    return a + b

# Calling the add function and printing the result
print("\nCalling add function:")
result = add(5, 3)
print(f"The sum is: {result}")

# 4. Function with Default Arguments: A function that uses default values for arguments
def greet_person_default(name="Guest"):
    print(f"Hello, {name}!")

# Calling the greet_person_default function without argument (defaults to "Guest")
print("\nCalling greet_person_default function (no argument):")
greet_person_default()

# Calling the greet_person_default function with a custom argument
print("\nCalling greet_person_default function (with argument):")
greet_person_default("Charlie")

# 5. Function with Variable Number of Arguments: Using *args to accept any number of positional arguments
def print_numbers(*numbers):
    print("Numbers:", numbers)

# Calling the print_numbers function with different numbers of arguments
print("\nCalling print_numbers function:")
print_numbers(1, 2, 3)
print_numbers(10, 20, 30, 40, 50)

# 6. Function with Keyword Arguments: Using **kwargs to accept any number of keyword arguments
def describe_person(**person_info):
    for key, value in person_info.items():
        print(person_info["name"])
        print(f"{key}: {value}")

# Calling the describe_person function with keyword arguments
print("\nCalling describe_person function:")
describe_person(name="John", age=30, city="New York")
