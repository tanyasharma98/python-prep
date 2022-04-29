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

Kim_Namjoon = Employee("Kim" ,"Namjoon")
Kim_Taehyung =Employee("Kim" , "Taehyung")

# print(Kim_Namjoon.explain())
print(Kim_Taehyung.email)

Kim_Taehyung.fname="V"

print(Kim_Taehyung.email)

Kim_Namjoon.email = "This.That@gmail.com"
print(Kim_Namjoon.email)

del Kim_Namjoon.email
Kim_Namjoon.email ="Kimi.Shimmy@gmail.com"
print(Kim_Namjoon.email)
