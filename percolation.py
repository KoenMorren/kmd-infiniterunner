def checkPercolation(world, world_width):
    ids = [x for x in range((len(world) + 2) * world_width)]
    max = len(ids)

    for i in range(world_width):
        if i != world_width - 1:
            connect(ids, i, i + i)
        
        if world[0][i] == 'O':
            connect(ids, i, i + world_width)

    for i in range(len(world) * world_width):
        x, y = i % world_width, i // world_width

        if (world[y][x] == 'O'):
            # check right
            if (x != world_width - 1 and world[y][x + 1] == 'O'):
                connect(ids, i + world_width, i + 1 + world_width)

            # check down
            if (y != len(world) - 1 and world[y + 1][x] == 'O'):
                connect(ids, i + world_width, i + world_width + world_width)

            if y == len(world) - 1:
                connect(ids, i + world_width, i + world_width + world_width)
                
    
    for i in range(max - world_width, max - 1):
        connect(ids, i, i + 1)

    for x in range(world_width):
        for y in range(max - world_width, max - 1):
            if (isConnected(ids, x, y)):
                return True

    return False

def root(ids, i):
    while ids[i] != i:
        i = ids[i]

    return i

def connect(ids, i, j):
    rootI, rootJ = root(ids, i), root(ids, j)
    ids[rootJ] = rootI

def isConnected(ids, i, j):
    return root(ids, i) == root(ids, j)