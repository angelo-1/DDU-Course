num = int(input("Enter the number of fibonacci series:"))
f1 = 1
f2 = 2
print(f1)
print(f2)
for i in range(3, num + 1):
    f3 = f1 + f2
    print(f3)
    f1 = f2
    f2 = f3
