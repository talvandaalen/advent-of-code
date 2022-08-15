import numpy as np
import statistics

inputfile = "inputs/7.txt"

crabs = np.loadtxt(inputfile, dtype=int, delimiter=",")

# Part 1
def cost_1(pos, crabs):
    return int(sum(abs(crab - pos) for crab in crabs))


print(f"part 1: {cost_1(statistics.median(crabs), crabs)}")

# Part 2
def cost_2(pos, crabs):
    return int(sum([abs(crab - pos) * (abs(crab - pos) + 1) / 2 for crab in crabs]))


print(f"part 2: {min([cost_2(pos, crabs) for pos in range(min(crabs), max(crabs))])}")
