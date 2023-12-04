import re

from aocd import data, submit

# data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

total_p = 0
cards = {}
copies = {}

for card in data.splitlines():
    c = re.findall(r'\d+', card)
    winning = set(c[1:11])
    have = c[11:]
    # winning = set(c[1:6])
    # have = c[6:]
    # cards[c[0]] = (winning, have)
    cards[c[0]] = 0
    copies[c[0]] = 1
    p = 0

    for x in have:
        if x in winning:
            if p == 0:
                p = 1
            else:
                p *= 2

            cards[c[0]] += 1

    total_p += p

print('total_p =', total_p)

i = 1
while i < int(max(cards, key=int)):
    # winning, have = cards[str(i)]
    won = cards[str(i)]
    for copy in range(copies[str(i)]):
        j = 1
        for w in range(won):
            copies[str(i+j)] += 1
            j += 1
            if i + j > int(max(cards, key=int)):
                break
        # for x in have:
        #     if x in winning:
        #         copies[str(i+j)] += 1
        #         j += 1

    i += 1

submit(sum(copies.values()))
# print(cards)
print(sum(copies.values()))
print(copies)
