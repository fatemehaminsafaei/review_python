"""
The __init__ method is similar to constructors in C++ and Java.
 Constructors are used to initialize the object’s state.
  The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
  Like methods, a constructor also contains collection of statements(i.e. instructions) that are executed at time of Object creation.
   It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object."""


class First(object):
    def __init__(self, something):
        print("First init called")
        self.something = something


class Second(First):
    def __init__(self, something):
        # Calling init of parent class
        First.__init__(self, something)
        print("Second init called")
        self.something = something


obj = Second("Something")

# ======================================================================================
# **************************************************************************************
# ======================================================================================

class Rectangle:
    def __init__(self, length, width, unit_cost =0):
        self.length = length
        self.width = width
        self.unit_cost = unit_cost

    def get_area(self):
        return self.width * self.length

    def calcilate_cost(self):
        area = self.get_area()
        return area * self.unit_cost

r = Rectangle(10 , 20 , 1000)
print(r.get_area())
print(r.calcilate_cost())