class Book:
    material = 'paper'
    text = True

    def __init__(self, book_title, author, scope, isbn, reserved=False):
        self.book_title = book_title
        self.author = author
        self.scope = scope
        self.isbn = isbn
        self.reserved = reserved

    def print_book(self):
        if self.reserved:
            print(f'Название: {self.book_title}, Автор: {self.author}, Страниц: {self.scope}, Материал: {self.material}'
                  f', Зарезервирована')
        else:
            print(f'Название: {self.book_title}, Автор: {self.author}, Страниц: {self.scope},'
                  f' Материал: {self.material}')


class SchoolBooks(Book):
    def __init__(self, book_title, author, scope, isbn, subject, group, homework=True, reserved=False):
        super().__init__(book_title, author, scope, isbn, reserved)
        self.subject = subject
        self.group = group
        self.homework = homework

    def print_school_book(self):
        if self.reserved:
            print(f'Название: {self.book_title}, Автор: {self.author}, Страниц: {self.scope}, '
                  f'Материал: {self.material}, Предмет: {self.subject}, Класс: {self.group}, Зарезервирована')
        else:
            print(f'Название: {self.book_title}, Автор: {self.author}, Страниц: {self.scope}, '
                  f'Материал: {self.material}, Предмет: {self.subject}, Класс: {self.group}')


book_1 = Book('Dark Matter', 'Stephen King', 450, '11-22-33', True)
book_2 = Book('Expanse', 'James Corey', 380, '12-23-44', False)
book_3 = Book('3 Body', 'Liu Cixin', 640, '13-24-44', False)
book_4 = Book('4 Body', 'iu', 530, '14-25-44', False)
book_5 = Book('5 Body', 'Miu', 950, '15-26-44', False)
school_book_1 = SchoolBooks('Math', 'Steven Clarke', 300, 2 - 30 - 4, 'mathematics', '1 A', False, True)
school_book_2 = SchoolBooks('His', 'G Smith', 400, 1 - 32 - 4, 'history', '1 B', True, False)
school_book_3 = SchoolBooks('Geo', 'Cian Burke', 500, 5 - 33 - 4, 'geography', '1 C', True, False)

book_1.print_book()
book_2.print_book()

school_book_1.print_school_book()
school_book_2.print_school_book()
