class Employee():
    number_of_leaves = 8
    def __init__(self,aname,aage):
        self.name = aname
        self.age = aage

    def printdetail(self):
        return f"name is {self.name} age is {self.age}"

    @classmethod
    def change_leave(cls, newleaves):
        cls.number_of_leaves = newleaves
    def __add__(self, other):
        return self.age + other.age
    def __repr__(self):
        return f"Employee('{self.name}', {self.age})"
    def __str__(self):
        return f"name is {self.name} age is {self.age}"
class Role:
    def __init__(self,name ,rol,aukat):
        self.name = name
        self.rol = rol
        self.aukat = aukat
    def click(self):
        return f"this is {self.name} playing role of{self.rol} "
    def __pow__(self, other):
        return self.aukat ** other.aukat
    def __str__(self):
        return self.name
a = Role("rajni", "suresh", 2)
b = Role("karna" , 'bathura', 4)
print(a ** b)
print(a,b)



emp_1 = Employee("Tarun", 870)
emp_2 = Employee("Rohan", 786)
emp_3 = Employee("Ramesh", 680)
print(repr(emp_3))