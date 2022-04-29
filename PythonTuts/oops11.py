class A:
    classvar1 = " This is a class variable in A"
    def __init__(self):
        self.var1= "I am inside class A constructor"
        self.classvar1="Instance Var in class A"
        self.special="Special"
class B(A):
    classvar1 ="I am in class B"
    def __init__(self):
        # super().__init__()
        self.var1= "I am inside class B constructor"
        self.classvar1="Instance Var in class B"
        super().__init__() # Class A called
        print(super().classvar1)

a= A()
b=B()

print(b.classvar1) #Will search for instance first
print(b.special , b.var1 , b.classvar1)
