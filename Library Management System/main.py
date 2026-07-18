from book import Book
from library import Library
from member import Member

library = Library("HyperX Library")
library.load_books()
library.load_members()

'''
# Create Books
book1 = Book("Python Programming", "John Doe", 123)
book2 = Book("Java Programming", "John Doe", 124)
book3 = Book("C++ Programming", "John Doe", 125)

# Add Books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create Members
member1 = Member("John Marston", 1)
member2 = Member("Jane Foster", 2)

# Register Members
library.add_member(member1)
library.add_member(member2)
'''


while True:
    print("\nLibrary Management System Menu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Show All Books")
    print("5. Add Member")
    print("6. Remove Member")
    print("7. Search Member")
    print("8. Show All Members")
    print("9. Borrow Book")
    print("10. Return Book")
    print("11. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book_id = int(input("Enter book ID: "))
        library.add_book(Book(title, author, book_id))
    elif choice == "2":
        book_id = int(input("Enter book ID: "))
        library.remove_book(book_id)
    elif choice == "3":
        book_id = int(input("Enter book ID: "))
        library.search_book(book_id)
    elif choice == "4":
        library.show_all_books()
    elif choice == "5":
        name = input("Enter member name: ")
        member_id = int(input("Enter member ID: "))
        library.add_member(Member(name, member_id))
    elif choice == "6":
        member_id = int(input("Enter member ID: "))
        library.remove_member(member_id)
    elif choice == "7":
        member_id = int(input("Enter member ID: "))
        library.search_member(member_id)
    elif choice == "8":
        library.show_all_members()
    elif choice == "9":
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        library.borrow_book(member_id, book_id)
    elif choice == "10":
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        library.return_book(member_id, book_id)
    elif choice == "11":
        library.save_books()
        library.save_members()
        print("Data saved successfully!")
        print("Exiting Library Management System. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")



    