class Employee:
    number_of_leaves = 8

    def __init__(self, aname, aage):
        self.name = aname
        self.age = aage

    def printdetail(self):
        return f"name is {self.name} age is {self.age}"

    @classmethod
    def change_leave(cls, newleaves):
        cls.number_of_leaves = newleaves

    @classmethod
    def from_dash(cls, str):
        return cls(*str.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good boy " +string)


class Programmer(Employee):
    def __init__(self,aname,aage,planguage):
        self.name = aname
        self.age = aage
        self.language = planguage

    def  printprog(self):
        return f"name is {self.name} age is {self.age} and languaes is {self.language}"

tarun = Employee("Tarun",21)
harry = Employee("Harry", 23)
rohan =Programmer.from_dash("rohan-56-['python','c++']")
print(rohan.printprog())
