import numpy as np
import csv

inputfile = "inputs/04.txt"

draws = list(
    int(i) for i in list(str(np.loadtxt(inputfile, max_rows=1, dtype=str)).split(","))
)
cards, matches = {}, {}

with open(inputfile) as fin:
    reader = csv.reader(fin, delimiter=" ")
    n = -1
    m = 0
    for l, row in enumerate(reader):
        if l < 1:
            continue
        if " ".join(row) == "":
            n += 1
            m = 0
            cards[n] = np.array(np.zeros((5, 5)))
            matches[n] = np.array(np.zeros((5, 5)))
            continue

        numbers = [int(i) for i in list(" ".join(row).split(" ")) if i != ""]
        cards[n][m] = numbers
        m += 1

# Part 1
def findWin(draws, cards):
    for d in draws:
        for ckey in cards.keys():
            if np.isin(d, cards[ckey]):
                matchcoords = np.where(cards[ckey] == d)
                matches[ckey][matchcoords[0], matchcoords[1]] = 1

                for f in range(5):
                    if (
                        sum(matches[ckey][f]) == 5
                        or sum(np.transpose(matches[ckey])[f]) == 5
                    ):
                        return (matches[ckey], cards[ckey], d)


winmatch, wincard, lastdraw = findWin(draws, cards)

unmarked = np.where(winmatch == 0)
sum_unmarked = 0
for x, y in zip(unmarked[0], unmarked[1]):
    sum_unmarked += wincard[x][y]

score = sum_unmarked * lastdraw
print(f"Part 1: {int(score)}")

# Part 2
def findLastWin(draws, cards):
    winningcards = []
    winningmatches = []
    winningdraws = []
    for d in draws:
        for ckey in cards.keys():
            if np.isin(d, cards[ckey]):
                matchcoords = np.where(cards[ckey] == d)
                matches[ckey][matchcoords[0], matchcoords[1]] = 1

                for f in range(5):
                    if (
                        sum(matches[ckey][f]) == 5
                        or sum(np.transpose(matches[ckey])[f]) == 5
                    ):
                        winningcards.append(cards[ckey])
                        winningmatches.append(matches[ckey])
                        winningdraws.append(d)
                        cards[ckey] = None

    return (winningmatches[-1], winningcards[-1], winningdraws[-1])


lastmatch, lastcard, lastdraw = findLastWin(draws, cards)
unmarked = np.where(lastmatch == 0)
sum_unmarked = 0
for x, y in zip(unmarked[0], unmarked[1]):
    sum_unmarked += lastcard[x][y]

score = sum_unmarked * lastdraw
print(f"Part 2: {int(sum_unmarked * lastdraw)}")
