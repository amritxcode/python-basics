class Book:
    def __init__(self,title, author, total_copies,available_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

    def display_info(self):
        print(self.title)
        print(self.author)
        print(self.total_copies)
        print(self.available_copies)

    def borrow_copies(self):
        if self.available_copies > 0:
           self.available_copies -= 1
           print("Book Borrowed Successfully")
        else:
            print("Book Not Available")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print("Book Returned")
        else:
            print("All books are already in the library")


py_cc = Book("Python Crash Course", "Eric Matthes", 5,5)
deep_learn = Book("Deep Learning", "Ian Goodfellow", 2, 1)


py_cc.borrow_copies()
py_cc.borrow_copies()
py_cc.return_book()
print()
deep_learn.borrow_copies()
deep_learn.borrow_copies()
deep_learn.return_book()
deep_learn.return_book()