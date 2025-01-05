"""
Python Operators and Their Examples

In Python, operators are special symbols or keywords used to perform operations on variables and values. Python supports various types of operators, categorized as:

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Membership Operators
7. Identity Operators

This file demonstrates the major operators in Python with examples.
"""

# 1. Arithmetic Operators
# Used for performing basic mathematical operations.
a = 10
b = 3

print("Addition:", a + b)       # 13
print("Subtraction:", a - b)    # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)        # 1
print("Exponentiation:", a ** b) # 1000

# 2. Comparison Operators
# Compare two values and return a Boolean result.
print("Equal:", a == b)           # False
print("Not Equal:", a != b)       # True
print("Greater than:", a > b)     # True
print("Less than:", a < b)        # False
print("Greater or Equal:", a >= b) # True
print("Less or Equal:", a <= b)    # False

# 3. Logical Operators
# Combine conditional statements.
x = True
y = False

print("Logical AND:", x and y)    # False
print("Logical OR:", x or y)      # True
print("Logical NOT:", not x)      # False

# 4. Bitwise Operators
# Perform bit-level operations on integers.
c = 5   # 0101 in binary
d = 3   # 0011 in binary

print("Bitwise AND:", c & d)      # 1 (0001)
print("Bitwise OR:", c | d)       # 7 (0111)
print("Bitwise XOR:", c ^ d)      # 6 (0110)
print("Bitwise NOT:", ~c)         # -6 (inverts all bits)
print("Left Shift:", c << 1)      # 10 (1010)
print("Right Shift:", c >> 1)     # 2 (0010)

# 5. Assignment Operators
# Used to assign values to variables.
e = 5
e += 3  # e = e + 3
print("Add and Assign:", e)       # 8
e -= 2  # e = e - 2
print("Subtract and Assign:", e)  # 6
e *= 2  # e = e * 2
print("Multiply and Assign:", e)  # 12
e /= 4  # e = e / 4
print("Divide and Assign:", e)    # 3.0
e %= 2  # e = e % 2
print("Modulus and Assign:", e)   # 1.0

# 6. Membership Operators
# Check if a value exists in a sequence (string, list, tuple, etc.).
nums = [1, 2, 3, 4, 5]
print("Is 3 in nums:", 3 in nums)      # True
print("Is 6 not in nums:", 6 not in nums) # True

# 7. Identity Operators
# Check if two objects are the same (memory reference).
f = [1, 2, 3]
g = [1, 2, 3]
h = f

# In Python, the 'is' operator checks whether two variables point to the same object in memory, not whether their values are equal.
print("f is g:", f is g)           # False (different objects)
print("f is h:", f is h)           # True (same object)
print("f is not g:", f is not g)   # True
