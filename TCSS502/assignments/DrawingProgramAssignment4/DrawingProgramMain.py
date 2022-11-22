from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory

class DrawingProgramMain():
  """
  creates a DrawingProgram, adds shapes to it. Sorts the shapes, adds some more shapes,
  replaces some shapes, sorts again. With each thing done be sure and
  include print statements to show what was done.
    -creates a drawing program
    -adds shapes to it
    -prints the shapes
    -sorts the shapes
    -prints the sorted shapes
  """

  # Create a shape factory
  sf = ShapeFactory()

  print("Creating some shapes and add them to the list...")
  c = sf.create_shape("Circle", radius=20)
  t = sf.create_shape("Triangle", tri_side_1=10, tri_side_2=10, tri_side_3=10)
  r = sf.create_shape("Rectangle", rect_tb_sides=20, rect_rl_sides=10)
  s = sf.create_shape("Square", sq_sides=15)
  tb = sf.create_shape("Triangle", tri_side_1=40, tri_side_2=40, tri_side_3=40)

  # Create a new Drawing Program
  dw = DrawingProgram()

  # Add Shapes to the Drawing Program List
  dw.add_shape(c)
  dw.add_shape(tb)
  dw.add_shape(r)
  dw.add_shape(s)
  dw.add_shape(t)

  print("==========")
  print("Initial List of Shapes: ")
  for shape in dw.list_of_shapes:
    shape.draw()

  print("==========")
  print("Printing the Triangles in the list (there should be two): ")
  dw.print_shape("Triangle")


  print("==========")
  print("Sorting the shapes...")
  dw.sort_shapes()

  print("==========")
  print("New Sorted List of Shapes: ")
  for shape in dw.list_of_shapes:
    shape.draw()

  print("==========")
  print("Get the shape at the 2nd index: ")
  dw.get_shape(2).draw()

  print("==========")
  print("Replacing the Square at the 2nd index with a Rectangle...")
  dw.set_shape(2, r)

  print("==========")
  print("Printing the new list: ")
  for shape in dw.list_of_shapes:
    shape.draw()

  print("==========")
  print("Removing the Rectangles...")
  dw.remove_shape("Rectangle")

  print("==========")
  print("Print the new list: ")
  for shape in dw.list_of_shapes:
    shape.draw()