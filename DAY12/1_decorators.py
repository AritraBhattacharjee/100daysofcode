"""
    Author : ARITRA BHATTACHARJEE
    Date : 24-02-2022(DD-MM-YYYY)
"""
# decorators are helpful in manipulating the behaviour of the class or a function. also helpful in preprocessing some stuff, that might be needed sometimes
def decors(func):
    def exec():
        print("Execution before function call")
        func()
        print("Executing after function call")
    return exec

# 1 way of implementing decorators
def say():
    print("Hello World")
say = decors(say)
say()

# 2nd way of implementing decorators

@decors
def say():
    print("Hello World")
say()

"""
    Topic learnt :
        1. Decorators

"""