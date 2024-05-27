class Book:
    material = 'бумага'
    text = True

    def __init__(self, books_name, author, pages, ISBN, is_Reserved):
        self.books_name = books_name
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.is_Reserved = is_Reserved

    def print_book_info(self):
        if self.is_Reserved:
            print(f'Название: {self.books_name}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}'
                  f', Зарезервирована')
        else:
            print(f'Название: {self.books_name}, Автор: {self.author}, страниц: {self.pages},'
                  f' материал: {self.material}')


Idiot = Book('Идиот', 'Достоевский', 500, 356, is_Reserved=False)
Idiot.is_Reserved = True

Idiot2 = Book('Идиот.Часть 2', 'Достоевский', 500, 356, is_Reserved=False)

Pride_and_Prejudice = Book('Гордость и предубеждение', 'Джейн Остен', 430, 22,
                           is_Reserved=False)

The_Great_Gatsby = Book('Великий Гэтсби', 'Ф. С. Фицджеральд', 220, 408, is_Reserved=True)

Hobbit = Book('Хоббит', author='Дж. Р. Р. Толкин', pages=879, ISBN=877, is_Reserved=False)

Idiot.print_book_info()
Idiot2.print_book_info()
Pride_and_Prejudice.print_book_info()
Hobbit.print_book_info()
The_Great_Gatsby.print_book_info()
