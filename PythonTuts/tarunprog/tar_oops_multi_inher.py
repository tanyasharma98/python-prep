class Employee:
    number_of_leaves = 8
    def __init__(self,aname,aage):
        self.name = aname
        self.age = aage
    def printdetails(self):
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
class Player:
    number_of_games=4
    def __init__(self,name,game):
        self.name= name
        self.game =game
    def printdetail(self):
        return f"name is {self.name} game is {self.game}"


class CoolProgrammer(Employee ,Player):
    language = "C++"
    def printlanguages(self):
        print(self.language)



tarun = Employee("Tarun",21)
harry = Employee("Harry", 23)
karan= CoolProgrammer("karan", 54)
print(karan.printdetails())