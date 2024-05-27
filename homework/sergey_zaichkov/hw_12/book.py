class Book:
    page_material = 'paper'
    text_presence = True

    def __init__(self, title, author, pages, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = is_reserved

    def __str__(self):
        # if self.reserved:
        unbooked = (f"Title: {self.title},"
                    f" Author: {self.author},"
                    f" Pages: {self.pages},"
                    f" Material: {self.page_material}")
        return unbooked if not self.reserved else unbooked + ', reserved'


book_1 = Book('Gore ot uma', 'Griboedov', 222, 2375627856)
book_2 = Book('The Invisible Man', 'H.G. Wells', 333, 34534)
book_3 = Book('Atlas Shrugged', 'Ayn Rand', 666, 14235)
book_2.reserved = True

if __name__ == "__main__":
    print(book_1)
    print(book_2)
    print(book_3)
