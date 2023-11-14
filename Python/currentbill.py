u = input("enter units: ")
u = int(u)
if u >= 0:
    if u <= 100:
        x = u * 10
    elif u <= 200:
        x = (100 * 10) + ((u - 100) * 15)
    elif u <= 300:
        x = (100 * (10 + 15)) + ((u - 200) * 20)
    elif u <= 400:
        x = (100 * (10 + 15 + 20)) + ((u - 300) * 25)
    elif u <= 500:
        x = (100 * (10 + 15 + 20 + 25)) + ((u - 400) * 30)
    elif u <= 600:
        x = (100 * (10 + 15 + 20 + 25 + 30)) + ((u - 500) * 35)
    a = "Total amount for {} units is {}"
    print(a.format(u, x))
else:
    print("unit is invalid")
