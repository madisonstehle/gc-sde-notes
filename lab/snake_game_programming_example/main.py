import time
from world import World
from wall import Wall
from player import Player
from apple import Apple

def main():
    world = World()

    width = 7
    for x in range(width):
        world.add_to_world(Wall(x, 0))
        world.add_to_world(Wall(0, x))
        world.add_to_world(Wall(width - 1, x))
        world.add_to_world(Wall(x, width - 1))

    world.add_to_world(Apple(4, 3))
    world.add_to_world(Player(1, 3))

    world.start()

main()