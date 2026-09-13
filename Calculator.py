def NumberCheck(number):
    try:
        testv = float(number)
        return True
    except ValueError:
        return False
def InputSystem():
    print("""
    Choose a function:
    1. +
    2. -
    3. /
    4. *
    5. 1 Percent
    6. ^
    """)
    Cmd = input("Function: ")
    if Cmd in ("1", "2", "3", "4", "6"):
        firstNum = input("First: ")
        secondNum = input("Second: ")
        while True:
            if NumberCheck(firstNum):
                firstNum = float(firstNum)
                break
            else:
                print("Not a number!")
                firstNum = input("First: ")
        while True:
            if NumberCheck(secondNum):
                secondNum = float(secondNum)
                break
            else:
                print("Not a number!")
                secondNum = input("Second: ")
        Calc(firstNum, secondNum, Cmd)
    elif Cmd == "5":
        firstNum = input("First: ")
        while True:
            if NumberCheck(firstNum):
                firstNum = float(firstNum)
                break
            else:
                print("Not a number!")
                firstNum = input("First: ")
        Calc(firstNum, None, "5")
def Calc(firstNum, secondNum, Command):
    if Command == "1":
        print(f"{firstNum} + {secondNum} = {firstNum + secondNum}")
    elif Command == "2":
        print(f"{firstNum} - {secondNum} = {firstNum - secondNum}")
    elif Command == "3":
        if secondNum == 0:
            print("Can't divide by zero!")
        else:
            print(f"{firstNum} / {secondNum} = {firstNum / secondNum}")
    elif Command == "4":
        print(f"{firstNum} * {secondNum} = {firstNum * secondNum}")
    elif Command == "5":
        print(f"{firstNum}% = {firstNum /100}")
    elif Command == "6":
        print(f"{firstNum} ^ {secondNum} = {firstNum ** secondNum}")
def Main():
    print("Initialization...")
    print("Calculator")
    print("By N1tyTheDev")
    print("Version 1.0")
    print("Initialization Complete.")
    while True:
        if input("To make new calculation please press enter. To exit type something ") == "":
            InputSystem()
        else:
            print("Goodbye!")
            break
Main()