from collections import defaultdict, namedtuple

import numpy as np
from matplotlib import pyplot as plt

from day9 import IntcodeComputer


Point = namedtuple("Point", ["x", "y"])


def paint(data):
    program = IntcodeComputer(data)
    tiles = defaultdict(int)
    location = (0, 0)
    direction = 0
    tile = program.comp([1])
    turn = program.comp([])
    steps = 0
    while tile is not None:
        steps += 1
        tiles[location] = tile
        direction = (direction + (1 if turn else - 1)) % 4
        if direction&1:
            location = (location[0] + (-1 if direction&2 else 1), location[1])
        else:
            location = (location[0], location[1] + (-1 if direction&2 else 1))

        print(len(tiles))
        tile = program.comp([tiles[location]])
        turn = program.comp([])

    max_x = max(tiles, key=lambda a: a[0])[0]
    max_y = max(tiles, key=lambda a: a[1])[1]
    min_x = min(tiles, key=lambda a: a[0])[0]
    min_y = min(tiles, key=lambda a: a[1])[1]
    print(min_x, min_y, max_x, max_y)
    img = np.zeros((max_y - min_y + 1, max_x - min_x + 1),)
    for coord, color in tiles.items():
        if color:
            img[abs(coord[1]), coord[0] - min_x] = 1

    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    with open("data11.txt") as d:
        paint([int(x) for x in d.read().split(",")])