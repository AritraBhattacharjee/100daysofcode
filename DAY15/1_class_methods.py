"""
    Author : ARITRA BHATTACHARJEE
    Date : 27-02-2022(DD-MM-YYYY)
"""
class Student:
    number_of_subjects = 5
    @classmethod  # It is a decorator, that defines a  class method. It can alter the values of class members.Cls is the reference to the class. Used to access any class variable from any class or object
    def change_subject(cls,sub):
        cls.number_of_subjects = sub
    def print_sub(self):
        return self.number_of_subjects
n = int(input("Enter the new subject : "))
x = Student()
print(x.print_sub())

x.change_subject(n)

print(x.print_sub())

#class method as constructor

class Employee:
    def __init__(self,name,status,salary):
        self.name = name
        self.status = status
        self.salary = salary
    def printDetails(self):
        return f"Employee Name : {self.name}, Status : {self.status}, Salary : {self.salary}"
    @classmethod
    def constrctr(cls,string):
        return cls(*string.split("-"))
    

emp1 = Employee("Sanjeev Kumar","HR",100000)
print(emp1.printDetails())
emp2 = Employee.constrctr("Prasant Kumar-SDE2-50000")
print(emp2.printDetails())

"""
    Topic Covered : 
        1. Class Methods
        2. Class Methods as alternative constructor
"""