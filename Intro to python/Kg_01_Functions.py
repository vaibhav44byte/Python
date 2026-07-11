def total_pay(hrs_pay):

    # pre tax paymet calculation
    pre_tax = hrs_pay * 15

    # after tax payment calculation
    after_tax = pre_tax * (0.88)

    return after_tax
# for generating the output result on screen
x = total_pay(10)
print(x)

## Pure and Impure functions
# Pure functions --
def pure_function(x,y):
    return x*y

print(pure_function(2,3))

n = 10
# Impure functions --
def impure_function(x):
    return x*n

print(impure_function(2))


def addnumbers(a,b):
    return a+b

print(addnumbers(2,3))