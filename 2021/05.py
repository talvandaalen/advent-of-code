import numpy as np

inputfile = "inputs/05.txt"

x1, y1, x2, y2 = np.loadtxt(inputfile, dtype=int, unpack=True, delimiter=",")
ar = np.zeros((max(x1 + x2), max(y1 + y2)))

# Part 1
for i in range(len(x1)):

    # horizontal lines
    if y1[i] == y2[i]:
        xmin, xmax = sorted([x1[i], x2[i]])
        for xit in range(xmin, xmax + 1):
            ar[xit, y1[i]] += 1

    # vertical lines
    elif x1[i] == x2[i]:
        ymin, ymax = sorted([y1[i], y2[i]])
        for yit in range(ymin, ymax + 1):
            ar[x1[i], yit] += 1

print(f"Part 2: {len(ar[ar > 1])}")

# Part 2
def direction(increasing):
    return 1 - 2 * (not increasing)


for i in range(len(x1)):
    xmin, xmax = sorted([x1[i], x2[i]])
    ymin, ymax = sorted([y1[i], y2[i]])

    inc_x = x1[i] < x2[i]
    inc_y = y1[i] < y2[i]

    # diagonal lines
    if y1[i] != y2[i] and x1[i] != x2[i]:
        for pos_x in range(x1[i], x2[i] + direction(inc_x), direction(inc_x)):
            pos_y = y1[i] + abs(x1[i] - pos_x) * direction(inc_y)
            ar[pos_x, pos_y] += 1

print(f"Part 2: {len(ar[ar > 1])}")
