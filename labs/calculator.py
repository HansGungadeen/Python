# calculator program
# creating function

def add(num1, num2):
    addition = num1 + num2
    return addition


def subtract(num1, num2):
    subtraction = num1 - num2
    return subtraction


def multiply(num1, num2):
    multiplication = num1 * num2
    return multiplication


def division(num1, num2):
    if num2 != 0:
        divide = num1 / num2
        return divide
    else:
        return 0


numOne = int(input("Insert num1 : "))
numTwo = int(input("Insert num2 : "))

sign = input("Insert the appropriate operator - + / * that you want to calculate ")

if sign == "+":
    answer = add(numOne, numTwo)
elif sign == "-":
    answer = subtract(numOne, numTwo)
elif sign == "/":
    answer = division(numOne, numTwo)
elif sign == "*":
    answer = multiply(numOne, numTwo)
else:
    print("Not valid operation.")
print(str(answer))