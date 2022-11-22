from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self, name):
        """
        name of shape
        """
        self.__name = name

    def area(self):
        """
        abstract method that will return the area of the given shape
        """
        pass

    def perimeter(self):
        """
        abstract method that will return the perimeter of the given shape
        """
        pass

    def draw(self):
        """
        prints the name of the shape followed by the area and perimeter of the shape
        formatted as follows: "name_of_shape, area: value_of_area, perimeter: value_of_perimeter"
        (e.g."Circle, area: 3.141592653589793, perimeter: 6.283185307179586")
        """
        pass