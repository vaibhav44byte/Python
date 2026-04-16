def total_pay(hrs_pay):
    # pre tax paymet calculation
    pre_tax = hrs_pay * 15
    # after tax payment calculation
    after_tax = pre_tax * (0.88)
    return after_tax
x = total_pay(10)
print(x)