# set_example.py

# 1. Creating a Set is an "UNORDERED" collection of unique elements.
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# 2. Adding Elements to a Set
# You can add a single element to a set using the `add()` method.
my_set.add(6)
print("Set after adding 6:", my_set)

# 3. Adding Multiple Elements to a Set
# You can also add multiple elements at once using the `update()` method.
my_set.update([7, 8, 9])
print("Set after adding multiple elements:", my_set)

# 4. Removing Elements from a Set
# You can remove an element using the `remove()` method. If the element is not present, it raises a KeyError.
my_set.remove(3)
print("Set after removing 3:", my_set)

# 5. Discarding Elements from a Set
# You can also use the `discard()` method to remove an element, but it does not raise an error if the element is not found.
my_set.discard(10)  # 10 is not in the set, no error will be raised
print("Set after discarding 10 (not present):", my_set)

# 6. Popping an Element from a Set
# The `pop()` method removes and returns an arbitrary element from the set. It raises a KeyError if the set is empty.
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after popping an element:", my_set)

# 7. Checking Membership in a Set
# You can check if an element is in the set using the `in` keyword.
print("Is 4 in the set?", 4 in my_set)  # Output: True
print("Is 10 in the set?", 10 in my_set)  # Output: False

# 8. Set Operations: Union
# Union combines all elements from two sets, removing duplicates.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# 9. Set Operations: Intersection
# Intersection returns elements that are common to both sets.
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# 10. Set Operations: Difference
# Difference returns elements that are in the first set but not in the second set.
difference_set = set1.difference(set2)
print("Difference of set1 and set2 (set1 - set2):", difference_set)

# 11. Set Operations: Symmetric Difference
# Symmetric difference returns elements that are in either of the sets, but not both.
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)

# 12. Set Length
# You can get the number of elements in a set using `len()`.
print("Number of elements in set1:", len(set1))

# 13. Set Copy
# You can create a shallow copy of a set using the `copy()` method.
set_copy = set1.copy()
print("Copy of set1:", set_copy)

# 14. Set Clear
# You can remove all elements from the set using the `clear()` method.
set1.clear()
print("Set1 after clear:", set1)

# 15. Empty Set
harry = set()