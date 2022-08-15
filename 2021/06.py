import numpy as np
from collections import Counter

inputfile = "inputs/06.txt"

fish = list(np.loadtxt(inputfile, dtype=int, delimiter=","))


def sim_num(fish, num_days):
    for _ in range(num_days):
        fish = Counter(
            {
                0: fish[1],
                1: fish[2],
                2: fish[3],
                3: fish[4],
                4: fish[5],
                5: fish[6],
                6: fish[0] + fish[7],
                7: fish[8],
                8: fish[0],
            }
        )
    return sum(fish.values())


print(f"Part 1: {sim_num(Counter(fish), 80)}")
print(f"Part 2: {sim_num(Counter(fish), 256)}")
