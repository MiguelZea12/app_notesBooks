
class Book: 
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
        

class Member:
    def __init__ (self, names, member_id) :
        self.names = names
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_books (self, book) :
        if not book.is_checked_out:
            book.is_checked_out = True
            self.borrowed_books.append(book)
        else:
            print(f"Book : {book.title}, is already checked out.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_checkend_out = False
            self.borrowed_books.remove(book)
        

class Library :
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def list_books(self):
        for book in self.books:
            status = 'Available' if not book.is_checked_out else 'Checked out'
            print(f'{book.title} by {book.author} - {status}')
        
    def list_members (self):
        for member in self.members:
            print(f'Member: {member.name}, ID: {member.member_id}')

# Usabilidad.
library = Library()
book1 = Book('1984', 'George Orwell', '1234567890')
book2 = Book('To kill a Mockingbird', 'Harper lee', '097654321')
member1 = Member('Miguel', '001')

library.add_book(book1)
library.add_book(book2)

library.list_books()
member1.borrow_books(book1)
library.list_books()
member1.return_book(book1)
library.list_books()
