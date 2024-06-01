from task_1 import Book


class School_book(Book):
    def __init__(self, books_name, author, pages, ISBN, is_Reserved, subject, group, homework):
        super().__init__(books_name, author, pages, ISBN, is_Reserved)
        self.subject = subject
        self.group = group
        self.homework = homework

    def print_school_book_info(self):
        if self.is_Reserved:
            print(f'Название: {self.books_name}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, '
                  f'класс: {self.group}, Зарезервирована')
        else:
            print(f'Название: {self.books_name}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, '
                  f'класс: {self.group}')


Mathmatics = School_book('Математика', 'Лучший автор', 900, 12, False,
                         'математика', '5a', True)
Mathmatics.is_Reserved = True

English = School_book('Английский', 'Автор года', 34, 2, is_Reserved=False,
                      subject='английский', group='3d', homework=False)

Mathmatics.print_school_book_info()
English.print_school_book_info()
