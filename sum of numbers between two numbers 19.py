sumofnumbers = 0

num1 = int(input('first number: '))
num2 = int(input('second number: '))

for i in range(num1 + 1, num2):
    sumofnumbers += i

print("Sum of numbers between {0} and {1} : {2}".format(num1, num2, sumofnumbers))