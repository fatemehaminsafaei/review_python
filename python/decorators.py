# Decorators provide a simple syntax for calling higher-order functions.
# By definition, a decorator is a function that takes another function
# and extends the behavior of the latter function without explicitly modifying it.
# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------
# decorator function to convert to lowercase
def lowercase_decorator(finction):
    def wrapper():
        func = finction()
        string_lowercase = func.lower()
        return string_lowercase

    return wrapper


# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------


## decorator function to split words
def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split

    return wrapper


@splitter_decorator
@lowercase_decorator
def hello():
    a = "Fatemeh Aminsafaei"
    return a


hello()


# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------
# defining a decorator
def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner1


def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()

# _________________________________________________________________________________
# *********************************************************************************
# _________________________________________________________________________________

import time
import math


def calculate_time(func):
    def innerr(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("total time taken in : ", func.__name__, end - begin)

    return innerr


@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


factorial(10)


# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------
def hello_decorator(func):
    def innerr2(*args, **kwargs):
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")
        return returned_value

    return innerr2

@hello_decorator
def sum(a, b):
    print("inside the function")
    return a + b


a, b = 1, 2
print("Sum = ", sum(a, b))
