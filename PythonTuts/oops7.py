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
        return cls(*string.split("-"))
    @staticmethod
    def priintThinhs(sting):
        print("This is good" +sting)

class programmer(Employee):
    no_of_holiday = 60
    def __init__(self ,aname , aage , adept, language):
        #Will do it later #inherit-----super
        self.name = aname
        self.age = aage
        self.dept = adept
        self.language = language

    def printyprint(self):
        return f"This is programmer {self.name}. My age is{self.age}and department is{self.dept}. and language is{self.language}"

tanya = Employee("tanya",40,"worldclass")
gonya = Employee("gonya",37,"nalli")
ponyoo = Employee.stringshig("ponyoo-30-swear")

kiolo= programmer("Kiolo",49,"Jail",["python" ,"C++"])
print(kiolo.printyprint())
print(kiolo.no_of_holiday)
# ponyoo.priintThinhs("Tanya")
# Employee.priintThinhs("ingo")