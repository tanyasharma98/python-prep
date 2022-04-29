# a =input("Enter your name")
# b= input("Enter your age")
# if int(b)==0:
#     raise ZeroDivisionError("Age can't be zero")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"HEllo ,{a} ,you {b} yr old")

#==============================TYpeError============================NameError==============#######
# def addii(a,b):
#     if type(a)!= type(b):
#         raise TypeError("It can,t be add")
#     print(a+b)
#
#
# integ =int(input("Enter value"))
# sto = (input("Enter name"))
# print(f"{integ},{sto}")
# addii(integ , sto)




sa =input("ENter name")

try:
    print(a)
except Exception as e:
    if sa == "tanya":
        raise ValueError("Tanya is Boss and Not allowed")
    print("Exception raised")













