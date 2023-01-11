import keyboard
import time

class World:
    objects_list = []
    ui = "This is the GUI"

    def add_to_world(self, obj):
        """
        Adds an object to the World

        :param obj: The object to add
        """

        self.objects_list.append(obj)

    def remove_object_at(self, x, y):
        """
        Deletes all objects at a specific x,y coordinate

        :param x: X coordinate to remove object from
        :param y: Y coordinate to remove object from
        """

        index = 0
        while index < len(self.objects_list):
            obj = self.objects_list[index]
            if obj.x == x and obj.y == y:
                self.objects_list.pop(index)
                index = 0
            else:
                index += 1

    def get_object_at(self, x, y):
        """
        Gets an object at a specific x,y coordinate

        :param x: X coordinate to get object from
        :param y: Y coordinate to get object from
        :return: Object at position
        """
        for obj in self.objects_list:
            if obj.x == x and obj.y == y:
                return obj
        return None

    def start(self):
        """
        Start the game
        """
        while True:
            self._step()
            time.sleep(0.4)









    def _step(self):
        pressed_keys = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            if keyboard.is_pressed(letter):
                pressed_keys.append(letter)
        for obj in self.objects_list:
            obj.step(self, pressed_keys)
        self._draw()

    def _draw(self):
        # Clear the console
        line = "\n" * 20

        # Get dimensions of world:
        width = 0
        height = 0
        for obj in self.objects_list:
            if obj.x > width:
                width = obj.x
            if obj.y > height:
                height = obj.y

        # Create 2D array
        picture = []
        hh = 0
        while hh < height + 1:
            row = ['🟫'] * (width + 1)
            picture.append(row)
            hh += 1

        # Put sprites in array
        for obj in self.objects_list:
            x = obj.x
            y = obj.y
            picture[y][x] = obj.sprite

        # Print the array
        ss = ""
        for row in picture:
            for character in row:
                ss += character
            ss += "\n"
        print(line + self.ui + "\n" + ss)