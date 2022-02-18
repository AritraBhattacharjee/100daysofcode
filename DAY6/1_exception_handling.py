"""
    Author : ARITRA BHATTACHARJEE
    Date : 18-02-2022(DD-MM-YYYY)
"""
# list index out of range exception : which occurs when we try to access an list index, which is beyound its range.
lst = [0,1,2,3,4]
try:
    print(lst[5])
except Exception as e:
    print(e)
print("Statement after catch block")

# Division by zero exception : which occurs when we try to divide any number by zero
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
try:
    print(a/b)
except Exception as e:
    print(e)
print("This is another statement after catch block")

# If an exception occurs in the program, then the program ends abruptly, without executing any further statements after the occurance. But Using try except(Exception Handling), we can print the occured exception in a more readable way, and it also prevents the program from abrupt termination. It also executes the statement after the occurance of exception.

"""
    Topics Learnt : 
        1. Exception Handling
"""