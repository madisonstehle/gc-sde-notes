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
        for Shape in self.list_of_shapes:
            Shape.draw()

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
        count = 0

        for Shape in self.list_of_shapes:
            if shape == Shape.get_name():
                self.list_of_shapes.remove(Shape)
                count += 1

        return count

    def print_shape(self, shape):
        """
        prints all shapes that match the type of the shape passed in
        """
        count = 0
        for Shape in self.list_of_shapes:
            if shape == Shape.get_name():
                count += 1
                Shape.draw()

    def sort_shapes(self):
        """
        sorts the list/collection of shapes -- you must use a sort that
        runs in O(nlogn) for its worst case
        shapes will be sorted first by name, then by area if names are same
        """
        # probably use merge sort here, since it is O(nlogn)
        self.merge_sort(self.list_of_shapes)


    def merge_sort(self, List):
        if len(List) > 1:  # if the list isn't empty
            left_list = List[:len(List) // 2]  # returns slice of origional array at 0, ending at end divided by 2
            right_list = List[
                         len(List) // 2:]  # starts at len of list divided by 2 goes to the end (// is floor divison**)

            # recursion time
            self.merge_sort(left_list)  # splitting left and right
            self.merge_sort(right_list)  # should do this recursively

            # time to merge!
            L = 0  # left list index
            R = 0  # right list index
            M = 0  # merged list index
            while L < len(left_list) and R < len(right_list):  # now we're just comparing and updating
                if left_list[L].get_name() == right_list[R].get_name():
                    if left_list[L].area() < right_list[R].area():
                        List[M] = left_list[L]
                        L += 1
                    else:
                        List[M] = right_list[R]
                        R += 1
                elif left_list[L].get_name() < right_list[R].get_name():
                    List[M] = left_list[L]
                    L += 1
                else:
                    List[M] = right_list[R]
                    R += 1
                M += 1  # constantly update merged list index
            while L < len(left_list):
                List[M] = left_list[L]
                L += 1
                M += 1
            while R < len(right_list):
                List[M] = right_list[R]
                R += 1
                M += 1

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