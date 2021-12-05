import random 

from percolation import checkPercolation

world = None
world_width = None
world_render = None

def generate(width, render):
    global world, world_width, world_render

    world_width = width
    world_render = render

    world = [
        [random.choice(['O', ' ']) for _ in range(width)],
        [random.choice(['O', ' ']) for _ in range(width)],
        [random.choice(['O', ' ']) for _ in range(width)],
        [random.choice(['O', ' ']) for _ in range(width)],
        [random.choice(['O']) for _ in range(width)],
    ]

    while not checkPercolation(world, world_width):
        world = [
            [random.choice(['O', ' ']) for _ in range(width)],
            [random.choice(['O', ' ']) for _ in range(width)],
            [random.choice(['O', ' ']) for _ in range(width)],
            [random.choice(['O', ' ']) for _ in range(width)],
            [random.choice(['O']) for _ in range(width)],
        ]

    return world

def addRow():
    global world

    world.insert(0, [random.choice(['O', ' ']) for _ in range(world_width)])

    # check with percolation
    while not checkPercolation(world, world_width):
        world[0] = [random.choice(['O', ' ']) for _ in range(world_width)]

    return world