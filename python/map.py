"""Python map() function

map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)"""

"""تابع map در پایتون این امکان را به شما می‌دهد که یک تابع را روی تمام اعضای یک لیست اعمال کنید.

نحوه تعریف map به صورت زیر است.

Map(function , list_name)           """

def addition(n):
    return n + n

numbers = (1, 2, 3, 4, 5)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = map(lambda x : x+x, numbers)
print(list(result))


# Add two lists using map and lambda

num1 = [1 ,2, 3, 4]
num2 = [5,6, 7, 8]
result = map (lambda x,y: x + y , num1, num2)
print(list(result))



# List of strings
l = ['Amin', 'Mahzad', 'Fatemeh', 'Hedieh']
f = list(map(list, l))
print(f)