# is_vs_equals.py

# Explanation of 'is' and '==' in Python
# --------------------------------------
# - `is`: Checks if two variables refer to the same object in memory (identity comparison).
# - `==`: Checks if the values of two variables are equal (value comparison).

# Example 1: Using '==' (value comparison)
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True, because the values of 'a' and 'b' are the same

# Example 2: Using 'is' (identity comparison)
print(a is b)  # Output: False, because 'a' and 'b' are different objects in memory

# Example 3: 'is' with immutable types (like integers and strings)
x = 100
y = 100

print(x == y)  # Output: True, because the values of 'x' and 'y' are the same
print(x is y)  # Output: True, because Python reuses small immutable objects (like integers between -5 and 256)

# Example 4: 'is' with mutable types (like lists)
m = [1, 2, 3]
n = m  # Both 'm' and 'n' point to the same object

print(m == n)  # Output: True, because the values of 'm' and 'n' are the same
print(m is n)  # Output: True, because 'm' and 'n' refer to the same object

# Modifying 'm' will also affect 'n'
m.append(4)
print(n)  # Output: [1, 2, 3, 4], because 'm' and 'n' are the same object

# Example 5: '==' vs 'is' with None
var1 = None
var2 = None

print(var1 == var2)  # Output: True, because their values are equal
print(var1 is var2)  # Output: True, because they refer to the same singleton None object

# Key Points:
# - Use `is` when checking identity (e.g., `None`, singleton objects).
# - Use `==` when checking if two variables have the same value.

# Output:
# -------
# True
# False
# True
# True
# True
# True
# [1, 2, 3, 4]
# True
# True
