# The self is used to represent the instance of the class.
# With this keyword, you can access the attributes and methods of the class in python.
# It binds the attributes with the given arguments. ... In Python, we have methods that make the instance to be passed automatically,
# but not received automatically


class Programming:
    def __init__(self, languege, branch):
        self.languege = languege
        self.branch = branch

    def introduce(self):
        print("Languege is : ", self.languege)
        print("for Programming in : ", self.branch)


py = Programming("python", "Backend")
re = Programming("React", "Front")

py.introduce()
re.introduce()

# ======================================================================================
# **************************************************************************************
# ======================================================================================

