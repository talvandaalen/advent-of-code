import numpy as np
from itertools import permutations
import fileinput

inputfile = "inputs/08.txt"

inputs, outputs = np.loadtxt(inputfile, dtype=str, delimiter=" | ", unpack=True)

# Part 1
num_app = [
    len([dig for dig in output.split(" ") if len(dig) in [2, 3, 4, 7]])
    for output in outputs
]
print(f"Part 1: {sum(num_app)}")

# Part 2
# (Convoluted but fast way)
def translatedict(inputs):
    one = next((x for x in inputs if len(x) == 2), None)
    four = next((x for x in inputs if len(x) == 4), None)
    seven = next((x for x in inputs if len(x) == 3), None)
    eight = next((x for x in inputs if len(x) == 7), None)
    others = [x for x in inputs if x not in [one, four, seven, eight]]

    A = next((x for x in seven if x not in one), None)
    nine = next(
        (x for x in others if len(x) == 6 and all(q in x for q in (four + seven))), None
    )
    six = next(
        (
            x
            for x in others
            if len(x) == 6 and x != nine and not all(q in x for q in one)
        ),
        None,
    )
    zero = next(
        (x for x in others if len(x) == 6 and x != nine and all(q in x for q in one)),
        None,
    )
    C = next((x for x in eight if x not in six), None)
    F = next((x for x in one if x != C), None)
    E = next((x for x in eight if x not in nine), None)
    G = next((x for x in nine if x not in (four + seven)), None)
    D = next((x for x in eight if x not in zero), None)
    B = next((x for x in eight if x not in [A, C, D, E, F, G]), None)
    tdict = {A: "a", B: "b", C: "c", D: "d", E: "e", F: "f", G: "g"}

    if None in tdict.values():
        print("Translation failed!")
        return False
    else:
        return tdict


convertdict = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def translate_number(number, tdict):
    tnumber = ""
    for x in number:
        tnumber += tdict[x]
    tnumber = "".join(sorted(tnumber))
    return convertdict[tnumber]


total = 0
for n, input in enumerate(inputs):
    tdict = translatedict(input.split(" "))
    number = ""
    for output in outputs[n].split(" "):
        number += str(translate_number(output, tdict))
    total += int(number)

print(f"Part 2 (fast): {total}")

# (Simple but slow way)
def translate(word, translation):
    return "".join(sorted(word.translate(translation)))


sum_output = 0
for input, output in zip(inputs, outputs):
    scramble = permutations("abcdefg", 7)
    for s in scramble:
        translation = str.maketrans("abcdefg", "".join(s))
        translation_is_good = True

        for inp in input.split(" "):
            if translate(inp, translation) not in convertdict.keys():
                translation_is_good = False
                break
        if not translation_is_good:
            continue

        output_numbers = [
            convertdict[translate(out, translation)] for out in output.split(" ")
        ]
        sum_output += int("".join(map(str, output_numbers)))


print(f"part 2 (slow): {sum_output}")
