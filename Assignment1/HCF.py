num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))


def hcf(num1, num2):
    if num1 > num2:
        z = num2
    else:
        z = num1
    for i in range(1, z + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            z = i
    return z


print("HCF of both numbers is:", hcf(num1, num2))
