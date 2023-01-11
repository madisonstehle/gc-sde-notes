class Wall:
    x = 0
    y = 0
    sprite = '🧱'
    name = "Wall"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self, world, keys):
        """
        Step is ran every frame of the game.

        :param world: The world object, used to call functions in the world
        :param keys: The current pressed key. Use to get input, ex: (if 'a' in keys:)
        """
        pass