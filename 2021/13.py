import fileinput
import numpy as np

inputfile = "inputs/13.txt"

lines = [line.strip() for line in fileinput.input(inputfile)]

coords, folds = [], []
for line in lines:
    if "," in line:
        coords.append([int(i) for i in line.split(",")])
    elif line.startswith("fold along"):
        foldwhere = line.split("=")
        folds.append([int(foldwhere[1]), foldwhere[0][-1]])

ar = np.zeros((max(i[0] for i in coords) + 1, max(i[1] for i in coords) + 2))
for x, y in coords:
    ar[x, y] = 1


def fold(ar, axis):
    flip_axis = 0 if axis[1] == "x" else 1

    first_half = ar[: axis[0], :] if axis[1] == "x" else ar[:, : axis[0]]
    sec_half = ar[axis[0] + 1 :, :] if axis[1] == "x" else ar[:, axis[0] + 1 :]

    return first_half + np.flip(sec_half, flip_axis)


for n, f in enumerate(folds):
    ar = (fold(ar, f) > 0).astype(int)
    if n == 0:
        print(f"Part 1: {int(np.sum(ar))}")

print(
    f"Part 2: \n %s"
    % str(np.flipud(ar))
    .replace("0", " ")
    .replace("1", "#")
    .replace("[", "")
    .replace("]", "")
)
