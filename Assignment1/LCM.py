num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))


def lcm(num1, num2):
    if num1 > num2:
        z = num1
    else:
        z = num2

    while (1):
        if (z % num1 == 0) and (z % num2 == 0):
            break
        z += 1

    return z


print("LCM of both numbers is:", lcm(num1, num2))
