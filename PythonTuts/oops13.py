class Employee:
    no_of_leaves = 8

    def __init__(self,aname, aage, adept):
        self.name= aname
        self.age= aage
        self.dept = adept

    def printdetails(self):
        return f"This is {self.name}. My age is{self.age}and department is{self.dept}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves
    def __add__(self, other):
        return self.age + other.age
    def __truediv__(self, other):
        return self.age / other.age


    def __repr__(self):
        return f"Employee is ( '{self.name}' ,'{self.age}','{self.dept}')"
    def __str__(self):
        return f"This is {self.name}. My age is {self.age}and department is {self.dept}"


    def is_not(a, b):
        return a.age is not  b.age
    def __lt__(self, other):
        return self.age<other.age

emp1 =Employee("tanya",30,"foni")
emp2 =Employee("gimki",60,"lopdi")
print(emp1)
print(repr(emp1))
print(emp1 is not emp2)
print(emp1< emp2)
# print(emp1 +emp2)
# print(emp1/emp2)