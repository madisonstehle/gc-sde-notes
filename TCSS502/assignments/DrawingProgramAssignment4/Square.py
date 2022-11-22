from Shape import Shape

class Square(Shape):
  def __init__(self, length_of_side):
    self.__name = "Square"
    self.side_length = length_of_side


  def get_name(self):
    return self.__name


  def area(self):
    return self.side_length * self.side_length


  def perimeter(self):
    return self.side_length * 4


  def draw(self):
    r_string = f"{self.__name}: area: {self.area()}, perimeter: {self.perimeter()}"
    print(r_string)
    return r_string