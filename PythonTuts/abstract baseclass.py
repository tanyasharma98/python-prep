# from abc import ABCMeta , abstractmethod
from abc import ABC , abstractmethod
# class shape(metaclass=ABCMeta):
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):
    type="Rectangle"
    sides= 4
    def __init__(self):
        self.length =4
        self.breadth =5
    def printarea(self):
        return self.length * self.breadth


rect1 =rectangle()
print(rect1.printarea())