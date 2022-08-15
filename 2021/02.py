from struct import unpack
import numpy as np

inputfile = "inputs/02.txt"

dir, val = np.loadtxt(inputfile, unpack=True, dtype=str)

# Part 1
x, y = 0, 0

for i in range(len(dir)):
    if dir[i] == "forward":
        x += int(val[i])
    elif dir[i] == "down":
        y += int(val[i])
    elif dir[i] == "up":
        y -= int(val[i])

print(f"Part 1: {x * y}")

# Part 2
x, y, a = 0, 0, 0

for i in range(len(dir)):
    X = int(val[i])
    if dir[i] == "down":
        a += X
    elif dir[i] == "up":
        a -= X
    elif dir[i] == "forward":
        x += X
        y += a * X

print(f"Part 2: {x * y}")
