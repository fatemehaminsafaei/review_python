temp = 10  # global_scop variebles


def func():
    temp = 20  # Local-scop variables
    print(temp)


print(temp)
func()
print(temp)

"""----------------------------------------------------------------
****************************************************************
----------------------------------------------------------------"""

temp = 10  # global_scop variebles


def func():
    global temp
    temp = 20  # Local-scop variables
    print(temp)


print(temp)
func()
print(temp)
