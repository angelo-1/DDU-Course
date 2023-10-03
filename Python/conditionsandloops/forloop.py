for i in range(1, 101):
    print(i)

for i in range(1, 30, 2):
    if i == 11:
        continue
    print(i)

a = [1, 2, 3, 4, 5]
b = [11, 22, 33, 44, 55]
c = [21, 31, 41, 51, 61]
for i in a:
    for j in b:
        for k in c:
            print(i, j, k)
# sum of natural numbers
sumn = 0
for i in range(0, 11, 2):
    sumn = sumn + i
print(sumn)

a = input("Enter first name:")
b = input("Enter second name:")
sorta = sorted(a)
sortb = sorted(b)
if sorta == sortb:
    print("Letters of given words are same")
else:
    print("Letters of the given words are different")
