"""
    Author : ARITRA BHATTACHARJEE
    Date : 26-02-2022(DD-MM-YYYY)
"""

class Student:
    no_of_subject = 5  # it is a class member
    pass

x = Student()  # creating an instance of the class "Student"
y = Student()   # creating another instance of the class "Student"
x.name = "ABC"
x.age = "14"
x.no_of_subject = 8  # it is an instance of a class member. Changing it doesnot change the actual value of the class member

print(x)
print(x.__dict__)
x.std  = 9
print(x.__dict__)

print(y)

"""
    Topic Covered : 
        1. Class Members
"""
