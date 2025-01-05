# tuple_example.py

# 1. Creating a Tuple
# Tuples are created by placing values inside parentheses `()`, separated by commas.
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# 2. Accessing Tuple Elements
# You can access tuple elements using indices. Indices start from 0.
print("First element:", my_tuple[0])  # Output: 1
print("Last element:", my_tuple[-1])  # Output: 5  (negative index starts from the end)

# 3. Slicing a Tuple # returns new tuple
# Slicing allows you to extract a part of the tuple.
# Syntax: tuple[start_index:end_index] (end_index is not included)
print("Slice (from index 1 to 3):", my_tuple[1:4])  # Output: (2, 3, 4)

# 4. Concatenating Tuples
# You can concatenate two or more tuples using the + operator.
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated Tuple:", concatenated_tuple)

# 5. Repeating a Tuple
# The * operator is used to repeat the elements of a tuple.
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)

# 6. Checking Membership
# You can check if an element exists in a tuple using the `in` keyword.
print("Is 3 in the tuple?", 3 in my_tuple)  # Output: True

# 7. Nested Tuples (Tuples inside Tuples)
# Tuples can contain other tuples (nested tuples).
nested_tuple = (1, (2, 3), 4)
print("Nested Tuple:", nested_tuple)

# To access elements in a nested tuple, you use multiple indices.
print("Element inside nested tuple:", nested_tuple[1][0])  # Output: 2 (accessing 2 inside (2, 3))

# 8. Tuple with Single Element
# When creating a tuple with a single element, a comma is necessary to distinguish it from a regular value.
single_element_tuple = (5,)  # Single-element tuple needs a trailing comma.
print("Single element tuple:", single_element_tuple)

# If you omit the comma, it is not a tuple but just the value inside parentheses.
not_a_tuple = (5)
print("Not a tuple:", not_a_tuple)  # This will just print 5, not a tuple

# ERROR if tries to modify the tuple
single_element_tuple[0] = 2

# CONVERTING TUPLE INTO LIST
# 1. Creating a Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# 2. Converting Tuple to List
# Since tuples are immutable, we first convert it to a list to modify the elements.
my_list = list(my_tuple)

# 3. Adding an Item to the List
# Now we can add an item to the list using the append() method.
my_list.append(6)
print("List after adding an item:", my_list)

# 4. Converting List Back to Tuple
# After modifying the list, we convert it back to a tuple using the tuple() function.
my_tuple = tuple(my_list)
print("Tuple after adding an item:", my_tuple)

# 5. Verifying the Tuple is Modified
# The tuple now contains the newly added element.
print("Final Tuple:", my_tuple)

# Index
# tuple.index(value, start, end)
my_tuple = (10, 20, 30, 40, 50, 20, 60)

# 2. Using the index() method to find the index of an element
index_of_20 = my_tuple.index(20)
print("The index of 20 is:", index_of_20)  # Output: 1 (first occurrence of 20)

# 3. Using the index() method with start and end parameters
# Searching from index 2 to the end of the tuple
index_of_20_from_index_2 = my_tuple.index(20, 2)
print("The index of 20 from index 2 onward is:", index_of_20_from_index_2)  # Output: 5

# 4. Handling ValueError if the element is not found
try:
    index_of_100 = my_tuple.index(100)
except ValueError:
    print("ValueError: 100 is not in the tuple.")