b = input("enter student name")
a = int(input("enter mark of student in english exam"))
if 90 < a <= 100:
    print(b + " has A+ grade in english")
elif 80 < a <= 90:
    print(b + " has A grade in english")
elif 70 < a <= 80:
    print(b + " has B+ grade in english")
elif 60 < a <= 70:
    print(b + " has B grade in english")
elif 50 < a <= 60:
    print(b + " has C+ grade in english")
elif 40 < a <= 50:
    print(b + " has C grade in english")
elif 30 < a <= 40:
    print(b + " has D+ grade in english")
else:
    print(b + " not passed in english")
