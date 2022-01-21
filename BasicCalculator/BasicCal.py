# Function defined to take inputs
def enterNum(text):
    while True:
        try:
            firstNum = float(input(f"Enter {text} number: "))
            return firstNum
        except:
            print("You did not enter a number") 
        
if __name__ == "__main__":
    firstNum = enterNum("first")
    print("first number is: ", firstNum)

    secondNum = enterNum("second")
    print("second number is: ", secondNum)

    while True:
        operation = input("Enter arithematic symbol: ")
        print("The operation you want to perform is: ", operation)

        if (operation == "+"):
            newValue = firstNum + secondNum
            break
        elif (operation == "-"):
            newValue = firstNum - secondNum
            break
        elif (operation == "*"):
            newValue = firstNum * secondNum
            break
        elif (operation == "/"):
            newValue = firstNum / secondNum
            break
        else:
            print("Not the right operation method. Enter again!!")

    print("Final value is: ", newValue)