"""
    Author : ARITRA BHATTACHARJEE
    Date : 15-02-2022(DD-MM-YYYY)
"""

# if-else are the conditional statements that helps the program to make decisions.
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
if(a>b):
    print(str(a)," is greater")
else:
    print(str(b)," is greater")

# checking type of triangle -> if-elif ladder
side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
if side1 == side2 and side2==side3 and side1 and side3 :
    print("Equilateral Triangle")
elif (side1 == side2 or side1==side3 or side2==side3):
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")


lst = [5,6,7,8,9,10,16,20,55]
key = int(input("Enter a number to search:"))
if key in lst:
    print("Present")
else:
    print("Not Present")

"""
    Topics Learnt :
        1. If - else
        2. If- elif ladder
"""