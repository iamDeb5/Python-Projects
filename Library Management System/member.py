from book import Book
class Member:
    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books: list[Book] = []

    def display_info(self):
        print(f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {[book.title for book in self.borrowed_books]}")

    def add_borrowed_book(self, book: Book):
        self.borrowed_books.append(book)

    def remove_borrowed_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        else:
            return False


