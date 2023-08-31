from abc import ABC, abstractmethod


# This violates the ISP because it forces OldPrinter to expose an interface that
# the class doesn’t implement or need.
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")


class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


if __name__ == "__main__":
    old_printer = OldPrinter()
    old_printer.print("hello.txt")

    modern_printer = ModernPrinter()
    modern_printer.print("hello.txt")
    modern_printer.fax("hello.txt")
    modern_printer.scan("hello.txt")
