# Write a Python program that accepts two inputs from the user.
# The program will find the L.C.M. of two input number.

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

def lcm(num1,num2):
    if num1 > num2:
        z = num1
    else:
        z = num2

    while (1):
        if (z % num1 == 0) and (z % num2 == 0):
            break
        z +=1
    return z

print("LCM: ", lcm(num1,num2))