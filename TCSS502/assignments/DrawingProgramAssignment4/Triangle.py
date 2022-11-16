from Shape import Shape
import math


class Triangle(Shape):
    def __init__(self, side_length_1, side_length_2, side_length_3):
        self.__name = "Triangle"
        self.side_1 = side_length_1
        self.side_2 = side_length_2
        self.side_3 = side_length_3


    def area(self):
        half_perimeter = (self.side_1 + self.side_2 + self.side_3) / 2
        area_squared = half_perimeter * (half_perimeter - self.side_1) * (half_perimeter - self.side_2) * (
                    half_perimeter - self.side_3)
        return math.sqrt(area_squared)


    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


    def draw(self):
        print(f"{self.__name}: area: {self.area()}, perimeter: {self.perimeter()}")
