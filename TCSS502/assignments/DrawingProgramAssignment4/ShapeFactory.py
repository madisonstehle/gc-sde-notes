from Circle import Circle
from Square import Square
from Triangle import Triangle
from Rectangle import Rectangle

class ShapeFactory():
  @staticmethod
  def create_shape(shape_name, radius=None, sq_sides=None, rect_tb_sides=None, rect_rl_sides=None, tri_side_1=None, tri_side_2=None, tri_side_3=None):
    try:
      if shape_name == "Circle":
        return Circle(radius)
      elif shape_name == "Square":
        return Square(sq_sides)
      elif shape_name == "Rectangle":
        return Rectangle(rect_tb_sides, rect_rl_sides)
      elif shape_name == "Triangle":
        return Triangle(tri_side_1, tri_side_2, tri_side_3)
      raise AssertionError("Shape Type is not valid")
    except AssertionError as e:
      print(e)


# c = ShapeFactory.create_shape("Circle", radius=20)
# t = ShapeFactory.create_shape("Triangle", tri_side_1=10, tri_side_2=10, tri_side_3=10)
# r = ShapeFactory.create_shape("Rectangle", rect_tb_sides=20, rect_rl_sides=10)
# s = ShapeFactory.create_shape("Square", sq_sides=15)
# # wrong = ShapeFactory.create_shape("Dodecahedron") # will print error
#
# print(c.area())
# print(t.area())
# print(r.area())
# print(s.area())