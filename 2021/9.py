import numpy as np
from functools import reduce
from itertools import product

inputfile = "inputs/9.txt"

lines = np.loadtxt(inputfile, dtype=str)

# pad edges with 9s
edge = [9 for x in range(len(lines[0]) + 2)]
heightmap = np.array(np.empty([len(edge), len(lines) + 2]))

heightmap[0] = edge
for n in range(len(lines)):
    heightmap[n + 1] = [9] + [int(i) for i in lines[n]] + [9]
heightmap[-1] = edge


def islowpoint(h, x, y):
    if (
        h[x][y] < h[x + 1][y]
        and h[x][y] < h[x - 1][y]
        and h[x][y] < h[x][y + 1]
        and h[x][y] < h[x][y - 1]
    ):
        return True


def getneighbors(h, x, y, visited: set, neighbors: set):
    visited.add((x, y))

    for coords in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
        if h[coords] != 9:
            neighbors.add(coords)

            if coords not in visited:
                getneighbors(h, coords[0], coords[1], visited, neighbors)

    return neighbors


sumrisk = 0
num_neighbors = []
for x, y in product(range(len(lines)), range(len(lines[0]))):
    if islowpoint(heightmap, x + 1, y + 1):

        sumrisk += 1 + heightmap[x + 1, y + 1]
        neighbors = getneighbors(heightmap, x + 1, y + 1, set(), set())
        num_neighbors.append(len(neighbors))

print(f"Part 1: {int(sumrisk)}")
print(f"Part 1: {reduce(lambda a, b: a * b, sorted(num_neighbors)[-3:])}")
