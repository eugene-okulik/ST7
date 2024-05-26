from book import Book


class SchoolBook(Book):
    def __init__(
            self,page_material, availability_of_text, book_title, author, number_of_pages, isbn, school_subject, school_class,
            is_task_available=True, is_booked=False
    ):
        super().__init__(page_material, availability_of_text,book_title, author, number_of_pages, isbn, is_booked)
        self.school_subject = school_subject
        self.school_class = school_class
        self.is_task_available = is_task_available


def __str__(self):
    if self.is_booked:
        return (f"School Book(title={self.book_title}, author={self.author}, pages={self.number_of_pages},"
                f" is_booked={self.is_booked})")
    else:
        return f"School Book(title={self.book_title}, author={self.author}, pages={self.number_of_pages}"


school_book1 = SchoolBook(
    page_material="Paper",
    availability_of_text=True,
    book_title="География материков",
    author="Сидоров",
    number_of_pages=270,
    isbn="9781122334455",
    school_subject="География",
    school_class=7,
    is_task_available=False,
    is_booked=True
)

school_book2 = SchoolBook(
    page_material="Paper",
    availability_of_text=True,
    book_title="ОБЖ",
    author="Иванов",
    number_of_pages=100,
    isbn="97819872334455",
    school_subject="Безопасность",
    school_class=7,
    is_task_available=False,
    is_booked=False
)

print(school_book2)