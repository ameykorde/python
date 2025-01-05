# enumerate_example.py

# Problem:
# When iterating over a list (or other iterable) and you need both the index and the value,
# you might be tempted to use a counter variable manually. This can be error-prone and
# less readable. Let's look at an example of the problem:

my_list = ["apple", "banana", "cherry"]

# Problematic Approach: Manually keeping track of the index
index = 0
for item in my_list:
    print(f"Index {index}: {item}")
    index += 1  # Manually incrementing the index

# This works, but it is less clean and error-prone. We must manually track the index.

# Solution: Using enumerate()

# The `enumerate()` function simplifies this by automatically providing both the index and the value in a loop.
print("\nUsing enumerate():")

for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")

# What `enumerate()` returns:
# The `enumerate()` function returns an enumerate object, which is an iterator that produces tuples.
# Each tuple contains two elements: the index and the corresponding value from the iterable.
# In the loop, it automatically unpacks the tuple into `index` and `item`.

# You can also specify the starting index using the `start` parameter.

print("\nUsing enumerate() with a custom start index:")

for index, item in enumerate(my_list, start=1):  # Start the index at 1 instead of 0
    print(f"Index {index}: {item}")

# Example of converting the enumerate object to a list (or any other collection type):
enumerate_list = list(enumerate(my_list))
print("\nEnumerate as a list of tuples:", enumerate_list)

# The result is a list of tuples where each tuple contains an index and the corresponding item from the iterable.
