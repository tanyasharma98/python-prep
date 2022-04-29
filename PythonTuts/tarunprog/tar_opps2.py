class Employee():
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
        # param= str.split(("-"))
        # print(param)
        # return cls(param[0],param[1])
        return cls(*str.split("-"))


tarun = Employee("Tarun", 21)
harry = Employee("Harry", 23)
larry = Employee.from_dash("larry-54")
harry.change_leave(34)
# tarun.name = "Tarun"
# tarun.age = 21
#
# harry.name = "Harry"
# harry.age = 23
# print(tarun.printdetail())
# print(harry.number_of_leaves)
print(harry.age)
