print("Pharmacy Stock Program!")

stock = []
print("Stock = ", stock)

def additem(item):
    stock.append(item)

def remitem(item):
    stock.remove(item)

def insitem(item,pos):
    stock.insert(pos,item)


choice = 0

print("********************************")
print("1. Add an item to stock Pharmacy.")
print("2. Remove item from stock.")
print("3. Insert item.")
print("4. Exit.")
print("********************************")

while (choice != 4):

    choice = int(input("Enter choice:"))
    if choice is 1:
        item = input("Enter item to be added:")
        additem(item)
        print(stock)

    elif choice is 2:
        item = input("Enter item to be removed:")
        remitem(item)
        print(stock)

    elif choice is 3:
        item = input("Enter item to be added:")
        pos = int(input("Enter position: "))
        insitem(item, pos)
        print(stock)
    else:
        break