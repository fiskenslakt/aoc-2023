from collections import defaultdict

from aocd import data

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


def tilt_platform(quarter_cycle=False):
    for y in range(rows):
        for x in range(cols):
            nx, ny = x, y
            if platform[(nx, ny)] == 'O':
                while platform.get((nx, ny-1)) == '.':
                    platform[(nx, ny-1)] = 'O'
                    platform[(nx, ny)] = '.'
                    ny -= 1

    if quarter_cycle:
        return

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

original_state = platform.copy()

tilt_platform(quarter_cycle=True)

print('Part 1:', get_load())

platform = original_state
cycles = 0
seen = defaultdict(int)
first_cycle = None

while True:
    tilt_platform()
    cycles += 1
    state = hash(''.join(platform.values()))

    if state in seen and first_cycle is None:
        first_cycle = cycles

    if state in seen and seen[state] == 2:
        break

    seen[state] += 1

configurations = sum(v == 2 for v in seen.values())
additional_cycles = (CYCLES - first_cycle) % configurations

for _ in range(additional_cycles):
    tilt_platform()

print('Part 2:', get_load())
