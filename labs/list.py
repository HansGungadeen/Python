# Write a Python program that accepts a string of characters as input from the user.
# The program them remove all duplicates from the list.



#str = "hhvvnnsss"
#rem(str)

def removedub(str):
    s = set(str)
    s = "".join(s)

    print(s)


str = input("Enter String of Characters: ")
removedub(str)