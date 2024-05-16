#abstraction(추상화)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# rectangle, triangle

class rectangle(Shape):
    def __init__(self,highlength,hight):
        self.highlength = highlength
        self.hight = hight

    def area(self):
        return self.highlength*self.hight

class triangle(Shape):
    def __init__(self,length):
        self.highlength = highlength
        self.lowlength = lowlength

    def area(self):
        return self.highlength*self.lowlength/ 2