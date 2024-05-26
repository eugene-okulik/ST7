class Book:
    def __init__(self, page_material, availability_of_text, book_title, author, number_of_pages, isbn, is_booked):
        self.page_material = page_material
        self.availability_of_text = availability_of_text
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_booked = is_booked

    def __str__(self):
        if self.is_booked:
            return (f"Book(title={self.book_title}, author={self.author}, pages={self.number_of_pages},"
                    f" is_booked={self.is_booked})")
        else:
            return f"Book(title={self.book_title}, author={self.author}, pages={self.number_of_pages}"


book1 = Book(page_material="Paper",
             availability_of_text=True,
             book_title="The Great Gatsby",
             author="F. Scott Fitzgerald",
             number_of_pages=180,
             isbn="9780743273565",
             is_booked=False)
book2 = Book(
    page_material="Paper",
    availability_of_text=True,
    book_title="1984",
    author="George Orwell",
    number_of_pages=328,
    isbn="9780451524935",
    is_booked=False
)

book3 = Book(
    page_material="Paper",
    availability_of_text=True,
    book_title="To Kill a Mockingbird",
    author="Harper Lee",
    number_of_pages=281,
    isbn="9780060935467",
    is_booked=True
)

book4 = Book(
    page_material="Paper",
    availability_of_text=True,
    book_title="Pride and Prejudice",
    author="Jane Austen",
    number_of_pages=279,
    isbn="9780141040349",
    is_booked=False
)

book5 = Book(
    page_material="Paper",
    availability_of_text=True,
    book_title="The Catcher in the Rye",
    author="J.D. Salinger",
    number_of_pages=214,
    isbn="9780316769488",
    is_booked=True
)
print(book5)
