class Book:
    def __init__(self, autor, page, title, text, reserved, page_count, material):
        self.autor = autor
        self.title = title
        self.page = page
        self.text = text
        self.reserved = reserved
        self.page_count = page_count
        self.material = material


class Pushkin(Book):
    def __init__(self, autor, page, title, text, reserved, page_count, material, isbn):
        super().__init__(autor, page, title, text, reserved, page_count, material)
        self.isbn = isbn


book1 = Pushkin('Пушкин', 'Есть', 'Lukomorie', 'есть', False, 343, 'Бумага', 453)
book2 = Book('Маяковский', 'Есть', 'На земле', 'есть', False, 3453, 'Бумага')
book3 = Book('Ремарк', 'Есть', 'Три товарища', 'есть', True, 66, 'Картон')
book4 = Book('Лука', 'Есть', 'Крыша', 'есть', False, 88, 'Картон')
book5 = Book('Даль', 'Есть', 'Корабль', 'нет', False, 65, 'Бумага')

for i in [book1, book2, book3, book4, book5]:
    if i.reserved:
        print(f'Название: {i.title}, Автор: {i.autor}, Страниц: {i.page_count}, материал: {i.material}'f', '
              f'Зарезервированна')
    else:
        print(f'Название: {i.title}, Автор: {i.autor}, Страниц: {i.page_count}, материал: {i.material}')


class ScolBook(Book):
    def __init__(self, autor, page, title, text, reserved, page_count, material, types, group, tasks):
        super().__init__(autor, page, title, text, reserved, page_count, material)
        self.types = types
        self.group = group
        self.tasks = tasks


textbook = ScolBook('Кулибин', 44, 'Алгебра', 'yes', False, 44, 'bumaga',
                    'Математика', ' 11A', 'tasks')
textbook2 = ScolBook('Кулибин', 55, 'История', 'yes', True, 44, 'bumaga',
                     'Физика', ' 9B', 'tasks')
textbook3 = ScolBook('Кулибин', 66, 'География', 'yes', False, 44, 'bumaga',
                     'Математика', ' 5G', 'tasks')

for i in [textbook, textbook2, textbook3]:
    if i.reserved:
        print(f'Название: {i.title}, Автор: {i.autor}, Страниц: {i.page_count}, предмет: {i.types}, класс{i.group}'f', '
              f'Зарезервированна')
    else:
        print(f'Название: {i.title}, Автор: {i.autor}, Страниц: {i.page_count}, предмет: {i.types}, класс{i.group}')
