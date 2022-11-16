from Shape import Shape
import math


class Circle(Shape):
  def __init__(self, radius):
    self.__name = "Circle"
    self.radius = radius


  def area(self):
    return math.pi * (self.radius ** 2)


  def perimeter(self):
    return 2 * math.pi * self.radius