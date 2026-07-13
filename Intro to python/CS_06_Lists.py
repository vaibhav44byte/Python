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

print("Reverse list",LIST[::-1])
# Joining two lists
print(LIST + [2,3,4]) # Concatenation of lists
print(LIST*3) # Repetition of list

## List Manupulation
LIST.append(5) # Adding element at the end of the list
LIST[2] = 10 # Changing the value of an element
LIST.pop(1) # Removing element at index 1
print(LIST)

## List Functions 
LIST.index(5) # Returns the index of first occurrence of 5
t1 = [1, 3, 5]
t2 = [2, 4, 6]
t1.extend(t2) # Extending t1 with elements of t2
print(t1)
LIST.count(5) # Returns the number of occurrences of 5 in the list
LIST.reverse() # Reverses the list
LIST.sort() # Sorts the list in ascending order
LIST.sort(reverse=True) # Sorts the list in descending order