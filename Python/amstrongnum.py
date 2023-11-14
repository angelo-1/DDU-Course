num = 407
order = len(str(num))
sum = 0
arms = num
while arms > 0:
    digits = arms % 10
    sum += digits ** order
    arms //= 10
if num == sum:
    print(num, "is Armstrong number")
else:
    print(num, "is  not Armstrong number")
