class Book:
    common_material = "бумага"
    common_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        reserved_str = "зарезервирована" if self.reserved else ""
        return (f"Название: {self.title}, Автор: {self.author}, Страницы: {self.pages}, "
                f"Материал: {self.common_material} {reserved_str}").strip()


books = [
    Book("Идиот", "Достоевский", 500, "978-5-17-049145-3"),
    Book("1984", "Оруэлл", 328, "978-0-451-52493-5"),
    Book("Властелин колец", "Толкин", 1207, "978-0-395-08256-0"),
    Book("Маленький принц", "Сент-Экзюпери", 96, "978-0-15-602734-8"),
    Book("Убить пересмешника", "Ли", 324, "978-0-06-242070-1"),
]


books[0].reserved = True


for book in books:
    print(book)

print("Учебники")


class Textbook(Book):
    def __init__(self, title, author, pages, isbn, subject, school_grade, assignments, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.school_grade = school_grade
        self.assignments = assignments

    def __str__(self):
        reserved_str = "зарезервирована" if self.reserved else ""
        return (f"Название: {self.title}, Автор: {self.author}, Страницы: {self.pages}, "
                f"Предмет: {self.subject}, Класс: {self.school_grade} {reserved_str}").strip()


textbooks = [
    Textbook("Алгебра", "Иванов", 200, "978-5-17-049145-4",
             "Математика", 9, True),
    Textbook("История", "Петров", 300, "978-5-17-049145-5",
             "История", 10, False),
    Textbook("География", "Сидоров", 250, "978-5-17-049145-6",
             "География", 8, True),
    Textbook("Физика", "Кузнецов", 400, "978-5-17-049145-7",
             "Физика", 11, True),
    Textbook("Литература", "Толстой", 350, "978-5-17-049145-8",
             "Литература", 7, False),
]


textbooks[0].reserved = True


for textbook in textbooks:
    print(textbook)
