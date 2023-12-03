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
        for i, j in ((0,1), (1,0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1,-1), (-1, 1)):
            nx = x + i + offset
            ny = y + j

            if nx < 0 or nx > schematic_width - 1:
                continue
            if ny < 0 or ny > schematic_height - 1:
                continue

            if not (cell := grid[ny][nx]).isdigit() and cell != '.':
                part_numbers.append(int(m[0]))
                break
        else:
            continue
        break

# print(part_numbers)
# print(sum(part_numbers))
submit(sum(part_numbers))
