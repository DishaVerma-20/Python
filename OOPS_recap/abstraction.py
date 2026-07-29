from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete classes... compulsory hame area and perimeter bnana he pdega
class Rectangle(Shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    def area(self) -> None:
        print(self.length*self.breadth)

    def perimeter(self) -> None:
        print(2*(self.length+self.breadth))
        
r = Rectangle(5, 2)
r.area()
r.perimeter()