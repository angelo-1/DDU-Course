# # public
class Example:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def biodata(self):
        print("Biodata: \n Name:", self.name, "\n Age:", self.age)


obj = Example("Angelo", 23)
obj.biodata()
obj.name = "Binu"
obj.biodata()

# private
# class Examplep:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def __biodata(self):
#         print("Biodata: \n Name:", self.__name, "\n Age:", self.__age)
#
#     # def fun(self):
#     #     self.__biodata()
#
#
# obj1 = Examplep("Angelo", 23)
# obj1._Examplep__biodata()
# # obj1.fun()
# obj1.name = "Binu"
# print("Name:", obj1.name)
# obj1._Examplep__biodata()

# protected

# class Examplepro:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def _biodata(self):
#         print("Biodata: \n Name:", self._name, "\n Age:", self._age)
#
#
# class Derived(Examplepro):
#     def __init__(self,name,age):
#         Examplepro.__init__(self,name,age)
#     def display(self):
#         self._biodata()
#
#
# obj2 = Derived("Angelo", 23)
# obj2.display()
# obj2.name = "Binu"
# obj2.display()
