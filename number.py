n = int(input("enter a number"))
temp = n
rev = 0
while n > 0:
    num = n % 10
    rev = rev * 10 + num
    n = n // 10
if temp == rev:
    print("palindrome number")
else:
    print("Not a palindrome number")
