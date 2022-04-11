"""
    Author : ARITRA BHATTACHARJEE
    Date : 03-03-2022(DD-MM-YYYY)
"""
#Abstract method sets a template for other functions, to which it is inherited. It must have the data members and member methods that has been declared in the abstract class, in addition to the same for their own class
# If we try to instantiate the Rectangle class without defining the printArea function, it will throw an error

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0
# We cannot create an object of an abstract base class.

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.type = "Rectangle"
        self.side = 4
        self.length = length
        self.breadth = breadth
    
    def printArea(self):
        return self.length * self.breadth

l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
rec = Rectangle(l,b)
print(f"Area of the rectangle with side {l}, {b} is {rec.printArea()}")

"""
    Topic Learnt : 
        1. Abstract Base class

"""
