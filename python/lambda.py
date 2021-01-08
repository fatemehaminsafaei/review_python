# Lambda is an anonymous function in Python,
# that can accept any number of arguments,
# but can only have a single expression.
# It is generally used in situations requiring an anonymous function for a short time period.

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odd_num = list(filter(lambda x: (x % 2 != 0), li))
print(odd_num)


l2 = [13, 90, 17, 59, 21, 60, 5]
Adlt = list (filter(lambda x: x>18 , l2))
print(Adlt)


names = ['fatmeh', 'hedieh', 'amin', 'mahzad']
upper_case = list(map(lambda name: str.upper(name), names))
print(upper_case)



