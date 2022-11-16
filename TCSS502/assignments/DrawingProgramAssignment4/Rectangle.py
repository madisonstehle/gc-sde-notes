from Shape import Shape


class Rectangle(Shape):
  def __init__(self, top_bottom_side_length, right_left_side_length):
    self.__name = "Rectangle"
    self.tb_sides = top_bottom_side_length
    self.rl_sides = right_left_side_length


  def area(self):
    return self.tb_sides * self.rl_sides


  def perimeter(self):
    return (self.rl_sides * 2) + (self.tb_sides * 2)

  def draw(self):
    print(f"{self.__name}: area: {self.area()}, perimeter: {self.perimeter()}")