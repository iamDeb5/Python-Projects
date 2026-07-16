from book import Book
from member import Member  

class Library:
    def __init__(self, name : str):
        self.name = name
        self.books : list[Book] = []
        self.members : list[Member] = []

    def add_book(self, book : Book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print(f"Book '{book.title}' already exists in the library.")
                return
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book_id : int):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library")
                return
        print(f"Book with ID '{book_id}' not found in the library.")

    def search_book(self, book_id: int ):
        for book in self.books:
            if book.book_id == book_id:
                book.display_info()
                return book
        print(f"Book with ID '{book_id}' not found in the library.")
        return None

    def show_all_books(self):
        if not self.books:
            print("No books found in the library.")
            return
        for book in self.books:
            book.display_info()
        return


# -------------------------
    # Member Operations
    # -------------------------

    def add_member(self, member: Member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                print(f"Member '{member.name}' already exists in the library.")
                return
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully.")

    def remove_member(self, member_id: int):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member '{member.name}' removed from the library")
                return
        print(f"Member with ID '{member_id}' not found in the library.")


    def search_member(self, member_id: int):
        for member in self.members:
            if member.member_id == member_id:
                member.display_info()
                return member
        print(f"Member with ID '{member_id}' not found in the library.")
        return None
    
    def show_all_members(self):
        if not self.members:
            print("No members found in the library.")
            return
        for member in self.members:
            member.display_info()
        return


 # -------------------------
    # Borrow / Return
    # -------------------------

    def borrow_book(self, member_id: int, book_id: int):
        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
            print("Member not found !")
            return

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if book is None:
            print("Book not found !")
            return

        if book.borrow():
            member.add_borrowed_book(book)
            print(f"Book '{book.title}' borrowed successfully.")
        else:
            print(f"Book '{book.title}' is already borrowed by someone.")

    def return_book(self, member_id: int, book_id: int):
        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
            print("Member not found !")
            return

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if book is None:
            print("Book not found !")
            return

        if book in member.borrowed_books:
            if book.return_book():
                member.remove_borrowed_book(book)
                print(f"Book '{book.title}' returned successfully.")
        else:
            print(f"Book '{book.title}' is not borrowed by this member.")


        
            


