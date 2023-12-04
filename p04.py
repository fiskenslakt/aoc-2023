import re
from collections import defaultdict

from aocd import data

points = 0
cards = {}
copies = defaultdict(lambda: 1)

for card in data.splitlines():
    c, winning, have = map(str.split, re.split(r':|\|', card))
    cid = int(c[1])
    cards[cid] = len(set(winning) & set(have))

    if (won := cards[cid]) > 0:
        points += 2 ** (won - 1)

    for i in range(1, won + 1):
        copies[cid + i] += copies[cid]

print('Part 1:', points)
print('Part 2:', sum(copies[card] for card in cards))
