# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Pop() method is used to return and delete the value of the key specified.
pop_ele = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('Value associated to poped key is: ' + str(pop_ele))

# The popitem() returns and removes an arbitrary element (key, value) pair from the dictionary.
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))

# All the items from a dictionary can be deleted at once by using clear() method.
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)

# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------
# Python comprehensions, like decorators,
# are syntactic sugar constructs that help build altered and filtered lists,
# dictionaries or sets from a given list, dictionary or set.
# Using comprehensions, saves a lot of time and code that might be considerably more verbose (containing more lines of code).

letter = ['a', 'b', 'c', 'd']
print(letter)
upper_letters = [x.upper() for x in letter]
print(upper_letters)

# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------

# list comprehension
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_lst = [x ** 2 for x in lst]
print(squared_lst)


# dict comprehension
squared_lst ={x: x**2 for x in lst}
print(squared_lst)


# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------

my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list if x%2 != 0]    # list comprehension
# output => [9 , 25 , 49 , 121]

squared_dict = {x:x**2 for x in my_list if x%2 != 0}    # dict comprehension
# output => {11: 121, 3: 9 , 5: 25 , 7: 49}

# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------

#Combining multiple lists into one
#Comprehensions allow for multiple iterators and hence,
# can be used to combine multiple lists into one.

a = [1, 3, 5, 7, 9]
b= [2, 4, 6, 8, 10]

rslt = [(x+y) for (x,y) in zip(a,b)]
print(rslt)


rslt = [(x,y) for x in a for y in b]
print(rslt)


# ______________________________________________________________________________________
# **************************************************************************************
# --------------------------------------------------------------------------------------

#Flattening a multi-dimensional list
#A similar approach of nested iterators (as above) can be applied to flatten a multi-dimensional list or work upon its inner elements.

my_list = [[10,20,30],[40,50,60],[70,80,90]]

flattened = [x for temp in my_list for x in temp]
print(flattened)