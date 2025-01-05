# fstring_example.py

# 1. Basic f-string Example
# F-strings allow you to embed expressions inside string literals using curly braces `{}`.
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.

# 2. f-string with Expressions
# You can use expressions inside the curly braces. The expression is evaluated at runtime.
result = 5 + 3
expression_string = f"The result of 5 + 3 is {result}."
print(expression_string)  # Output: The result of 5 + 3 is 8.

# 3. f-string with Calculations Inside
# You can also perform calculations directly inside the f-string.
calculation = f"10 multiplied by 2 is {10 * 2}."
print(calculation)  # Output: 10 multiplied by 2 is 20.

# 4. f-string with Formatting (Decimal Places)
# You can format numbers (like float values) using f-strings.
pi = 3.14159265359
formatted_pi = f"Pi rounded to 2 decimal places is {pi:.2f}."
print(formatted_pi)  # Output: Pi rounded to 2 decimal places is 3.14.

# 5. f-string with Padding
# You can also use f-strings for string formatting with padding.
name = "Bob"
padded_name = f"{name:10}"  # Adds padding to the right (10 characters wide).
print(f"Padded name: '{padded_name}'")  # Output: Padded name: 'Bob       '

# 6. f-string with Alignment
# Align text to the left, right, or center within a certain width.
aligned_text = f"{'Hello':<10}"  # Left-aligned within 10 characters
centered_text = f"{'Hello':^10}"  # Center-aligned within 10 characters
right_aligned_text = f"{'Hello':>10}"  # Right-aligned within 10 characters

print(f"Left aligned: '{aligned_text}'")  # Output: Left aligned: 'Hello     '
print(f"Center aligned: '{centered_text}'")  # Output: Center aligned: '  Hello   '
print(f"Right aligned: '{right_aligned_text}'")  # Output: Right aligned: '     Hello'

# 7. f-string with Multiple Variables
# You can include multiple variables and expressions inside a single f-string.
first_name = "John"
last_name = "Doe"
full_name = f"Full name: {first_name} {last_name}"
print(full_name)  # Output: Full name: John Doe

# 8. f-string with Variables in Complex Expressions
# You can also use complex expressions inside the curly braces.
x = 7
y = 3
complex_expression = f"The result of {x} raised to the power of {y} is {x ** y}."
print(complex_expression)  # Output: The result of 7 raised to the power of 3 is 343.

# 9. f-string with Dictionary
# You can access values from a dictionary inside an f-string.
person = {"name": "Charlie", "age": 25}
person_string = f"Name: {person['name']}, Age: {person['age']}"
print(person_string)  # Output: Name: Charlie, Age: 25
