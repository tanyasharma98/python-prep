class A:
    def hello(self):
        print("This is class A")


class B(A):
    def hello(self):
        print("This is class B")


class C(A):
    def hello(self):
        print("This is class C")


class D(B, C):
    def hello(self):
        print("This is class D")


a = A()
b = B()
c = C()
d = D()
d.hello()
a.hello()
