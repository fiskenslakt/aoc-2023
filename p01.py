import re

from aocd import data

digit_pattern = re.compile(r'([1-9]).*([1-9])')
numeral_pattern = re.compile(r'([1-9]|one|two|three|four|five|six|seven|eight|nine).*'
                                '([1-9]|one|two|three|four|five|six|seven|eight|nine)')
numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

wrong_values = []
right_values = []
for line in data.splitlines():
    if match := digit_pattern.search(line * 2):
        wrong_values.append(int(match[1] + match[2]))

    if match := numeral_pattern.search(line * 2):
        first = numbers.get(match[1], match[1])
        last = numbers.get(match[2], match[2])
        right_values.append(int(first + last))

print('Part 1:', sum(wrong_values))
print('Part 2:', sum(right_values))
