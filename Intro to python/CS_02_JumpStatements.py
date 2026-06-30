# Break Statement
a = b = c = 0
for i in range (1,11):
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))
    if b == 0:
        print("Division by zero is not allowed")
        break
    else:
        c = a/b
        print("The result of division is",c)

# Continue Statement
"""a = b = c = 0
for i in range (1,11):
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))
    if b == 0:
        print("Division by zero is not allowed")
        continue
    else:
        c = a/b
        print("The result of division is",c)"""