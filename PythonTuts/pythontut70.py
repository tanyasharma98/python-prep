class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email= f"{fname}.{lname}@hoki.com"
    def explain(self):
        return f"This is {self.fname} {self.lname}"
    def email(self):
        return f" {self.fname}.{self.lname}@jojo.com"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return f"Email is not set"
        return f"{self.fname}.{self.lname}@soki.com "

    @email.setter
    def email(self,string):
        print('Setting Now....')
        name = string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname = name.split(".")[1]
    @email.deleter
    def email(self):
        self.fname= None
        self.lname = None
class A:
    def __init__(self,fname ,lname):
        self.fname =fname
        self.lname =lname
    def printing(self):
        return f"This is {self.fname} {self.lname}"
class B(A):
    pass
class C(B):
    pass

skillf =Employee("Skill" ,"F")
# print(skillf.email)
o= "this is string"
# print(type(skillf))
# print(id(skillf))
# print(dir(o))
# print(dir(skillf))
# print(id("This is string"))
# print(id("Thato thato"))

import inspect
# print(inspect.getmembers(skillf))
# print(inspect.isclass(skillf))
# print(inspect.isclass(Employee))
print(inspect.getmro(C))
tanya =A("Tanya","Sharma")
print(tanya.printing())
print(inspect.getmembers(tanya))
