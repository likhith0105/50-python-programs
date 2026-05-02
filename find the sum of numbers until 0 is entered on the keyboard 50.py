total=0
while True:
  num = float(input("enter a number: "))
  if num == 0:
    break
  total+=num
print("The sum of the numbers: ",total)