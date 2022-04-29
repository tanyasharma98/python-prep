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

    @classmethod
    def stringshig(cls,string):
        # params = string.split("-")
        # return cls(params[0], params[1],params[2])
        return cls(*string.split("-"))


tanya = Employee("tanya",40,"worldclass")
gonya = Employee("gonya",37,"nalli")
ponyoo = Employee.stringshig("ponyoo-30-swear")
# tanya.change_leaves(50)
# Employee.change_leaves(30)
# Employee.no_of_leaves=40 --------- first visit Instance then class variable
print(ponyoo.age)
print(ponyoo.no_of_leaves)