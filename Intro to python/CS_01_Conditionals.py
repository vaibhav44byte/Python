# if statements
x = 10
if x>5:
    print("x is greater than 5")
else: #punctuation(:)
    print("x is less than or equal to 5")

# if - elif Statements
runs = 50
if runs>50:
    print("You have scored more than 50 runs")
elif runs==50:
    print("You have scored 50 runs")
else:
    print("You have scored less than 50 runs")

# nested if statements
x = int(input("Enter 1 number"))
y = int(input("Enter 2 number"))
z = int(input("Enter 3 number"))
if x>y:
    if x>z:
        print("x is the greatest number")
    else:
        print("z is the greatest number")
else :
    if y>z:
        print("y is the greatest number")
    else:
        print("z is the greatest number")