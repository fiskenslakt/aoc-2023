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


CYCLES = 1_000_000_000

rows = len(data.splitlines())
cols = len(data.splitlines()[0])


def get_load():
    load = 0
    for y in range(rows):
        for x in range(cols):
            if platform[(x, y)] == 'O':
                load += rows - y

    return load


def tilt_platform(cycles):
    for cycle in range(cycles or 1):
        for y in range(rows):
            for x in range(cols):
                nx, ny = x, y
                if platform[(nx, ny)] == 'O':
                    while platform.get((nx, ny-1)) == '.':
                        platform[(nx, ny-1)] = 'O'
                        platform[(nx, ny)] = '.'
                        ny -= 1

        if cycles == 0:
            break

        for x in range(cols):
            for y in range(rows):
                nx, ny = x, y
                if platform[(nx, ny)] == 'O':
                    while platform.get((nx-1, ny)) == '.':
                        platform[(nx-1, ny)] = 'O'
                        platform[(nx, ny)] = '.'
                        nx -= 1

        for y in range(rows-1, -1, -1):
            for x in range(cols):
                nx, ny = x, y
                if platform[(nx, ny)] == 'O':
                    while platform.get((nx, ny+1)) == '.':
                        platform[(nx, ny+1)] = 'O'
                        platform[(nx, ny)] = '.'
                        ny += 1

        for x in range(cols-1, -1, -1):
            for y in range(rows):
                nx, ny = x, y
                if platform[(nx, ny)] == 'O':
                    while platform.get((nx+1, ny)) == '.':
                        platform[(nx+1, ny)] = 'O'
                        platform[(nx, ny)] = '.'
                        nx += 1


platform = {}

for y, line in enumerate(data.splitlines()):
    for x, cell in enumerate(line):
        platform[(x, y)] = cell

# import pudb;pu.db
# for y, line in enumerate(data.splitlines()):
#     for x, cell in enumerate(line):
#         nx, ny = x, y
#         if cell == 'O':
#             while platform.get((nx, ny-1)) == '.':
#                 platform[(nx, ny-1)] = cell
#                 platform[(nx, ny)] = '.'
#                 ny -= 1
cycles = 0
seen = set()
from collections import defaultdict
seen = defaultdict(int)
first_cycle = None
# seen.add(hash(''.join(platform.values())))
while True:
    tilt_platform(1)
    cycles += 1
    state = hash(''.join(platform.values()))
    if state in seen and first_cycle is None:
        first_cycle = cycles
    if state in seen and seen[state] == 2:
        # print('cycle at', cycles, 'with load', get_load())
        break
    # seen.add(state)
    seen[state] += 1

configurations = sum(v == 2 for v in seen.values())
additional_cycles = (CYCLES - first_cycle) % configurations

for _ in range(additional_cycles):
    tilt_platform(1)

print(get_load())

# load = 0

# for y, line in enumerate(data.splitlines()):
#     for x, cell in enumerate(line):
#         print(platform[(x, y)], end='')
#     print()

# for y, line in enumerate(data.splitlines()):
#     for x, cell in enumerate(line):
#         if platform[(x, y)] == 'O':
#             load += rows - y

# submit(load)
# print('Part 1:', load)
# print(load)
