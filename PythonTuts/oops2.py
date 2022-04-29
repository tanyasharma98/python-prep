class Employee:
    no_of_leaves = 8
    pass
tanya = Employee()
gonya = Employee()

tanya.name= "Tanya"
tanya.age =22
tanya.dep= "WorldClass"

gonya.name ="Gonya"
gonya.age=300
gonya.dep="Nalii"
print(gonya.__dict__)
print(Employee.__dict__)
print(Employee.no_of_leaves)
gonya.no_of_leaves=9
print(gonya.__dict__)
Employee.no_of_leaves=9
print(Employee.__dict__)
print(gonya.no_of_leaves)