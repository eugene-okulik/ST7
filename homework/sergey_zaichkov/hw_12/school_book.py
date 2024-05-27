from book import Book


class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, subject, grade, task_availability, is_reserved=False):
        super().__init__(title, author, pages, isbn, is_reserved)
        self.subject = subject
        self.grade = grade
        self.task_availability = task_availability

    def __str__(self):
        unbooked = (f"Title: {self.title},"
                    f" Author: {self.author},"
                    f" Pages: {self.pages},"
                    f" Subject: {self.subject},"
                    f" Grade: {self.grade}")
        return unbooked if not self.reserved else unbooked + ', reserved'


sb_1 = SchoolBook(
    title='Super Math',
    author='Bobby Bob',
    pages=33,
    isbn=24524,
    subject='math',
    grade=5,
    task_availability=False)

sb_2 = SchoolBook(
    title='Mega Physic',
    author='Jimmy Jim',
    pages=40,
    isbn=2436256,
    subject='physic',
    grade=6,
    task_availability=True)

sb_3 = SchoolBook(
    title='Holy Chemistry',
    author='J.C.',
    pages=51,
    isbn=2436289,
    subject='chemistry',
    grade=8,
    task_availability=False)
sb_3.reserved = True

if __name__ == "__main__":
    print(sb_1)
    print(sb_2)
    print(sb_3)
