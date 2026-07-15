class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ID: {self.book_id}, Available: {self.is_available}")

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' borrowed successfully.")
        else:
            print(f"Book '{self.title}' is not available.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book '{self.title}' returned successfully.")
        else:
            print(f"Book '{self.title}' is already available.")

obj = Book("Python Programming", "John Doe", 123)



    

