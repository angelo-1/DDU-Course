num = int(input("Enter a number:"))
fl = 0
if num == 1:
    print(num, "not prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            fl = 1
            break
if fl == 0:
    print(num, "is prime number")
else:
    print(num, "is not prime number")
