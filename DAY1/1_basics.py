"""
    Author : ARITRA BHATTACHARJEE
    Date : 13-02-2022(DD-MM-YYYY)
"""


print("Hello World")  # printing to the console window

print("My name is")
print("Aritra Bhattacharjee") # both the lines are printed in new lines 

print("My name is",end="")
print("Aritra Bhattacharjee") #both the lines are printed in the same line

#   SINGLE LINE COMMENT

"""
    MULTI 
    LINE
    COMMENT
"""

# Escape Sequence
print("This is \tmy First\n python program.") # \t -> tab   \n-> new-line

#   More Escape Sequences : https://www.python-ds.com/python-3-escape-sequences


# Variables
var1 = "Hello"
var2 = 5
var3 = 3.14
var4 = True

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

# Type Casting
var1 = "Hello"
var2 = 39
var3 = var1 + str(var2) # var2 is typecasted to string 
print(var3)

var4 = "78"
var5 = 65
var6 = int(var4) + var5  # var4 is typecasted to integer
print(var6)



"""
    Topics Learnt: 
        1. Printing to console window
        2. Comment Lines
        3. Escape Sequence
        4. Variables
        5. Data Types
        6. Type Casting
        7. Taking User Input
"""