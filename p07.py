import re
from collections import Counter
# import pudb;pu.db

from aocd import data, submit

# data = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''

card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

def hand_type(hand):
    h = list(Counter(hand).values())

    if 5 in h:
        return 7  # 5oak
    elif 4 in h and 1 in h:
        return 6  # 4oak
    elif 3 in h and 2 in h:
        return 5  # fh
    elif 3 in h and h.count(1) == 2:
        return 4  # 3oak
    elif h.count(2) == 2 and 1 in h:
        return 3  # 2p
    elif h.count(1) == 3 and 2 in h:
        return 2  # 1p
    else:
        return 1  # hc


def f(hand):
    return hand_type(hand), [card_values[c] for c in hand]

hands = [(line.split()[0], int(line.split()[1])) for line in data.splitlines()]

# for hand, bid in hands:
#     print(hand, bid)

hands.sort(key=lambda h: f(h[0]))
# print()
winnings = 0
for i, (hand, bid) in enumerate(hands, 1):
    # print(i, hand, bid)
    winnings += bid * i

submit(winnings)
