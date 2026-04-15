
salary = input("enter salary: ")
raise_rate = input("salary raise rate(%): ")
newsalary = int(salary) + (int(salary) * int(raise_rate) / 100)
print("increased salary:", newsalary)