for a in range(1,4):
    if a%2 ==0:
        break
        print("The number is ",end="")
        print(a)
    else :
        print("The number is not divisible by 8")

a = int(input("Enter a number : "))
while(a>0):
    print("The number is ",end="")
    print(a)
    a = a-1