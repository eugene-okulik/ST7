class Book:
    page_material = "paper"
    text_availability = True
    school_subject = ''

    def __init__(self, book_title, author, number_of_pages, isbn, is_reserved=False):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


class SchoolBook(Book):
    def __init__(
            self, book_title, author, number_of_pages, isbn, school_subject, school_class,
            homework_availability=True, is_reserved=False
    ):
        super().__init__(book_title, author, number_of_pages, isbn, is_reserved)
        self.school_subject = school_subject
        self.school_class = school_class
        self.homework_availability = homework_availability


def print_book_details(name):
    print(f'Название: {name.book_title}, Автор: {name.author}, страниц: {name.number_of_pages}', end='')
    if name.school_subject:
        print(f', предмет: {name.school_subject}, класс: {name.school_class}', end='')
    else:
        print(',  материал: бумага', end='')
    if name.is_reserved:
        print(', зарезервирована', end='')
    print()


book_1 = Book('Идиот', 'Достоевский', 500, '2-266-11156-6 ', True)
book_2 = Book('Мастер и Маргарита', 'Булгаков', 666, '2-666-11156-6 ')
book_3 = Book('Война и Мир. Том 1', 'Толстой', 999999, '1-266-78156-6 ')
book_4 = Book('Сборник стихов', 'Лермонтов', 499, '2-276-11156-6 ')
book_5 = Book('Пикник на обочине', 'Стругацкие', 501, '2-266-11246-6 ')
book_6 = SchoolBook(
    'Информатика для старших классов', 'Кнутт', 256, '2-266-11056-6 ', 'Информатика', 10, True
)
book_7 = SchoolBook(
    'История средних веков', 'Иванова', 93, '2-266-11856-6 ', 'История', 7, False, True
)
book_8 = SchoolBook(
    'Алгебра', 'Иванов', 200, '2-266-12856-6 ', 'Математика', 9, True
)

print_book_details(book_1)
print_book_details(book_2)
print_book_details(book_3)
print_book_details(book_4)
print_book_details(book_5)
print_book_details(book_6)
print_book_details(book_7)
print_book_details(book_8)
