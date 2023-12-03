import re

from aocd import data

grid = data.splitlines()

SCHEMATIC_WIDTH = len(grid[0])
SCHEMATIC_HEIGHT = len(grid)
NEIGHBORS = ((0,1), (1,0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1,-1), (-1, 1))

part_numbers = []
pn_coords = {}

for match in re.finditer(r'\d+', data.replace('\n', '')):
    y = match.start() // SCHEMATIC_WIDTH
    x = match.start() % SCHEMATIC_HEIGHT
    for offset in range(match.end() - match.start()):
        for i, j in NEIGHBORS:
            nx = x + i + offset
            ny = y + j

            if nx < 0 or nx > SCHEMATIC_WIDTH - 1:
                continue
            if ny < 0 or ny > SCHEMATIC_HEIGHT - 1:
                continue

            if not (cell := grid[ny][nx]).isdigit() and cell != '.':
                part_numbers.append(match)
                pn_y = match.start() // SCHEMATIC_WIDTH
                pn_x = match.start() % SCHEMATIC_HEIGHT
                for offset in range(match.end() - match.start()):
                    pn_coords[(pn_x+offset, pn_y)] = match
                break
        else:
            continue
        break

gear_ratios = []
for match in re.finditer(r'\*', data.replace('\n', '')):
    y = match.start() // SCHEMATIC_WIDTH
    x = match.start() % SCHEMATIC_HEIGHT

    adj = set()
    for i, j in NEIGHBORS:
        nx = x + i
        ny = y + j

        if (nx, ny) in pn_coords:
            adj.add(pn_coords[(nx, ny)])

    if len(adj) == 2:
        ratio = int(adj.pop()[0]) * int(adj.pop()[0])
        gear_ratios.append(ratio)

print('Part 1:', sum(map(lambda pn: int(pn[0]), part_numbers)))
print('Part 2:', sum(gear_ratios))
