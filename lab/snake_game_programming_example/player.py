import random
from snake_piece import Snake_Piece

class Player:
    x = 0
    y = 0
    sprite = '🐌'
    name = "Player"
    alive = True
    direction = "right"
    snake_piece_list = []

    points = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self, world, keys):
        """
        Step is ran every frame of the game.

        :param world: The world object, used to call functions in the world
        :param keys: The current pressed key. Use to get input, ex: (if 'a' in keys:)
        """

        x_change = 0
        y_change = 0

        if self.alive:

            if 'a' in keys and self.direction != "right":
                self.direction = "left"
            if 'd' in keys and self.direction != "left":
                self.direction = "right"
            if 'w' in keys and self.direction != "down":
                self.direction = "up"
            if 's' in keys and self.direction != "up":
                self.direction = "down"

            if self.direction == "up":
                y_change = -1
            elif self.direction == "down":
                y_change = 1
            elif self.direction == "right":
                x_change = 1
            elif self.direction == "left":
                x_change = -1

            next_x = self.x
            next_y = self.y
            for piece in self.snake_piece_list:
                temp_x = piece.x
                temp_y = piece.y

                piece.x = next_x
                piece.y = next_y

                next_x = temp_x
                next_y = temp_y

            if x_change != 0 or y_change != 0:
                obj = world.get_object_at(self.x + x_change, self.y + y_change)
                if obj is None:
                    self.x += x_change
                    self.y += y_change
                elif obj.name != "Wall":

                    if obj.name == "Apple":
                        self.points += 1

                        # Do stuff
                        obj.x = random.randint(1, 5)
                        obj.y = random.randint(1, 5)
                        world.ui = "Points: " + str(self.points)

                        new_piece = Snake_Piece(self.x, self.y)
                        world.add_to_world(new_piece)
                        self.snake_piece_list.append(new_piece)
                        pass

                    self.x += x_change
                    self.y += y_change

                elif obj.name == "Wall":
                    self.alive = False
                    self.sprite = "💀"
                    made_skull = False
                    for piece in self.snake_piece_list:
                        piece.sprite = "🟥"
                        if not made_skull:
                            piece.sprite = "💀"
                            made_skull = True
        pass
