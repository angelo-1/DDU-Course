num = int(input("Enter a number"))
sum = 0
while (num):
    n = num % 10
    sum = sum + n
    num = int(num / 10)
print("sum of digit is:", sum)
