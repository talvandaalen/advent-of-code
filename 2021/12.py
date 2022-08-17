import numpy as np

inputfile = "inputs/12.txt"
connectors = [con.split("-") for con in np.loadtxt(inputfile, dtype=str)]

all_connections = {con: [] for subcon in connectors for con in subcon}
for con in connectors:
    all_connections[con[0]] += [con[1]]
    all_connections[con[1]] += [con[0]]


def generate_paths(this_cave, visited, twice_allowed):
    if this_cave == "end":
        yield []

    for next_cave in all_connections[this_cave]:
        visited_upd = visited.copy()

        if next_cave not in visited:
            if next_cave.islower():
                visited_upd.add(next_cave)
            for path in generate_paths(next_cave, visited_upd, twice_allowed):
                yield [next_cave] + path

        elif twice_allowed and next_cave not in ["start", "end"]:
            for path in generate_paths(next_cave, visited, False):
                yield [next_cave] + path


all_paths = [c for c in generate_paths("start", {"start"}, False)]
print(f"Part 1: {len(all_paths)}")

all_paths_exp = [c for c in generate_paths("start", {"start"}, True)]
print(f"Part 2: {len(all_paths_exp)}")
