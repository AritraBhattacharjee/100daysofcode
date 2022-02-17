"""
    Author : ARITRA BHATTACHARJEE
    Date : 17-02-2022(DD-MM-YYYY)
"""

def fact(n):
    """
        parameters : an integer n
        return : Factorial of n
        Function type : Recieving and returning
    """
    # The first comment statement in the function is called a docstring
    fact = 1
    for i in range (1,n+1):
        fact = fact*i
        
    return fact

n = int(input("Enter a number : "))
print(fact(n))
print(fact.__doc__)  # printing the docstring of the function
print(sum.__doc__)  # we can print the docstring of any function

# Other Function types : 
# 1. not recieving and not returning
def fibonacci():
    n = int(input("Enter the range : "))
    a = 0
    b = 1
    print(a," ",b," ")
    for i in range (2,n+1):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
        
fibonacci()

# 2. not recieving and returning
# 3. recieving and not returning

"""
    Topics Learnt : 
        1. Functions
"""