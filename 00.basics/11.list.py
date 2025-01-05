# lists_example.py

# 1. Creating Lists
print("1. Creating Lists:")

# A simple list of numbers
numbers = [1, 2, 3, 4, 5]
print("List of numbers:", numbers)

# A list of strings
fruits = ["apple", "banana", "cherry"]
print("List of fruits:", fruits)

# A mixed list containing different data types (integers, strings, and booleans)
mixed_list = [1, "hello", True, 3.14]
print("Mixed list:", mixed_list)

# 2. Accessing List Elements
print("\n2. Accessing List Elements:")

# Accessing the first element (index starts from 0)
print("First element of numbers:", numbers[0])  # Output: 1

# Accessing the last element using negative indexing
print("Last element of fruits:", fruits[-1])  # Output: cherry

# Accessing a slice of the list (from index 1 to 3, not including index 3)
print("Slice of numbers (index 1 to 2):", numbers[1:3])  # Output: [2, 3]

# 3. Modifying Lists
print("\n3. Modifying Lists:")

# Changing an element in the list by its index
fruits[1] = "blueberry"
print("Modified fruits list:", fruits)

# Appending a new element to the list
fruits.append("grape")
print("Fruits after appending 'grape':", fruits)

# Inserting an element at a specific index
fruits.insert(1, "orange")
print("Fruits after inserting 'orange' at index 1:", fruits)

# Removing an element by value
fruits.remove("orange")
print("Fruits after removing 'orange':", fruits) # gives error if element not present

# Popping an element (removes the last element by default)
last_fruit = fruits.pop()
print("Last fruit removed:", last_fruit)
print("Fruits after popping the last element:", fruits)

# 4. List Operations
print("\n4. List Operations:")

# Concatenating lists using + operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Concatenated list:", combined_list)

# Repeating a list using * operator
repeated_list = [0] * 4
print("Repeated list:", repeated_list)

# Checking if an item is in the list
print("Is 'apple' in fruits?", "apple" in fruits)  # Output: True

# Finding the index of an element in the list
print("Index of 'cherry' in fruits:", fruits.index("cherry"))  # Output: 1 # gives error is element not found

# Counting occurrences of an element in the list
numbers_with_duplicates = [1, 2, 3, 1, 1, 4, 5]
print("Count of 1 in numbers_with_duplicates:", numbers_with_duplicates.count(1))  # Output: 3

# 5. List Comprehension
print("\n5. List Comprehension:")

# Using list comprehension to create a new list where each number is squared
squared_numbers = [x ** 2 for x in numbers]
print("Squared numbers:", squared_numbers)

# Filtering a list to keep only even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers from numbers:", even_numbers)

# 6. Nested Lists
print("\n6. Nested Lists:")

# A list containing other lists (nested list)
nested_list = [[1, 2, 3], ["apple", "banana", "cherry"], [True, False]]
print("Nested list:", nested_list)

# Accessing an element in a nested list
print("First element of the second list inside nested_list:", nested_list[1][0])  # Output: apple

# COPY of list
l = [1, 2, 3]
# m = l # reference is copied # any modification in m will reflect in l also
m = l.copy()