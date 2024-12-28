import time

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def checkIfInt(possibleInt):
    return possibleInt.isdigit()

def calculator():
    var1 = input("Enter first number: ")
    var2 = input("Enter second number: ")
    
    if checkIfInt(var1) and checkIfInt(var2):
        var1 = int(var1)
        var2 = int(var2)
        userInput = input("Choose operation (*, /, +, -): ")
        
        if userInput == "*":
            print("The product is:", mul(var1, var2))
        elif userInput == "/":
            print("The quotient is:", div(var1, var2))
        elif userInput == "+":
            print("The sum is:", add(var1, var2))
        elif userInput == "-":
            print("The difference is:", sub(var1, var2))
        else:
            print("Invalid operation.")
    else:
        print("Both inputs must be integers.")
        calculator()

def main():
    while True:
        calculator()
        again = input("Would you like to calculate again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()