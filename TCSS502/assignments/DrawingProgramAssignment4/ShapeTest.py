from ShapeFactory import ShapeFactory
from DrawingProgram import DrawingProgram

import unittest

class ShapeTests(unittest.TestCase):
    """
    This class tests a great deal of the functionality provided by the DrawingProgram class.
    """

    def test_init_default(self):
      """
      Tests to see the default value for list_of_shapes and not specifying any parameters to the DrawingProgram constructor (__init__()).
      """
      dw = DrawingProgram()

      self.assertEqual([], dw.list_of_shapes, "default list not set to []")

    def test_init_circle(self):
      """
      Does Drawing Program set the list_of_shapes correctly when initialized with a value
      """
      sf = ShapeFactory()
      c = sf.create_shape("Circle", radius=20)
      dw = DrawingProgram([c])

      self.assertEqual([c], dw.list_of_shapes, "Drawing Program not initialized with the given list of shapes (Circle)")

    def test_get_shape(self):
      """
      Simple test to see shape getter (get_shape()) return the correct value
      """
      sf = ShapeFactory()
      c = sf.create_shape("Circle", radius=20)
      dw = DrawingProgram([c])

      self.assertEqual(dw.list_of_shapes[0], dw.get_shape(0), "shape at index 0 was not gotten")

    def test_set_shape(self):
      """
      Simple test to see shape setter (set_shape()) replaces one value with another
      Also tests the get_name() method in Shape
      """
      sf = ShapeFactory()
      c = sf.create_shape("Circle", radius=20)
      s = sf.create_shape("Square", sq_sides=15)

      dw = DrawingProgram([c])
      dw.set_shape(0, s)

      self.assertEqual("Square", dw.get_shape(0).get_name(), "first element not reset to Square from Circle")

    def test_remove_shape(self):
      """
      Simple test to see shape remover (remove_shape()) removes the shape and returns the count of shapes removed
      Also tests the get_name() method in Shape
      """
      sf = ShapeFactory()
      c = sf.create_shape("Circle", radius=20)
      s = sf.create_shape("Square", sq_sides=15)

      dw = DrawingProgram([c, s])

      self.assertEqual(1, dw.remove_shape("Circle"), "1 Circle should have been removed, did not return count 1")
      self.assertEqual(dw.list_of_shapes[0], dw.get_shape(0), "shape at index 0 was not as gotten as expected")
      self.assertEqual("Square", dw.get_shape(0).get_name(), "shape at index 0 was not Square after removing Circle")

    def test_add_shape(self):
      """
      Simple test to see shape adder (add_shape()) adds a shape
      Also tests the get_name() method in Shape
      """
      sf = ShapeFactory()
      c = sf.create_shape("Circle", radius=20)
      s = sf.create_shape("Square", sq_sides=15)

      dw = DrawingProgram()
      dw.add_shape(c)
      dw.add_shape(s)

      self.assertEqual([c, s], dw.list_of_shapes, "new shapes were not added correctly to list of shapes")

    def test_print_shape(self):

      """
      Simple test to see print_shape method excecuted
      should print shapes after calling print_shapes()
      """
      sf = ShapeFactory()
      c = sf.create_shape("Circle", radius=20)
      s = sf.create_shape("Square", sq_sides=15)

      dw = DrawingProgram()
      dw.add_shape(c)
      dw.add_shape(s)

      dw.print_shape(c)
      dw.print_shape(s)

      self.assertEqual([c, s], dw.list_of_shapes, "new shapes were not printed correctly")


    def test_sort_shapes(self):
        """
        Simple test to see if shapesorter (sort_shape()) sorts shapes
        by name and area
        """
        sf = ShapeFactory()
        c = sf.create_shape("Circle", radius=20)
        cb = sf.create_shape("Circle", radius=28)
        s = sf.create_shape("Square", sq_sides=15)

        dw = DrawingProgram()
        dw.add_shape(c)
        dw.add_shape(s)
        dw.add_shape(cb)

        dw.sort_shapes()

        self.assertEqual([c, cb, s], dw.list_of_shapes, "new shapes were not sorted correctly to list of shapes")

              #########SHAPES TESTS:############

    def test_draw_triangle(self):
        """
        Tests Draw() method of a shape. draw() also tests get_name(), perimeter() and area()
        Draw() prints name, area, perimeter
        """
        sf = ShapeFactory()
        t = sf.create_shape("Triangle", tri_side_1=10, tri_side_2=10, tri_side_3=10)
        t.draw()

        self.assertEqual('Triangle: area: 43.30127018922193, perimeter: 30', t.draw(), "Triangle was not drawn or incorrect area and perimeter")

    def test_draw_circle(self):
        """
        Tests Draw() method of a shape. draw() also tests get_name(), perimeter() and area()
        Draw() prints name, area, perimeter
        """
        sf = ShapeFactory()
        c = sf.create_shape("Circle", radius=20)
        c.draw()

        self.assertEqual('Circle: area: 1256.6370614359173, perimeter: 125.66370614359172', c.draw(), "Circle was not drawn or incorrect area and perimeter")



    def test_draw_rectangle(self):
        """
        Tests Draw() method of a shape. draw() also tests get_name(), perimeter() and area()
        Draw() prints name, area, perimeter
        """
        sf = ShapeFactory()
        r = sf.create_shape("Rectangle", rect_tb_sides=20, rect_rl_sides=10)
        r.draw()

        self.assertEqual('Rectangle: area: 200, perimeter: 60', r.draw(), "Rectangle was not drawn or incorrect area and perimeter")

    def test_draw_square(self):
        """
        Tests Draw() method of a shape. draw() also tests get_name(), perimeter() and area()
        Draw() prints name, area, perimeter
        """
        sf = ShapeFactory()
        s = sf.create_shape("Square", sq_sides=15)
        s.draw()

        self.assertEqual('Square: area: 225, perimeter: 60', s.draw(), "Square was not drawn or incorrect area and perimeter")

    def test_shape_factory(self):
        """
        Tests the shape factory's create_shape() method on each shape and adds_shape, appending it to the new list
        """

        sf = ShapeFactory()
        c = sf.create_shape("Circle")
        t = sf.create_shape("Triangle")
        r = sf.create_shape("Rectangle")
        s = sf.create_shape("Square")
        tb = sf.create_shape("Triangle")


        dw = DrawingProgram()
        dw.add_shape(c)
        dw.add_shape(tb)
        dw.add_shape(r)
        dw.add_shape(s)
        dw.add_shape(t)

        self.assertEqual([c, tb, r, s, t], dw.list_of_shapes, "shapes were not properly created! see expected vs actual")

    def test_iter(self):
        """
        Tests the iter by iterating through the list_of_shapes
        """

        sf = ShapeFactory()
        c = sf.create_shape("Circle", radius=20)
        t = sf.create_shape("Triangle", tri_side_1=10, tri_side_2=10, tri_side_3=10)
        s = sf.create_shape("Square", sq_sides=15)

        dw = DrawingProgram()
        dw.add_shape(c)
        dw.add_shape(s)
        dw.add_shape(t)

        concat_string = ""
        for shape in dw.list_of_shapes:
            concat_string += f"{shape.get_name()}, {shape.area()}, "

        self.assertEqual("Circle, 1256.6370614359173, Square, 225, Triangle, 43.30127018922193, ", concat_string, "shapes were not properly iterated through")