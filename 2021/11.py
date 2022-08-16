import numpy as np
from itertools import product, count

inputfile = "inputs/11.txt"

levels = np.loadtxt(inputfile, dtype=str)
_width, _height = len(levels[0]), len(levels)
ar = np.array([[int(n) for n in level] for level in levels])
flashes = 0


def step(ar, flashes):
    ar += 1
    while (ar > 9).any():
        flashing = [(x, y) for (x, y) in zip(*np.where(ar > 9))]
        ar[ar > 9] = -1
        for pos in flashing:
            flashes += 1
            adj_cells = [
                (pos[0] + a, pos[1] + b) for a, b in product([-1, 0, 1], [-1, 0, 1])
            ]
            adj_cells.remove(pos)
            for adj in adj_cells:
                if not any(n in adj for n in [-1, _width, _height]):
                    ar[adj] += ar[adj] != -1

    ar[ar == -1] = 0
    return ar, flashes


for N in count(start=1):
    ar, flashes = step(ar, flashes)

    # Part 1
    if N == 100:
        print(f"Part 1: {flashes}")

    # Part 2
    if (ar == 0).all():
        print(f"Part 2: {N}")
        break
