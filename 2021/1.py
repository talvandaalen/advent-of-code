import numpy as np

inputfile = "inputs/1.txt"

d = list(np.loadtxt(inputfile))

# Part 1
print(f"Part 1: {len([d[i] for i in range(len(d)) if d[i] > d[i - 1]])}")

# Part 2
def getsum(i):
    return sum(d[i - 2 : i + 1])


n_larger = 0
for i in range(2, len(d)):
    tot = getsum(i)
    try:
        if getsum(i + 1) > tot:
            n_larger += 1
    except IndexError:
        break

print(f"part 2: {n_larger}")
