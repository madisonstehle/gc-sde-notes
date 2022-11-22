from Shape import Shape
import math


class Circle(Shape):
  def __init__(self, radius):
    self.__name = "Circle"
    self.radius = radius


  def get_name(self):
    return self.__name


  def area(self):
    return math.pi * (self.radius ** 2)


  def perimeter(self):
    return 2 * math.pi * self.radius


  def draw(self):
    r_string = f"{self.__name}: area: {self.area()}, perimeter: {self.perimeter()}"
    print(r_string)
    return r_string
