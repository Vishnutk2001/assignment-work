a = int(input("enter a number"))
b = int(input("enter another number"))
print("prime numbers in range")
for num in range (a,b+1):
    if num > 1:
        for i in range (2 , num):
            if num % i == 0:
                break
        else:
            print(num)

