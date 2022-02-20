"""
    Author : ARITRA BHATTACHARJEE
    Date : 19-02-2022(DD-MM-YYYY)
"""

# A Lambda Function in Python programming is an anonymous function or a function having no name. It is a small and restricted function having no more than one line. Just like a normal function, a Lambda function can have multiple arguments with one expression.

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter third number : "))

avg = lambda a,b,c:(a+b+c)/3
print("The average is: ",avg(a,b,c))

"""
    Topics Learnt : 
        1. Lambda Functions
"""
