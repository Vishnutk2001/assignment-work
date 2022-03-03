namelist = []
agelist = []
deslist = []
salarylist = []
count = int(input("employee details"))
for i in range (0,count):
    name = input("enter the name")
    age = input("enter the age")
    des = input("enter designation")
    salary = input("enter salary")
    namelist.append(name)
    agelist.append(age)
    deslist.append(des)
    salarylist.append(salary)
print(namelist)
print(agelist)
print(deslist)
print(salarylist)
