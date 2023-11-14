class Calculation:

    def addnum(self, a, b):
        c = a + b
        print(c)
        self.sum = c

    @staticmethod
    def subnum(a, b):
        c = a - b
        print(c)

    def multnum(self, a, b):
        c = a * b * self.sum
        print(c)

    @staticmethod
    def divnum(a, b):
        c = a / b
        print(c)

    @staticmethod
    def squnum(a):
        c = a ** 2
        print(c)


calculate = Calculation()
calculate.addnum(100, 20)
calculate.subnum(200, 150)
calculate.multnum(20, 30)
calculate.divnum(120, 20)
calculate.squnum(30)
