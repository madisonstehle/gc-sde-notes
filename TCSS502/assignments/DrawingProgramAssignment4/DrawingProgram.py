from DrawingProgramIterator import DrawingProgramIterator

class DrawingProgram():
    def __init__(self, list_of_shapes=None):
        """
        Attributes(instance fields/data)
          - a list/collection of Shapes
          - any other data you feel is necessary for the class

        can be passed a list of Shapes or nothing at all
        """
        if list_of_shapes == None:
            self.list_of_shapes = []
        else:
            self.list_of_shapes = list_of_shapes

    def __str__(self):
        """
        returns a string representation of each of the shapes --
        each shape will be separated from others by a newline (\n)
        """
        pass

    def add_shape(self, shape):
        """
        a method that adds a Shape
        """
        self.list_of_shapes.append(shape)

    def remove_shape(self, shape):
        """
        a method that removes ALL shapes that match the one passed as a parameter --
        it should return in integer value to signify how many of that shape was removed
        """
        count_removed = 0

        # do the removal work

        return count_removed

    def print_shape(self, shape):
        """
        prints all shapes that match the type of the shape passed in
        """
        for index in range (0, len(self.list_of_shapes)):
            try:
                if shape == getattr(self.list_of_shapes[index], f"_{shape}__name"):
                    print(self.list_of_shapes[index])
            except:
                pass


    def sort_shapes(self):
        """
        sorts the list/collection of shapes -- you must use a sort that
        runs in O(nlogn) for its worst case
        shapes will be sorted first by name, then by area if names are same
        """
        # probably use merge sort here, since it is O(nlogn)
        pass

    def get_shape(self, index):
        """
        returns the shape at the specified index
        """
        return self.list_of_shapes[index]

    def set_shape(self, index, shape):
        """
        replaces the shape at the specified index
        any other behaviors you feel are necessary for the class
        """
        self.list_of_shapes.pop(index)
        self.list_of_shapes.insert(index, shape)