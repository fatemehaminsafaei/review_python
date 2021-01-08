# Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.
# 1_ __iter(iterable)__ method that is called for the initialization of an iterator. This returns an iterator object
# 2- next ( __next__ in Python 3) The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object,
# internally it uses the iter() method to get an iterator object which further uses next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.


itarable_val = "FatemehAminsafaei"
iterablae_obj = iter(itarable_val)

while True:
    try:
        item = next(iterablae_obj)
        print(item)
    except StopIteration:
        break


# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------

# An iterable user defined type

class Iteratorstuff:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x = x + 1
        return x


for f in Iteratorstuff(16):
    print(f)

for f in Iteratorstuff(4):
    print(f)

# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------

