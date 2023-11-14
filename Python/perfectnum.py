num = int(input("Enter a number:"))
sum = 0
flag = num
for i in range(1, num):
    rem = num % i
    if rem == 0:
        sum += i
if sum == flag:
    print(flag, " is a perfect number")
elif sum > flag:
    print(flag, "is abundant")
else:
    print(flag, "is deficient")
