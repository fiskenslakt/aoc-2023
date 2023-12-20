import re
from collections import defaultdict

from aocd import data


class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length
        self.prev = None
        self.next = None


class Box:
    def __init__(self):
        self.lenses = {}
        self.head = None


def get_hash(s):
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value %= 256

    return value


steps = data.split(',')
step_pattern = re.compile(r'(.+)(=|-)(\d+)?')

sequence_sum = 0
boxes = defaultdict(Box)

for step in steps:
    sequence_sum += get_hash(step)

    label, operation, focal_length = step_pattern.search(step).groups()
    focal_length = int(focal_length) if focal_length else None

    box_num = get_hash(label)
    box = boxes[box_num]

    if operation == '=':
        if label in box.lenses:
            box.lenses[label].focal_length = focal_length
        else:
            lens = Lens(label, focal_length)
            box.lenses[label] = lens
            if box.head is None:
                box.head = lens
            else:
                cur_lens = box.head
                while cur_lens.next is not None:
                    cur_lens = cur_lens.next
                cur_lens.next = lens
                lens.prev = cur_lens

    elif operation == '-':
        if label not in box.lenses:
            continue
        lens = box.lenses[label]
        prev_lens = lens.prev
        next_lens = lens.next
        if prev_lens is not None:
            prev_lens.next = next_lens
        else:
            box.head = next_lens
        if next_lens is not None:
            next_lens.prev = prev_lens
        del box.lenses[label]

print('Part 1:', sequence_sum)

focusing_power = 0
for box_num, box in boxes.items():
    if box.head is not None:
        cur_lens = box.head
        slot = 1
        while cur_lens is not None:
            focusing_power += (box_num + 1) * slot * cur_lens.focal_length
            cur_lens = cur_lens.next
            slot += 1

print('Part 2:', focusing_power)
