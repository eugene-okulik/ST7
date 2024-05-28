
class Books:
    page_material = 'paper'
    is_text = True

    def __init__(self, title, author, numb_of_pages, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.numb_of_pages = numb_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


first = Books('Inspired', 'Marty Cagan', 266, 'AA-4789')
second = Books('Hackers & Painters', 'Paul Graham', 271, 'AA-4790')
third = Books('The Clean Coder', 'Robert C. Martin', 256, 'AA-4891', True)
forth = Books('The 7 Habits of Highly Effective People', 'Stephen R Covey', 464, 'AA-4792')
fifth = Books('Empowered', 'Marty Cagan', 432, 'AA-4793')

def book_param(book):
        if book.is_reserved:
            print(f'Title : {book.title}, Author: {book.author}, Number of pages: {book.numb_of_pages}, '
                 f'Material: {book.page_material}, Reserved')
        else:
            print(f'Title : {book.title}, Author: {book.author}, Number of pages: {book.numb_of_pages}, '
                  f'Material: {book.page_material}')


book_param(first)
book_param(second)
book_param(third)
book_param(forth)
book_param(fifth)


class SchoolBooks(Books):
    def __init__(self, title, author, numb_of_pages, isbn, subject, unit, is_reserved=False):
         super().__init__(title, author, numb_of_pages, isbn, is_reserved)
         self.subject = subject
         self.unit = unit


math = SchoolBooks('Math 6 grade', 'Ruhl', 199, 'AA-98289', 'Math', 'Tornado 6', True)
lang_art = SchoolBooks('Language Arts 6 grade', 'Mark', 202, 'AA-75236', 'Language Arts', 'Riptides 6')
science = SchoolBooks('Science 6 grade', 'Logan', 218, 'AA-8723', 'Science', 'Hurricane 6')


def s_book_param(s_book):
    if s_book.is_reserved:
        print(f'Title : {s_book.title}, Author: {s_book.author}, Number of pages: {s_book.numb_of_pages}, '
              f'Subject: {s_book.subject}, Unit: {s_book.unit}, Reserved')
    else:
        print(f'Title : {s_book.title}, Author: {s_book.author}, Number of pages: {s_book.numb_of_pages}, '
              f'Subject: {s_book.subject}, Unit: {s_book.unit}')

s_book_param(math)
s_book_param(lang_art)
s_book_param(science)
