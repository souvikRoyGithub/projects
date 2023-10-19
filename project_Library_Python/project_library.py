class library:
    def __init__(self,listofbooks,libraryname):
        self.listofbooks=listofbooks
        self.libraryname=libraryname
        print(f"-------Welcome to {self.libraryname}--------")
    def displaybook(self):
        print(f"{self.listofbooks}\n")
    def lendbooks(self,lbook):
        if lbook in self.listofbooks:
            self.listofbooks.remove(lbook)
            p=input("Enter your name: ")
            record_lended(p,lbook)
            modify_available_books_file()
        else:
            print("This book is not available.\n")
    def addbooks(self,abooks):
        self.listofbooks.append(abooks)
        modify_available_books_file()
        modify_Belongs_to_library_books_file()
    def returnbook(self,rbook):
        if rbook in O_lofbooks:
            self.listofbooks.append(rbook)
            r=input("Enter your name: ")
            record_returned(r,rbook)
            modify_available_books_file()
            print(f"\nThank you for returning the book named {rbook}\n")
        else:
            print("\nSorry,This book does not belong to this library.\n")

def record_lended(person,lendedbook):
    import time
    # dict1={}
    # dict1[lendedbook]=person
    with open ("lenedbooks_record.txt","a") as f:
        f.write(f"{lendedbook},{person},{str(time.asctime())}\n")

def record_returned(person,returnedbook):
    import time
    # dict2={}
    # dict2[returnedbook]=person
    with open ("returnedbooks_record.txt","a") as f:
        f.write(f"{returnedbook},{person},{str(time.asctime())}\n")

def modify_available_books_file():
    with open("Available books.txt","w") as f:
        s=",".join(svklib.listofbooks)
        f.write(s)

def modify_Belongs_to_library_books_file():
    with open("Belongs to library books.txt","w") as f:
        s1=",".join(svklib.listofbooks)
        f.write(s1)

with open("Belongs to library books.txt","r") as f:
    O_books=f.read()
O_lofbooks=O_books.split(",")
O_lofbooks

with open ("Available books.txt","r")as f:
    books=f.read()
lofbooks=books.split(",")

svklib=library(lofbooks, "Iamsvk1710library")

while True:
    try:
        n=int(input("Enter 1 to see the books available in the Library\nEnter 2 to Lend available books from the library\nEnter 3 to Add book to the library\nEnter 4 to Return book to the library\nEnter 5 to close the programme\n"))
        if n==1:
            print("Available books are: ")
            svklib.displaybook()
        elif n==2:
            print("Available books are: ")
            svklib.displaybook()
            LB=input("Enter name of the book you want to borrow: ")
            svklib.lendbooks(LB)
            print(f"\nCongratulations you have successfully borrowed the book named {LB}\n")
        elif n==3:
            AB=input("Enter name of the book you want to add to the library: ")
            svklib.addbooks(AB)
            print(f"\nThank you for donating the book named {AB}\n")
        elif n==4:
            RB=input("\nEnter name of the book you want to return to the library: ")
            svklib.returnbook(RB)
        elif n==5:
            break
        else:
            i=input("\nYou have not chose any of those options.\n")
            continue
    except ValueError as e:
        print("\nYou have not chose any of those availble options.\n")
        continue

print("Thank you for using This library.")