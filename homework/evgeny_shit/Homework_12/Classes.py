class Book:
    material_pages = "paper"
    has_text = True

    def __init__(self, title, author, year, pagination, isbn, reserved=False):
        self.title = title
        self.author = author
        self.year = year
        self.num_of_pages = pagination
        self.isbn = isbn
        self.is_reserved = reserved

    def reserve(self):
        self.is_reserved = True

    def __str__(self):
        # ANSI escape sequences for bold text selection
        bold_start = "\033[1m"
        bold_end = "\033[0m"
        reserved_status = f"{bold_start}Reserved:{bold_end} Yes" if self.is_reserved else ""
        return (
                f"{bold_start}Book name:{bold_end} {self.title}, "
                + f"{bold_start}Author:{bold_end} {self.author}, "
                + f"{bold_start}Publishing year:{bold_end} {self.year}, "
                + f"{bold_start}Pages:{bold_end} {self.num_of_pages}, "
                + f"{bold_start}Material:{bold_end} {self.material_pages} "
                + f"{reserved_status}"
        ).strip()


class Textbook(Book):
    def __init__(self, title, author, year, pagination, isbn, subject, grade, has_exercises, reserved=False):
        super().__init__(title, author, year, pagination, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises

    def __str__(self):
        bold_start = "\033[1m"
        bold_end = "\033[0m"
        base_str = super().__str__()
        subject_str = f"{bold_start}Subject:{bold_end} {self.subject}, "
        grade_str = f"{bold_start}Grade:{bold_end} {self.grade} "
        return f"{base_str}, {subject_str}{grade_str}".strip()


book_data = [
    {"title": "Идиот", "author": "Достоевский", "year": 1869, "pagination": 500, "isbn": "978-5-699-12057-6"},
    {"title": "Война и мир", "author": "Толстой", "year": 1869, "pagination": 1225, "isbn": "978-5-17-070545-2"},
    {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "pagination": 671,
     "isbn": "978-5-17-076249-3"},
    {"title": "Анна Каренина", "author": "Толстой", "year": 1877, "pagination": 864, "isbn": "978-5-389-07489-1"},
    {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "pagination": 480, "isbn": "978-5-17-084003-0"}
]

books = [Book(**data) for data in book_data]
books[2].reserve()

for book in books:
    print(book)

print()

textbook_data = [
    {"title": "Алгебра", "author": "Иванов", "year": 2021, "pagination": 200, "isbn": "978-5-699-12057-7",
     "subject": "Математика", "grade": 9, "has_exercises": True},
    {"title": "История", "author": "Петров", "year": 2020, "pagination": 150, "isbn": "978-5-17-070545-3",
     "subject": "История", "grade": 8, "has_exercises": False},
    {"title": "География", "author": "Сидоров", "year": 2019, "pagination": 180, "isbn": "978-5-17-076249-4",
     "subject": "География", "grade": 7, "has_exercises": True},
    {"title": "Физика", "author": "Кузнецов", "year": 2022, "pagination": 220, "isbn": "978-5-389-07489-2",
     "subject": "Физика", "grade": 10, "has_exercises": True},
    {"title": "Химия", "author": "Николаев", "year": 2023, "pagination": 190, "isbn": "978-5-17-084003-1",
     "subject": "Химия", "grade": 9, "has_exercises": False}
]

textbooks = [Textbook(**data) for data in textbook_data]
textbooks[0].reserve()

for textbook in textbooks:
    print(textbook)
