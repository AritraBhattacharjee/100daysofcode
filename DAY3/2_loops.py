"""
    Author : ARITRA BHATTACHARJEE
    Date : 15-02-2022(DD-MM-YYYY)
"""

# for loop
# printing the fibonacci series upto a given range
n = int(input("Enter a range : "))
a,b = 0,1
for i in range(0,n):
    print(a,end=" ")
    c = a+b
    a=b
    b=c

# Iterating through lists
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for items in lst:
    print(items,end=" ")

# Iterating through Dictionaries
dct = {"Name":"Aritra", "City":"Durgapur","Stream":"B.Tech Cse","Food":"Biriyani"}
for i in dct:
    print(i,end=" ")
print()
for x,y in dct.items():
    print(x," : ",y)

# While Loop
i = 0
while True:
    print(i,end=" ")
    
    if(i == 10):
        break   # Terminating the loop's Iteration
    elif(i == 5):
        i = i+1
        continue  # Forcing the control of the program to the next iteration, leaving the other statements below it.
    i = i+1

"""
    Topics Learnt :
        1. For loops
        2. While Loop  
"""