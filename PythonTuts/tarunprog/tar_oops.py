class Employee():
    hair_color =  "black"

    pass
tarun = Employee()
harry = Employee()
tarun.name = "Tarun"
tarun.age = 21
print(f"{tarun.hair_color}  BEFORE")
tarun.hair_color = "red" #intance cannnot change class variable
print(f"{tarun.hair_color}  by calling tarun instance")
Employee.hair_color ="brown"
print(f"{Employee.hair_color}  By changing employee" )
print(tarun.__dict__)