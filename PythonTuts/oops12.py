class A:
    def met(self):
        print("We are in class A")
class B(A):
    def met(self):
        print("We are in class B")
class C(A):
    def met(self):
        print("We are in class C")
class D(B,C):
    def met(self):
        print("We are in class D")


a=A()
b=B()
c=C()
d=D()


d.met()