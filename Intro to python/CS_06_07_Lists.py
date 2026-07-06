# List in python
# Lists are mutable

my_list = [] # Empty list
L = list() # Empty list using list constructor
l1 = list("Hello") # List of characters from string
print(l1)

## Taking Input from the user
LIST = list(input("enter list elements : "))
print(LIST)
print(len(LIST)) # Length of the list

print(LIST[0]) # First element of the list

## Traversing in list
for i in LIST:
    print(i, end=' ')

# Joining two lists
print(LIST + [2,3,4]) # Concatenation of lists