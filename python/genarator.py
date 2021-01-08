"""
Generators in Python

Prerequisites: Yield Keyword and Iterators

There are two terms involved when we discuss generators.

Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value,
it does so with the yield keyword rather than return. If the body of a def contains yield,
the function automatically becomes a generator function."""


def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# for i in simple_generator():
# print(i)


# x = simple_generator()
# print(x.next())

# ======================================================================================
# **************************************************************************************
# ======================================================================================

def numberGenerator(n):
    number = 0
    while number < n:
        yield number
        number += 1


g = numberGenerator(3)


# print (next(g))
# print (next(g))
# print (next(g))


# ======================================================================================
# **************************************************************************************
# ======================================================================================


def numberGenerator(n):
    number = 0
    while number < n:
        yield number
        number += 1


g = numberGenerator(10)

counter = 0

while counter < 10:
    # print(next(g))
    counter += 1


# ======================================================================================
# **************************************************************************************
# ======================================================================================

# Managing Exceptions

def munber_generator(n):
    try:
        number = 0
        while number < n:
            yield number
            number += 1

    finally:
        yield n


# print (list(munber_generator(10)))


# ======================================================================================
# **************************************************************************************
# ======================================================================================

# Connecting Generators

def my_genarator(n):
    for i in range(n):
        yield i


def my_genarator2(n, m):
    for j in range(n, m):
        yield j


def my_genarator3(n, m):
    yield from my_genarator(n)
    yield from my_genarator2(n, m)
    yield from my_genarator2(n, m + 5)


print(list(my_genarator(5)))
print(list(my_genarator2(5, 10)))
print(list(my_genarator3(0, 10)))
