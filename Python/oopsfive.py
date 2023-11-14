class Calculation:

    def fibonacci(self, n):
        f1 = 1
        f2 = 2
        print("fibonacci series is:")
        print(f1)
        print(f2)
        for i in range(3, n + 1):
            f3 = f1 + f2
            print(f3)
            f1 = f2
            f2 = f3

    def factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print(fact, " is factorial of the number", n)

    def oddeven(self, n):

        if n % 2 == 0:
            print("number is even")
        else:
            print("number is odd")

    def primeornot(self, n):
        fl = 0
        if n == 1:
            print(n, "not prime number")
        elif n > 1:
            for i in range(2, n):
                if n % i == 0:
                    fl = 1
                    break
        if fl == 0:
            print(n, "is prime number")
        else:
            print(n, "is not prime number")

    def perfect(self, n):
        sums = 0
        flag = n
        for i in range(1, n):
            rem = n % i
            if rem == 0:
                sums += i
        if sums == flag:
            print(flag, " is a perfect number")
        elif sums > flag:
            print(flag, "is abundant")
        else:
            print(flag, "is deficient")


calculate = Calculation()
num = int(input("Enter a number:"))
calculate.oddeven(num)
calculate.primeornot(num)
calculate.perfect(num)
calculate.factorial(num)
calculate.fibonacci(num)
