"""از تابع داخلی dir() برای پیدا کردن نام هایی که یک ماژول تعریف می کند استفاده می شود. این تابع یک لیست مرتب شده از رشته ها را باز می گرداند."""
"""
dir() is a powerful inbuilt function in Python3, 
which returns list of the attributes and methods of any object 
(say functions , modules, strings, lists, dictionaries etc.)

Syntax :

dir({object})
"""

# Note that we have not imported any modules
print(dir())

# Now let's import two modules
import random
import math

# return the module names added to
# the local namespace including all
# the existing ones as before
print(dir())

# Python3 program to demonstrate working
# of dir(), when user defined objects are
# passed are parameters.

# ======================================================================================
# **************************************************************************************
# ======================================================================================

# Creation of a simple class with __dir()__
# method to demonstrate it's working
class Supermarket:

    # Function __dir()___ which list all
    # the base attributes to be used.
    def __dir__(self):
        return ['customer_name', 'product',
                'quantity', 'price', 'date']


my_cart = Supermarket()
print(dir(my_cart))