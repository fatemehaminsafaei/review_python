import sys


class Calculator:
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.result = 0

    def sum(self):
        self.result = self.number1 + self.number2

    def substraction(self):
        self.result = self.number1 - self.number2

    def multiplication(self):
        self.result = self.number1 * self.number2

    def divition(self):
        self.result = self.number1 / self.number2

    def power(self):
        self.result = self.number1 ** self.number2


object = Calculator()

while True:
    print("\n Calculator")
    print("\n 1.ADD \n 2.SUBSTRACTION \n 3.MULTIPLY \n 4.DIVISION \n 5.POWER \n 6.EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        object.number1 = int(input("Enter number 1: "))
        object.number2 = int(input("Enter number 2: "))
        object.sum()
        print("RESULT = ", object.result)

    elif choice == 2:
        object.number1 = int(input("Enter number 1: "))
        object.number2 = int(input("Enter number 2: "))
        object.substraction()
        print("RESULT = ", object.result)

    elif choice == 3:
        object.number1 = int(input("Enter number 1: "))
        object.number2 = int(input("Enter number 2: "))
        object.multiplication()
        print("RESULT = ", object.result)

    elif choice == 4:
        object.number1 = int(input("Enter number 1: "))
        object.number2 = int(input("Enter number 2: "))
        object.divition()
        print("RESULT = ", object.result)

    elif choice == 5:
        object.number1 = int(input("Enter number 1: "))
        object.number2 = int(input("Enter number 2: "))
        object.power()
        print("RESULT = ", object.result)

    elif choice == 6:
        print("EXIT")
        sys.exit()

    else:
        print("Invalid Choice")
