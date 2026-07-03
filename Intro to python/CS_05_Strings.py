# Strings in python 
""" 0 1 2 3 4 5
    P y t h o n
    -5 -4 -3 -2 -1""" # forward and backward indexing in strings
s = "python"
print(len(s))
print(s[0])  # Accessing the first character
# Traversing in string
for ch in s:
    print(ch,'~ ',end='')  

# String Operators
print("Hello " + "World")  # Concatenation
print("Hello " * 3)  # Repetition

#>> membership operators 
# <string> in/not in <string>  # returns True if substring is found in string
print("y" in s)  # True
print("v" in "vaibhav")

# Comparison Operators
print("Hello" == "Hello")  # True
print("Hello" != "World")  # True
# to get the ASCII value of the character
print(ord('X'))

# String Functions 
str = "hey, there"
print(len(str))  # Length of the string
print(str.isdigit())  # Check if all characters are digits
print(str.isspace())  # Check if all characters are whitespace
print(str.isupper())  # Check if all characters are uppercase
print(str.upper())  # Convert to uppercase
print(str.swapcase())  # Swap case of each character

