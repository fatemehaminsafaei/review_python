# Python code for implementation of isupper()

# checking for uppercase characters
string = 'FATEMEH'
print(string.isupper())

string = 'Fatemeh'
print(string.isupper())


# Python code for implementation of isupper()

# checking for lowercase characters
string = 'fatemeh'
print(string.islower())

string = 'Fatemeh'
print(string.islower())

# Python code for implementation of lower()

# Checking for lowercase characters
string = 'FATEMH'
print(string.lower())

string = 'Fatemeh'
print(string.lower())


# Python code for implementation of upper()

# checking for uppercase characters
string = 'fatemeh'
print(string.upper())

string = 'Fatemeh aminsafaei'
print(string.upper())

# ======================================================================================
# **************************************************************************************
# ======================================================================================


string1 = "My name is Fatemeh Aminsafei"
string2 = ""
count1 = 0
count2 = 0
count3 = 0

for l in string1:
    if (l.isupper()) == True:
        count1 +=1
        string2 += (l.lower())
    elif (l.islower()) == True:
        count2 +=1
        string2 += (l.upper())
    elif (l.isspace()) == True:
        count3 += 1
        string2 += l

print("In original String : ")
print("Uppercase -", count1)
print("Lowercase -", count2)
print("Spaces -", count3)

print("After changing cases:")
print(string2)