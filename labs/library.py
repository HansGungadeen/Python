# Write a Python program for a library, with menu:
# 1. Add a book to library (add from the last position)
# 2. Remove book from library (verify if it exists in the library)
# 3. Insert a book at specified position in the library.

library = ["HaPo"]
print("Library = ", library)

def add(book):
    library.append(book)

def remove(book):
    library.remove(book)

def insert(book,pos):
    library.insert(pos,book)

choice = 0

print("1. Add a book.")
print("2. Remove a book.")
print("3. Insert a book.")
print("4. Exit")

while (choice !=4):

    choice = int(input("Enter Choice: "))
    if choice == 1:
        book = input("Enter Book to be added: ")
        add(book)
        print(library)
    elif choice == 2:
        book = input("Enter Book to be removed: ")
        remove(book)
        print(library)
    elif choice == 3:
        book = input("Enter Book to be added: ")
        pos = int(input("Enter Position: "))
        insert(book,pos)
        print(library)
    else:
        break