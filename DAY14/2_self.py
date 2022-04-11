"""
    Author : ARITRA BHATTACHARJEE
    Date : 26-02-2022(DD-MM-YYYY)
"""

class Student:
    no_of_subject = 5  
    
    def printDetails(self):  #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        return f"Name : {self.name}, Age : {self.age}, Number of Subjects : {self.no_of_subject}"

x = Student()  
y = Student()   
x.name = "ABC"
x.age = "14"
x.no_of_subject = 8
print(x.printDetails())

class Employee:
    def __init__(self,e_name,e_status,e_salary):
        self.empname = e_name
        self.empstatus = e_status
        self.empsalary = e_salary
    
    def printDetails(self):
        return f"Employee Name : {self.empname}, Status : {self.empstatus}, Salary : {self.empsalary}"

emp1 = Employee("Sanjeev Kumar","HR",100000)
print(emp1.printDetails())

"""
    Topics Learnt:
        1. Using of self
        2. Constructors
"""