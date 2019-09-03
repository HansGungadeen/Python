def details(N,S,SS,DS,x):
    print("*****************")
    print("Name: ",N)
    print("Surname: ", S)
    print("From: ", SS)
    print("To: ", DS)
    print("Price: Rs ", x)
    print("*****************")

def price():
    result = 25*10*1.15
    return result
x=price()

name = input("What is your name?")
surname = input("What is your surname?")
starting = input("Enter starting point:")
destination = input("Enter destination point:")

details(name,surname,starting,destination,x)