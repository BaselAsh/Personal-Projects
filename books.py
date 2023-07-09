"""
- This app is the implementation of a book library
- This app was started in 7/7/2023
- This app was finished in ...
"""


# Create the book class
class Book:
    """
    - This class is to create a book object
    """
    def __init__(self, name: str, content: str, size: int, last_page: int):
        self.name = name
        self.content = content
        self.size = size
        self.last_page = last_page

    def view(self) -> str:
        """
        - This method returns the book content
        """
        return self.content





# Create the library class
class Library:
    """
    - This class create a library object that stores books from the book class
    """
    def __init__(self):
        self.serial = 0
        self.books = []

    def add_book(self, book: Book):
        """
        - This method adds a book to the library
        """
        self.books.append(book)
        self.serial += 1

    def remove_book(self, serial: int):
        """
        - This method removes a book from the library
        """
        self.books.pop(serial - 1)
        self.serial -= 1

    def view_book(self, serial: int):
        """
        - This method returns a book's content
        """
        return self.books[serial-1].view()

    def view_all(self) -> list:
        """
        - This method returns all books in the library
        """
        all_content = list()
        for book in self.books:
            all_content.append(book.view())
        return all_content




def main():
    lib = Library()
    lib.add_book(Book("greeting", "Hello, world", 12, 3))
    print(lib.view_book(1))
    print("-" * 30)
    content = lib.view_all()
    for i in content:
        print(i)
        print("=" * 50)


if __name__ == "__main__":
    main()
