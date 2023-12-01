from aocd import data, submit

# import pudb;pu.db


# data = '''1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet'''

# data = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen'''

numbers = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

x = []
for line in data.splitlines():
    # if line == 'cbcvd9':
    #     import pudb;pu.db
    f = None
    L = None
    fn = (float('inf'), None)
    Ln = (-1, None)
    for n in numbers:
        if (idx := line.find(n)) >= 0:
            if idx < fn[0]:
                fn = (idx, n)
            if idx > Ln[0]:
                Ln = (idx, n)

    for i, c in enumerate(line):
        if c.isdigit():
            if f is None and i < fn[0]:
                f = c
            elif i > Ln[0]:
                L = c

    if f is None:
        f = str(numbers.index(fn[1]) + 1)
    if L is None and Ln[1] is not None:
        L = str(numbers.index(Ln[1]) + 1)


    if L is not None:
        x.append(int(f+L))
    else:
        x.append(int(f+f))

# print(x)
submit(sum(x))
