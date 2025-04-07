class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        return f"Reading {self.title} by {self.author}..."

    def flip_page(self):
        return "Flipping to the next page..."

# Creating an object of the Book class
book1 = Book("2020", "Brianna Wiest", 153)

print(book1.read())
print(book1.flip_page())
