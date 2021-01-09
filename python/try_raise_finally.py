"""
try:
       # Some Code....

except:
       # optional block
       # Handling of exception (if required)

else:
       # execute if no exception

finally:
      # Some code .....(always executed)
"""

"""
Let’s first understand how the try and except works –

First try clause is executed i.e. the code between try and except clause.
If there is no exception, then only try clause will run, except clause is finished.
If any exception occurred, the try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception left unhandled, then the execution stops.
A try statement can have more than one except clause
"""


# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


divide(3, 2)
divide(3, 0)


# ======================================================================================
# **************************************************************************************
# ======================================================================================

def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed')

    # Look at parameters and note the working of Program


divide(3, 2)
divide(3, 0)
