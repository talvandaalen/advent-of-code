import numpy as np

inputfile = "inputs/10.txt"

lines = np.loadtxt(inputfile, dtype=str)

match_dict = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
openers = "([{<"
closers = ")]}>"

illegal_chars = ""
completion_strings = []

for line in lines:
    now_open = ""
    corrupt_line = False
    incomplete_line = False

    for count, char in enumerate(line):

        # Part 1
        if not corrupt_line:
            if char in openers:
                now_open += char

            elif char in closers:
                if now_open[-1] == match_dict[char]:
                    now_open = now_open[:-1]
                else:
                    illegal_chars += char
                    corrupt_line = True

    # Part 2
    if not corrupt_line:
        completion = ""

        for char in reversed(now_open):
            completion += match_dict[char]

        completion_strings.append(completion)

score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
print(f"Part 1: {sum([score_dict[char] for char in illegal_chars])}")


def calc_score(string):
    sc = 0
    sc_dict = {")": 1, "]": 2, "}": 3, ">": 4}
    for char in string:
        sc *= 5
        sc += sc_dict[char]
    return sc


scores = sorted([calc_score(string) for string in completion_strings])
print(f"Part 2: {scores[int(len(scores)/2)]}")
