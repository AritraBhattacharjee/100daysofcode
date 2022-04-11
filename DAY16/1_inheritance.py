"""
    Author : ARITRA BHATTACHARJEE
    Date : 28-02-2022(DD-MM-YYYY)
"""
# Single Inheritance : One Base class derived to a derived class
class A:
    def printdetails():
        print("I am from class A")
    def greet(self):
        print("Hello!")
class B(A):
    def printdetails(self):
        print("I am from class B")
    def say(self):
        print("Hola!")

b = B()
b.printdetails() # calls the function of class B. If it was absent, then it would have executed the printdetails function of class A
b.greet()   # we can access class A function using object of derived class.
b.say()

# MultiLevel Inheritance : two or more base class derived to single derived class

class X:
    def printdet(self):
        print("From Class X")


class Y:
    def printdet(self):
        print("From Class Y")



class Z(Y,X):
    def printdet(self):
        print("From Class Z")
    

obj = Z()

obj.printdet()  # Calls function from class X. Order of inheritance  is important. Control searches printdet function in class Z, then in class X and lastly in class Y

"""
    Topic Learnt : 
        1. Single Inheritance
        2. Multiple Inheritance

""" 