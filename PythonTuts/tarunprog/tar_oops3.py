class Employee():
    number_of_leaves = 8
    def __init__(self,aname,aage):
        self.name = aname
        self.age = aage
    #
    def printdetail(self):
        return f"name is {self.name} age is {self.age}"

    @classmethod
    def change_leave(cls, newleaves):
        cls.number_of_leaves = newleaves

    @classmethod
    def from_dash(cls,str):
        return cls(*str.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good boy " +string)

tarun = Employee("Tarun",21)
harry = Employee("Harry", 23)
larry = Employee.from_dash("larry-54")
harry.change_leave(34)
Employee.printgood("tarun")
harry.printgood("rohan")

