# dictionary_example.py

# 1. Creating Dictionary
# A dictionary is an Ordered(in earlier version unordered) collection of key-value pairs.
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Original Dictionary:", my_dict)

# 2. Accessing Values by Key
# You can access values in a dictionary by using the key.
name = my_dict["name"] # raise error if not present
print("Name:", name)  # Output: John

# 3. Using get() Method for Access
# The `get()` method is used to access values. It does not raise an error if the key is not found.
age = my_dict.get("age")
print("Age:", age)  # Output: 30
address = my_dict.get("address", "Not Available")  # Returns "Not Available" if key does not exist
print("Address:", address)  # Output: Not Available

# 4. Adding Key-Value Pairs to a Dictionary
# You can add a new key-value pair to a dictionary using the key.
my_dict["email"] = "john@example.com"
print("Dictionary after adding email:", my_dict)

# 5. Updating Values in a Dictionary
# You can update the value of an existing key by assigning a new value to the key.
my_dict["age"] = 31  # Update age
print("Dictionary after updating age:", my_dict)

# 6. Removing Key-Value Pairs
# You can remove a key-value pair using the `del` keyword.
del my_dict["city"]
print("Dictionary after deleting city:", my_dict)

# 7. Popping Elements from a Dictionary
# The `pop()` method removes and returns the value associated with a given key.
email = my_dict.pop("email")
print("Removed email:", email)  # Output: john@example.com
print("Dictionary after popping email:", my_dict)

# 8. Iterating Through Keys and Values
# You can iterate through a dictionary using a for loop.
print("Keys and Values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 9. Checking if a Key Exists
# You can check if a key exists in the dictionary using the `in` keyword.
print("Is 'name' a key in the dictionary?", "name" in my_dict)  # Output: True
print("Is 'city' a key in the dictionary?", "city" in my_dict)  # Output: False

# 10. Dictionary Length
# You can get the number of key-value pairs in the dictionary using `len()`.
print("Number of items in the dictionary:", len(my_dict))  # Output: 2

# 11. Copying a Dictionary
# You can create a shallow copy of a dictionary using the `copy()` method.
dict_copy = my_dict.copy()
print("Copy of the dictionary:", dict_copy)

# 12. Clearing the Dictionary
# You can remove all items from the dictionary using the `clear()` method.
my_dict.clear()
print("Dictionary after clearing:", my_dict)  # Output: {}

# 13. Nested Dictionary
# Dictionaries can also contain other dictionaries as values.
nested_dict = {
    "person1": {"name": "Alice", "age": 28},
    "person2": {"name": "Bob", "age": 34}
}
print("Nested Dictionary:", nested_dict)

# Accessing values inside a nested dictionary
person1_name = nested_dict["person1"]["name"]
print("Person1 Name:", person1_name)  # Output: Alice
