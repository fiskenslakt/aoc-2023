import re

from aocd import data, submit

total_p = 0

for card in data.splitlines():
    c = re.findall(r'\d+', card)
    winning = set(c[1:11])
    have = c[11:]
    p = 0

    for x in have:
        if x in winning:
            if p == 0:
                p = 1
            else:
                p *= 2

    total_p += p

submit(total_p)
