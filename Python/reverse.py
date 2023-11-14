num = int(input("Enter a number:"))
rever = 0
while num != 0:
    digits = num % 10
    rever = rever * 10 + digits
    num = int(num / 10)
# print("reverse number is"+str(rever))
print("revers number is", rever)
