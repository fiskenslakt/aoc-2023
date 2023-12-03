import re

from aocd import data, submit

# data = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''

# import pudb;pu.db
neighbors = ((0,1), (1,0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1,-1), (-1, 1))
part_numbers = []
grid = data.splitlines()
schematic_width = len(grid[0])
schematic_height = len(grid)
for m in re.finditer('\d+', data.replace('\n', '')):
    # if m[0] == '633':
    #     import pudb;pu.db
    y = m.start() // schematic_width
    x = m.start() % schematic_width
    for offset in range(m.end() - m.start()):
        for i, j in neighbors:
            nx = x + i + offset
            ny = y + j

            if nx < 0 or nx > schematic_width - 1:
                continue
            if ny < 0 or ny > schematic_height - 1:
                continue

            if not (cell := grid[ny][nx]).isdigit() and cell != '.':
                part_numbers.append(m)
                break
        else:
            continue
        break

# print(part_numbers)
# print(sum(part_numbers))
pn_coords = {}
for pn in part_numbers:
    pn_y = pn.start() // schematic_width
    pn_x = pn.start() % schematic_height
    for offset in range(pn.end() - pn.start()):
        pn_coords[(pn_x+offset, pn_y)] = pn

gear_ratios = []

for m in re.finditer('\*', data.replace('\n', '')):
    y = m.start() // schematic_width
    x = m.start() % schematic_height

    adj = set()

    for i, j in neighbors:
        nx = x + i
        ny = y + j

        if (nx, ny) in pn_coords:
            adj.add(pn_coords[(nx, ny)])

    if len(adj) == 2:
        ratio = int(adj.pop()[0]) * int(adj.pop()[0])
        gear_ratios.append(ratio)

# print(gear_ratios)
submit(sum(gear_ratios))
