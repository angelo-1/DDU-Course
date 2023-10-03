x = int(input("enter a year:"))

if x % 4 == 0 and x % 100 != 0:
    print("year is leap year")
elif x % 400 == 0 and x % 100 == 0:
    print("year is leap year")
else:
    print("not leap year")
