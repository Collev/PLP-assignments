
class Book:
    def __init__(self, title, author, pages):
        self._title = title  # Encapsulated attribute
        self._author = author
        self._pages = pages

    def read(self):
        print(f"You start reading '{self._title}' by {self._author}.")

    def book_info(self):
        return f"'{self._title}' by {self._author} - {self._pages} pages"



class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self._file_size = file_size

    def download(self):
        print(f"Downloading '{self._title}' - {self._file_size} MB.")

    def book_info(self):
        base_info = super().book_info()
        return f"{base_info}, File Size: {self._file_size} MB"


class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")



class Bird(Animal):
    def move(self):
        print("Flying")



class Fish(Animal):
    def move(self):
        print("Swimming")


# Derived class: Cat
class Cat(Animal):
    def move(self):
        print("Walking")




