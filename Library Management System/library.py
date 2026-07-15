from book import Book  
class Library:
    def __init__(self, name : str):
        self.name = name
        self.books : list[Book] = []

    def add_book(self, book : Book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book : Book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print(f"Book '{book.title}' not found in the library.")

    def search_book(self, title:str ):
        for book in self.books:
            if book.title == title:
                book.display_info()
                return
        print(f"Book '{title}' not found in the library.")

    def show_all_books(self):
        for book in self.books:
            book.display_info()

    def borrow_book(self, title:str):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title:str):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in the library.")

obj = Library("My Library")
obj.add_book(Book("Python Programming", "John Doe", 123))
obj.add_book(Book("Java Programming", "John Doe", 124))
obj.add_book(Book("JavaScript Programming", "John Doe", 125))
obj.add_book(Book("HTML and CSS", "John Doe", 126))
obj.borrow_book("Python Programming")
obj.borrow_book("Java Programming")
obj.borrow_book("JavaScript Programming")
obj.show_all_books()

