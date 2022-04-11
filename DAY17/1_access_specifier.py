"""
    Author : ARITRA BHATTACHARJEE
    Date : 01-03-2022(DD-MM-YYYY)
"""
class Student:
    no_of_subject = 8  # public variable
    _fav_subject = "Maths"  # protecteed variable
    __highestmarks = 100    # private variable
    def Private(self):
        return self.__highestmarks


Aritra = Student()
print(Aritra.no_of_subject)  # accessing public variable
print(Aritra._fav_subject)  # accessing protected variable 
# print(Aritra.__highestmarks)  # we cannot access private variable like this, because python has done a name mangling with the private variable
print(Aritra._Student__highestmarks)  # accessing private variable

print(Aritra.Private())  # another way to access private variable, by public member function of the class having a private member

# using a predefined init (constructor) function to initialise the members of another class
class Employee:
    
    def __init__(self,name,salary,):
        self.name = name
        self.salary = salary
    def printDetails(self):
        return f"Name : {self.name}, Salary : {self.salary}"

class Person(Employee):
    
    def __init__(self, name, salary,age):
        super().__init__(name, salary)
        self.age = age
    def printDetails(self):
        return f"Name : {self.name}, Salary : {self.salary}, Age : {self.age}"

Emp = Employee("Aritra",70000)
Per = Person("Aritra",80000,20)

print(Emp.printDetails())
print(Per.printDetails())


"""
    Topic Learnt:
        1. Access Specifier : Public, Protected, Private
        2. Super function
"""