"""copy in Python (Deep Copy and Shallow Copy)

In Python, Assignment statements do not copy objects, they create bindings between a target and an object.
 When we use = operator user thinks that this creates a new object; well, it doesn’t. It only creates a new variable that shares the reference of the original object.
  Sometimes a user wants to work with mutable objects, in order to do that user looks for a way to create “real copies” or “clones” of these objects.
   Or, sometimes a user wants copies that user can modify without automatically modifying the original at the same time, in order to do that we create copies of objects.

A copy is sometimes needed so one can change one copy without changing the other.
In Python, there are two ways to create copies :

Deep copy
Shallow copy"""

# Shallow copy
a = [1, 2, 3, 4, 5]
b = a

print(id(a))
print(id(b))

b[1] = 30
print(a)
print(b)

# ======================================================================================
# **************************************************************************************
# ======================================================================================


# Deep copy
import copy

a = [1, 2, 3, 4]
b = [5, 6]
c = a + b
d = copy.copy(c)
print(id(c))
print(id(d))
c[0] = 12
c[1] = 12
print("c = ", c)
print("d = ", d)

# ======================================================================================
# **************************************************************************************
# ======================================================================================

# Deep copy

import copy

a = [1, 2, 3, 4]
b = [5, 6]
c = a + b
d = copy.deepcopy(c)
print(id(c))
print(id(d))
c[0] = 12
c[1] = 12
print("c = ", c)
print("d = ", d)

# ======================================================================================
# **************************************************************************************
# ======================================================================================

import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# original elements of list
print("The original elements before shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# checking if change is reflected
print("The original elements after shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")
