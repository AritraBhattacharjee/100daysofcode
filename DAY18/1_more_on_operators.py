"""
    Author : ARITRA BHATTACHARJEE
    Date : 02-03-2022(DD-MM-YYYY)
"""
# https://docs.python.org/3/library/operator.html
class Family:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def printDetails(self):
        return f"Name : {self.name}, Salary : {self.salary}"
    
    def __add__(self,other):
        return self.salary + other.salary
    def __repr__(self) :
        return self.printDetails()

    def __str__(self) -> str:
        return "Calling from str"    

x = Family("Shibam",15000)
y = Family("Rohan",50000)
print(x.__add__(y))
print(x.printDetails())
print(x.__repr__())
print(x.__str__())

"""
    Topics Learnt :
        1. Mapping Operator with function
"""
