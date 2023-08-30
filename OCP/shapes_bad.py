from math import pi

# This voilates the OCP principle because if we want to add a new shape,
# we have to modify the Shape class, which is not closed for modification.
class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2


if __name__ == "__main__":
    rectangle = Shape("rectangle", width=10, height=5)
    rectangle.calculate_area()

    circle = Shape("circle", radius=5)
    circle.calculate_area()
