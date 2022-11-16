from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory

class DrawingProgramMain():
  """
  creates a DrawingProgram, adds shapes to it. Sorts the shapes, adds some more shapes,
  replaces some shapes, sorts again. With each thing done be sure and
  include print statements to show what was done.
  """
  drawing_program = DrawingProgram()

  c = ShapeFactory.create_shape("Circle", radius=20)
  t = ShapeFactory.create_shape("Triangle", tri_side_1=10, tri_side_2=10, tri_side_3=10)
  r = ShapeFactory.create_shape("Rectangle", rect_tb_sides=20, rect_rl_sides=10)
  s = ShapeFactory.create_shape("Square", sq_sides=15)

  drawing_program.add_shape(c)
  drawing_program.add_shape(t)
  drawing_program.add_shape(r)
  drawing_program.add_shape(s)
  drawing_program.add_shape(t)

  drawing_program.print_shape("Triangle")