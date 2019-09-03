def add():
    result = int(num1) + int(num2)
    return result

def substract():
    result = int(num1) - int(num2)
    return result

def multiply():
    result = int(num1) * int(num2)
    return result

def divide():
    result = int(num1) / int(num2)
    return int(result)

num1= input("Enter Num1: ")
num2= input("Enter Num2: ")

w=add()
x=substract()
y=multiply()
z=divide()

print("Addition = ", w)
print("Substraction = ",x)
print("Multiplication = ",y)
print("Divide = ", z)