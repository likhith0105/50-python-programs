#(except zero):
number = input("enter an number: ")
carpim = 1
for digitofnumber in str(number):
    if int(digitofnumber) != 0:
        carpim *= int(digitofnumber)
print("digits of the number: ", carpim)