import fileinput
from itertools import count
from collections import Counter

inputfile = "inputs/14.txt"

lines = [line.strip() for line in fileinput.input(inputfile)]

polymer = lines[0]
count_chars, count_pairs = Counter(), Counter()
rules = {}

# Build rules
for line in lines[2:]:
    pair, target = line.split(" -> ")
    rules[pair] = target

# Set up counters
for n in range(len(polymer) - 1):
    pair = polymer[n : n + 2]
    count_pairs[pair] += 1
    count_chars[polymer[n]] += 1
count_chars[polymer[-1]] += 1  # Last char was not reached in loop above

for step in count(start=1):

    count_next_pairs = Counter()  # To-be-updated pair counter

    for pair, quant in count_pairs.items():
        if pair in rules.keys():

            # Update char and pair counts
            count_chars[rules[pair]] += quant
            count_next_pairs[pair[0] + rules[pair]] += quant
            count_next_pairs[rules[pair] + pair[1]] += quant

    count_pairs = count_next_pairs  # Replace old with new pair counter

    if step == 10:
        print(f"Part 1: {max(count_chars.values()) - min(count_chars.values())}")

    if step == 40:
        print(f"Part 2: {max(count_chars.values()) - min(count_chars.values())}")
        break
