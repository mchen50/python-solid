from abc import ABC, abstractmethod


# With this implementation in place, you can use the Shape type interchangeably
# with its Square and Rectangle subtypes when you only care about their common behavior.
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2


# This function is polymorphic because it can accept any shape type.
def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)


if __name__ == "__main__":
    get_total_area([Rectangle(10, 5), Square(5)])
