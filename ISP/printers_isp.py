from abc import ABC, abstractmethod


# Now Printer, Fax, and Scanner are base classes that provide specific interfaces with a single responsibility each.
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


if __name__ == "__main__":
    old_printer = OldPrinter()
    old_printer.print("hello.txt")

    modern_printer = NewPrinter()
    modern_printer.print("hello.txt")
    modern_printer.fax("hello.txt")
    modern_printer.scan("hello.txt")
