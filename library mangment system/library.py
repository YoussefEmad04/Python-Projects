class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.checked_out_books = []

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def check_out(self, patron, book):
        if book.checked_out:
            print(f"{book} is checked out.")
        else:
            book.checked_out = True
            patron.checked_out_books.append(book)
            print(f"{book} checked out by {patron}.")

    def check_in(self, patron, book):
        if book in patron.checked_out_books:
            book.checked_out = False
            patron.checked_out_books.remove(book)
            print(f"{book} checked in by {patron}.")
        else:
            print(f"{book} not checked out by {patron}.")

    def list_checked_out_books(self, patron):
        checked_out_books = [str(book) for book in patron.checked_out_books]
        return checked_out_books


book1 = Book("instant", "ahmed hafez", "30201054")
book2 = Book("anythinng", "ali mohamed", "46473766")

patron1 = Patron("youssef", "1234")
patron2 = Patron("ali", "4567")

library = Library()

library.add_book(book1)
library.add_book(book2)

library.add_patron(patron1)
library.add_patron(patron2)

library.check_out(patron1, book1)
library.check_out(patron2, book2)

print(library.list_checked_out_books(patron1))
print(library.list_checked_out_books(patron2))

library.check_in(patron1, book1)
library.check_in(patron2, book2)

print(library.list_checked_out_books(patron1))
print(library.list_checked_out_books(patron2))
