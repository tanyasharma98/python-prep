from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        self.length = 6
        self.breath = 7
    def printarea(self):
        return self.length * self.breath
class Square(Shape):
    def __init__(self):
        self.length = 5
    # def hello(self):
    #     return "hello"
    def printarea(self):
        return self.length ** 2
rect_1 = Rectangle()
squ_1  = Square()
print(rect_1.printarea())
print(squ_1.printarea())