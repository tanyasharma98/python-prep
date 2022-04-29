class Library:
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name

    def list_of_book(self):
        print(f"List of book {self.book_list}")
        return f"Books avialable at this moment {self.book_list}"

    def add_book(self, newbook):
        self.book_list.append(newbook)
        print(f"{newbook} is added in library \nUpdated list of Book {self.book_list}")
        # print(book)

    def lend_book(self, book_want):
        if book_want in self.book_list:
            print(f"Book avialable")
            self.book_list.remove(book_want)
            dict_manage.update({book_want: lb_name})

        elif book_want in dict:
            if dict_manage[book_want] == self.library_name:
                print("you already have this book")

            else:
                print("currently unavialabe")
                print(f"these book belong to {dict_manage[book_want]}")

        else:
            print("Not in library")

    def return_book(self, retn):
        dict_manage.pop(retn)
        self.book_list.append(retn)
        print(f"{retn} returned sucessfully")


if __name__ == '__main__':
    book = ["stellar", "cosmos", "tron", "bitcoin", "uniswap"]
    dict_manage = {}
    lb_name = input("Enter your name")
    user = Library(book, lb_name)
    while True:
        user_input = int(input(f"Hello {lb_name.capitalize()} \n"
                               "Press 1 :- List of book\nPress 2 :- Donate \n"
                               "Press 3 :- Lend book \npress 4 :- Return book\n"))

        if user_input == 1:
            user.list_of_book()
        elif user_input == 2:
            donate_book = input("Book name you want to add")
            user.add_book(donate_book)
        elif user_input == 3:
            want = input("Enter book name you want")
            user.lend_book(want)
        elif user_input == 4:
            re_back = input("Enter book you want to return")
            user.return_book(re_back)
        if input("Do yo want anything else").capitalize() == "Yes":
            continue
        else:
            lb_name = input("Enter your name")
            user = Library(book, lb_name)
