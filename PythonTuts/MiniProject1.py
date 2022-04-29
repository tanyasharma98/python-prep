# Library Management System
class LibraryClass:
    def __init__(self, list_of_books, library_name):
        self.diction = {}
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.__private = 123456

        for bookss in list_of_books:
            self.diction[bookss] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def add_books(self, codes, boonames):
        if boonames not in self.list_of_books:
            if codes == self.__private:
                self.list_of_books.append(boonames)
                self.diction[boonames] = None
            print("Book Added")
        else:
            print(f"It's already existed ")

    def lend_books(self, bookname, names):
        if bookname in self.list_of_books:
            if self.diction[bookname] is None:
                self.diction[bookname] = names
                print(f"{bookname} is lended to Sir/Mam {names}")
            else:
                print(f"{bookname} is already taken!!!Lend Other")
        else:
            print(f"This Book is not available Here")

    def return_books(self, hopped):
        if hopped in self.list_of_books:
            if self.diction[hopped] is not None:
                self.diction[hopped] = None
                print(f"Book returned! Successfully")
            else:
                print("It was not lended before")
        else:
            print("This book doesn't belong here")

    def delete_books(self, other):
        if other in self.list_of_books:
            self.list_of_books.remove(other)
            self.diction.pop(other)
            print("Book Deleted")


if __name__ == '__main__':
    list1 = ["NineTails", "BlackClover", "DemonSlayer", "RockLee", "DeathNote"]
    kip = input("Enter Your Libraby Name\n")
    print(f"Welcome to {kip}'s Library")
    kip = LibraryClass(list1, kip)

    i = False
    while i is not True:
        inp = int(input(f"Enter:1(Display Books)\n"
                        f"Enter:2(Add Books)\n"
                        f"Enter:3(Lend Book)\n"
                        f"Enter:4(Delete Book)\n"
                        f"Enter:5(Return Book)\n"
                        f"Enter:0(Exit)"))

        if inp == 1:
            kip.display_books()
        elif inp == 2:
            adding = input("Enter  Book Name You want to add\n")
            jig = int(input("Type Access Code"))
            kip.add_books(jig, adding)

        elif inp == 3:
            name = input("Enter Your name\n")
            book = input("Enter the name of Book\n")
            kip.lend_books(book, name)
        elif inp == 4:
            iy = int(input("Enter Excess code"))
            if iy == 123456:
                fop = input("Enter Book Name")
                kip.delete_books(fop)
        elif inp == 5:
            hop = input("Enter Book name to be returned")
            kip.return_books(hop)
        elif inp == 0:
            i = True
