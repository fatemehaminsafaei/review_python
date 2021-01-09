"""در واقع args* و kwargs** برای تعریف کردن توابع یا متد هایی استفاده میشوند که تعداد ورودی های آن مشخص نیست.
 برای مثال فرض کنید میخواهیم تعدادی ورودی از کاربر بگیریم که نمیدانیم کاربر چه تعداد ورودی به برنامه میدهد.
 در اکثر مواقع از آرگومان های args* و kwargs** استفاده می شود،"""

"""Special Symbols Used for passing arguments:-

1.)*args (Non-Keyword Arguments)

2.)**kwargs (Keyword Arguments)
“We use *args and **kwargs as an argument when we have no doubt about the number of  arguments we should pass in a function.”
"""


def func(*args):
    for arg in args:
        print(arg)


func('fatemeh', 'hedi', 2)


# ======================================================================================
# **************************************************************************************
# ======================================================================================

def func2(arg1, *args):
    print("arg1 : ", arg1)
    for arg in args:
        print("*args : ", arg)


func2('fatemeh', 'hedi', 2)

"""2.)**kwargs

The special syntax **kwargs in function definitions in python is used to pass a keyworded,
 variable-length argument list. We use the name kwargs with the double star. 
 The reason is because the double star allows us to pass through keyword arguments (and any number of them).

 A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
 That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out."""
"""آرگومان kwargs**:

تفاوت kwargs** با args* در نوع داده ای آن است، در kwargs** داده ها به صورت دیکشنری در متغیری به نام kwargs ذخیره میشود."""


def func3(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


func3(first="Canada", second="switzerland", third="australia")

# ======================================================================================
# **************************************************************************************
# ======================================================================================

# Using *args and **kwargs in same line to call a function

def func4(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
func4("canada","greek",first="Canada", second="switzerland", third="australia")
