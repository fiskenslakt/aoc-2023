from aocd import data, submit

# data = '''O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....'''

ROWS = len(data.splitlines())

platform = {}

for y, line in enumerate(data.splitlines()):
    for x, cell in enumerate(line):
        platform[(x, y)] = cell

# import pudb;pu.db
for y, line in enumerate(data.splitlines()):
    for x, cell in enumerate(line):
        nx, ny = x, y
        if cell == 'O':
            while platform.get((nx, ny-1)) == '.':
                platform[(nx, ny-1)] = cell
                platform[(nx, ny)] = '.'
                ny -= 1

load = 0

# for y, line in enumerate(data.splitlines()):
#     for x, cell in enumerate(line):
#         print(platform[(x, y)], end='')
#     print()

for y, line in enumerate(data.splitlines()):
    for x, cell in enumerate(line):
        if platform[(x, y)] == 'O':
            load += ROWS - y

submit(load)
