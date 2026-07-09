## Tuple in Python
# () tuples are immutable data structures in Python that can hold a collection of items. They are similar to lists, but unlike lists, tuples cannot be changed after they are created. Tuples are defined by enclosing the items in parentheses `()`.
T = () # Empty tuple
t1 = (1, 2, 3) # Tuple of integers
T = tuple([1]) # Tuple from a list
t2 = tuple('hello') # Tuple of characters from string
L = ['s','d','f'] # List of characters
t3 = tuple(L) # Tuple from a list
print(t3)
## Taking input 
t3 = tuple(input("Enter tuple elements : ")) # Taking input from user
print(t3)

# accessing elements in a tuple
print(t3[2]) # Accessing the third element of the tuple
L[1] = 'h'
# t3[1] = 'h' This will raise an error because tuples are immutable

# traversing in a tuple
for i in t3:
    print(i,end=' ')

tup = (1, 2, 3, 4, 5) 
print(tup[1:4]) # Slicing the tuple to get elements from index 1 to 3