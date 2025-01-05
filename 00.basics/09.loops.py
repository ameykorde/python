# loops_example.py
# No do while in python
# 1. For Loop: Iterating over a range of numbers
print("For Loop Example:")
for i in range(5):  # range(5) will generate numbers from 0 to 4
    print(f"Iteration {i + 1}: {i}")  # Print the current iteration number and value

for i in range(1,5,2):
    print(i) # 5 not included # 1 3

# 2. For Loop: Iterating over a list
print("\nFor Loop with List Example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")  # Prints each fruit in the list

# 3. For Loop: Iterating over a dictionary (key-value pairs)
print("\nFor Loop with Dictionary Example:")
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")  # Prints each key-value pair in the dictionary

# dictionary_methods_example.py
# Sample dictionary
person = {"name": "John", "age": 30, "city": "New York"}
# 1. Using items() to iterate over key-value pairs
print("Using items() to get key-value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")
# 2. Using keys() to iterate over keys only
print("\nUsing keys() to get keys only:")
for key in person.keys():
    print(key)
# 3. Using values() to iterate over values only
print("\nUsing values() to get values only:")
for value in person.values():
    print(value)


# 4. While Loop: Runs as long as the condition is True
print("\nWhile Loop Example:")
counter = 0
while counter < 5:
    print(f"Counter value: {counter}")  # Prints the current counter value
    counter += 1  # Increment counter by 1 to eventually break the loop

# 5. Nested Loop Example: A loop inside another loop
print("\nNested Loops Example:")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer loop iteration {i}, Inner loop iteration {j}")

# 6. For Loop with Break Statement: Breaking out of the loop
print("\nFor Loop with Break Example:")
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i equals 5
    print(f"i: {i}")

# 7. For Loop with Continue Statement: Skipping an iteration
print("\nFor Loop with Continue Example:")
for i in range(5):
    if i == 3:
        print("Skipping iteration at i =", i)
        continue  # Skip the rest of the loop when i equals 3
    print(f"i: {i}")

# 8. For Loop with Else: Executes after the loop FINISHES not executes if loops BREAKS
print("\nFor Loop with Else Example:")
for i in range(3):
    print(f"Iteration {i + 1}: {i}")
else:
    print("For loop has completed all iterations.")  # This block runs after the loop ends

# 9. Nested loops

colors = ["Red","Green","Blue"]
for color in colors:
    print(color)
    for i in color:
        print(i)
'''
Red
R
e
d
Green
G
r
e
e
n
Blue
B
l
u
e
'''