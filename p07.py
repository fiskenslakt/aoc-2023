from collections import Counter

from aocd import data

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
        return 7  # five of a kind
    elif 4 in h and 1 in h:
        return 6  # four of a kind
    elif 3 in h and 2 in h:
        return 5  # full house
    elif 3 in h and h.count(1) == 2:
        return 4  # three of a kind
    elif h.count(2) == 2 and 1 in h:
        return 3  # two pair
    elif h.count(1) == 3 and 2 in h:
        return 2  # one pair
    else:
        return 1  # high card


def normal_sort(hand):
    return hand_type(hand), [card_values[c] for c in hand]


def joker_sort(hand):
    ncard_values = card_values.copy()
    ncard_values['J'] = 1
    h = Counter(hand.replace('J', ''))
    c = h.most_common(2)
    if len(c) == 2 and c[0][1] > c[1][1]:
        fake_hand = hand.replace('J', c[0][0])
    else:
        fake_hand = hand.replace('J', max(hand, key=lambda c: ncard_values[c]))

    return hand_type(fake_hand), [ncard_values[c] for c in hand]


hands = [(line.split()[0], int(line.split()[1])) for line in data.splitlines()]

hands.sort(key=lambda h: normal_sort(h[0]))

winnings = 0
for i, (hand, bid) in enumerate(hands, 1):
    winnings += bid * i

print('Part 1:', winnings)

hands.sort(key=lambda h: joker_sort(h[0]))
winnings = 0
for i, (hand, bid) in enumerate(hands, 1):
    winnings += bid * i

print('Part 2:', winnings)
