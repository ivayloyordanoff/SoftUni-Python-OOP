from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class IFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class Formatter(IFormatter):
    def format(self, book: Book) -> str:
        return book.content


class IPrinter(ABC):
    @abstractmethod
    def get_book(self, book: Book) -> str:
        pass


class Printer(IPrinter):
    def __init__(self, formatter: IFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book
