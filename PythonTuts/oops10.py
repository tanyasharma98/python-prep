class Employee:
    no_of_leaves = 8
    var =1
    _protec =9   #protected
    __private =98  #private ---- used witn name-mangling

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
class player:
    no_of_games = 4
    var=2

    def __init__(self,name , game):
        self.name = name
        self.game= game

    def printdetails(self):
        return f"This is {self.name}. My game is{self.game}"

class coolprog( player,Employee ):
    language ="C++"
    # var=3

    def printlangua(self):
        print(self.language)


tanya = Employee("tanya",40,"worldclass")
gonya = Employee("gonya",37,"nalli")
ponyoo = Employee.stringshig("ponyoo-30-swear")

filo= player("filoo","Hathi-GhoDA")
tullu = coolprog("tullu","mcd ")

emp = Employee("Goku",50,"Protected")
print(emp.printdetails())
print(emp._protec)
print(emp._Employee__private)  # Namemangling


#Abstraction
#Encapsulation-0
#Inheritance
#Polymorphisum