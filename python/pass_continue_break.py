"""
pass could be used in scenarios when you need some empty functions, classes or loops for future implementations, and there's no requirement of executing any code.
continue is used in scenarios when no when some condition has met within a loop and you need to skip the current iteration and move to the next one.
"""

x = [1, 2, 3, 4]
for i in x:
    if i == 2:
        pass  # Pass actually does nothing. It continues to execute statements below it.
        print("This statement is from pass.")
for i in x:
    if i == 2:
        continue  # Continue gets back to top of the loop.And statements below continue are executed.
        print("This statement is from continue.")
# -----------------------------------------------------------------------

x = [1, 2, 3, 4]
for i in x:
    if i == 2:
        pass  # Pass actually does nothing. It continues to execute statements below it.
    print("This statement is from pass.")
for i in x:
    if i == 2:
        continue  # Continue gets back to top of the loop.And statements below continue are executed.
    print("This statement is from continue.")

# ======================================================================================
# **************************************************************************************
# ======================================================================================

my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru']

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        break
        print('After break statement')

print('Loop is Terminated')

# ======================================================================================
# **************************************************************************************
# ======================================================================================

my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru']
i = 0

while True:
    print(my_list[i])
    if (my_list[i] == 'Guru'):
        print('Found the name Guru')
        break
        print('After break statement')
    i += 1

print('After while-loop exit')

# ======================================================================================
# **************************************************************************************
# ======================================================================================

for i in range(4):
    for j in range(4):
        if j == 2:
            break
        print("i , j : ", i, j)
