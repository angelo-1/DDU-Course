# def fun(n):
#     if n != 0:
#         fun(n - 1)
#         print(n)
#
#
# fun(10)

def fun(num):
    if num != 0:
        fun(num - 1)
        print("{}*{}={}".format(num, a, num * a))


num = int(input("Enter the limit:"))
a = int(input("Enter the number:"))
fun(num)
