class A:
    classvar1 = "I am class A variable"

    def __init__(self):
        self.classvar1 = "I am instance of class A"
        self.var1 = "I am vr of A"
        self.special = "Hi there"


class B(A):
    classvar1 = "I am class B variable"

    def __init__(self):
        # super().__init__()
        self.classvar1 = "I am instance of class B"
        self.var1 = "I am vr of B"
        super().__init__()
        print(super().classvar1)


a = A()
b = B()
print(b.classvar1, "b.special")
