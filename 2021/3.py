import numpy as np

inputfile = "inputs/3.txt"

d = list(np.loadtxt(inputfile, dtype=str))

# Part 1
eps, gam = "0b", "0b"

for i in range(len(d[0])):
    thiscolumn = [d[j][i] for j in range(len(d))]
    if thiscolumn.count("1") > len(d) // 2:
        eps += "1"
        gam += "0"
    else:
        eps += "0"
        gam += "1"

print(f"Part 1: {int(eps, 2) * int(gam, 2)}")

# Part 2
oxd, co2d = list(d), list(d)

for i in range(len(d[0])):

    thisox = [oxd[j][i] for j in range(len(oxd))]
    thisco2 = [co2d[j][i] for j in range(len(co2d))]

    if not len(thisox) == 1:
        if thisox.count("1") > thisox.count("0"):
            oxd = list(filter(lambda x: x[i:].startswith("1"), oxd))
        elif thisox.count("1") == thisox.count("0"):
            oxd = list(filter(lambda x: x[i:].startswith("1"), oxd))
        else:
            oxd = list(filter(lambda x: x[i:].startswith("0"), oxd))

    if not len(thisco2) == 1:
        if thisco2.count("1") < thisco2.count("0"):
            co2d = list(filter(lambda x: x[i:].startswith("1"), co2d))
        elif thisco2.count("1") == thisco2.count("0"):
            co2d = list(filter(lambda x: x[i:].startswith("0"), co2d))
        else:
            co2d = list(filter(lambda x: x[i:].startswith("0"), co2d))

print(f"Part 2: {int(oxd[0], 2) * int(co2d[0], 2)}")
