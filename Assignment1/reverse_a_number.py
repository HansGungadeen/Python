n = int(input("Enter number: "))


def reverse(n):
    rev = 0

    while (n>0):
        num = n % 10
        rev = (rev * 10) + num
        n = n // 10

    return rev


x = reverse(n)

print("Is Number = Reverse ?")

if n == x:
    print("True")
else:
    print("False")
