name='raj'
print(name[0]) # r
# print(name[3]) # IndexError: string index out of range

name = "John"
age = 30
# Using f-string for formatting
print(f"My name is {name} and I am {age} years old.")

#--------------------------------------------------------------------
name='my name is raj' # same variable name not giving error
print(name[:5]) # my na (first 5 characters)
print(name[1:5]) # y na (starts from 1 ends at 4)
# name[start(inclusive), end(exclusive)]

print(len(name)) #14

print(name[0:-1]) #my name is ra
# pretend it as name[0: len(name)-1]

print(name[-3:-2]) # r
# name[len(name)-3, len(name)-2]
# name[14-3, 14-2]
# name[11,12]
# r

# string[start:stop:step] # u can say default step is 1
string1 = "abcdef"
result = string1[0:5:2] # 2 means skip 1 character
print(result)  # Output: "ace"

# ---------------------------------------------------------------------

# STRING FUNCTIONS - Strings are immutable in python

a = "!!Rohan!!!"
print(a.upper()) # returns new string with uppercase
print(a.lower()) # !!rohan!!!

# strip # by default strip removes whitespaces
print(a.rstrip('!')) # !!Rohan
print(a.lstrip('!')) # Rohan!!!
print(a.strip('!')) # Rohan

# replace # string.replace(old, new, count)
'''
old: The substring you want to replace.
new: The substring you want to replace old with.
count (optional): The maximum number of occurrences to replace.
If omitted, all occurrences of old are replaced.
'''
text = "Python is great. Python is versatile."
result = text.replace("Python", "Java")
print(result)  # Output: "Java is great. Java is versatile."

text = "Python, Python, Python!"
result = text.replace("Python", "Java", 2)
print(result)  # Output: "Java, Java, Python!"

# The replace() method is case-sensitive:
text = "Python is fun!"
result = text.replace("python", "Java")
print(result)  # Output: "Python is fun!" (no replacement made)

# The method can replace even partial matches within words:
text = "mississippi"
result = text.replace("iss", "123")
print(result)  # Output: "m123123ippi"

# split # string.split([separator], [maxSplit])
'''
separator (optional): The delimiter string on which the split will occur.
If omitted or None, it defaults to whitespace (including spaces, tabs, and newlines).
maxSplit (optional): The maximum number of splits to perform.
If omitted, all possible splits are made.
Returns:
A list of substrings.
'''
text = "Hello World! Welcome to Python."
result = text.split()
print(result)  # Output: ['Hello', 'World!', 'Welcome', 'to', 'Python.']

text = "apple,banana,cherry"
result = text.split(",")
print(result)  # Output: ['apple', 'banana', 'cherry']

text = "one,two,three,four"
result = text.split(",", 2)
print(result)  # Output: ['one', 'two', 'three,four']

# If the separator is not found, the entire string is returned as a single-element list:
text = "Hello World!"
result = text.split(",")
print(result)  # Output: ['Hello World!']

# rsplit(): Splits a string starting from the right, allowing control over splitting behavior when using maxSplit:
text = "a,b,c,d"
result = text.rsplit(",", 2)
print(result)  # Output: ['a,b', 'c', 'd']

# splitlines(): Splits a string at line breaks (\n, \r, or both):
text = "First line\nSecond line\nThird line"
result = text.splitlines()
print(result)  # Output: ['First line', 'Second line', 'Third line']

# capitalize
header = "introduction tO jS"
print(header.capitalize()) # Introduction to js

# count
print(header.count('n')) # 2

# endswith()
print(header.endswith('js')) # False
print(header.endswith(' jS')) # True
print(header.endswith('on', 10, 12)) # True

# find()
# gives index of first occurrence
# if not present then returns -1
print(header.find('on')) # 10

# index()
# gives index of first occurrence
# if not present then raises an EXCEPTION : substring not found
print(header.index('on')) # 10
# print(header.index('z')) # Exception
