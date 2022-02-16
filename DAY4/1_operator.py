"""
    Author : ARITRA BHATTACHARJEE
    Date : 16-02-2022(DD-MM-YYYY)
"""

# 1. Arithmatic Operator : +,-,*,/,//,**,%
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

print(a ," + ",b," = ", a+b)
print(a ," - ",b," = ", a-b)
print(a ," * ",b," = ", a*b)
print(a ," / ",b," = ", a/b)
print(a ," // ",b," = ", a//b)  # Integer Division
print(a ," ** ",b," = ", a**b)  # Exponential : a to the power b
print(a ," % ",b," = ", a%b)    # Modulo Division : return the remainder after division

# 2. Assignment Operator : =,+=,-=,*=,/=,%=
num = int(input("Enter a number"))  # '=' is the assignment operator

# 3. Comparison Operator: ==,!=,>,>=,<,<=,

if(a>b): 
    print(a," is greater")
elif(a==b):
    print("Numbers are equal")
else:
    print(b," is greater")

# 4. Logical Operator: and , or , not

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
if side1+side2>=side3 or side2+side3>=side1 or side1+side3>=side2 :
    print("Triangle possible")
else:
    print("Triangle not possible")

# 5. Identity Operator: is, is not : Checks whether two numbers are equal or not

m = int(input("Enter a number: "))
n = int(input("Enter another number : "))
print(m is n)
print(m is not n)

# 6. Membership Operator: in, not in : Checks whether a number is present in the lst or not

lst = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Enter a number"))
if( x in lst):
    print("Present")
elif(x not in lst):
    print("Not Present")

# 7. Bitwise Operator: & , |

p = int(input("Enter a number: "))
q = int(input("Enter another number: "))
print(p ," & ",q," = ", p&q)
print(p ," | ",q," = ", p|q)

"""
    Topics Learnt : 
        1. Operators
"""
