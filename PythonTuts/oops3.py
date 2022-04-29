class Employee:
    no_of_leaves = 8

    def __init__(self,aname, aage, adept):
        self.name= aname
        self.age= aage
        self.dept = adept

    def printdetails(self):
        return f"This is {self.name}. My age is{self.age}and department is{self.dep}"

tanya = Employee("tanya",40,"worldclass")
# gonya = Employee()
#
# tanya.name= "Tanya"
# tanya.age =22
# tanya.dep= "WorldClass"

# gonya.name ="Gonya"
# gonya.age=300
# gonya.dep="Nalii"


print(tanya.name)

