import math


class Shape:
    def __init__(self, name) -> None:
        self.name = name


class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return math.pi * self.radius * self.radius


rec = Rectangle("Rec", 12, 6)
print(rec.area())

cir = Circle("cir", 8)
print(cir.area())
