from itertools import combinations

from aocd import data, submit

# data = '''...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....'''

rows = data.splitlines()
row_length = len(rows[0])
cols = list(zip(*rows))

empty_rows = [i for i, row in enumerate(rows) if '#' not in row]
empty_cols = [i for i, col in enumerate(cols) if '#' not in col]

print(empty_rows, empty_cols)

expanded = []
for i, row in enumerate(rows):
    if i in empty_rows:
        expanded.append('.' * (row_length + len(empty_cols)))
    new_row = ''
    for j, col in enumerate(row):
        if j in empty_cols:
            new_row += '.'

        new_row += col

    expanded.append(new_row)

galaxies = []

for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col == '#':
            galaxies.append((x, y))

path_lengths = []
for g1, g2 in combinations(galaxies, 2):
    x1, y1 = g1
    x2, y2 = g2

    x_offset = 0
    y_offset = 0

    for i in empty_rows:
        if min(y1,y2) < i < max(y1,y2):
            y_offset += int(1e6) - 1
            # y_offset += 9

    for i in empty_cols:
        if min(x1,x2) < i < max(x1,x2):
            x_offset += int(1e6) - 1
            # x_offset += 9

    length = abs(x1 - x2) + abs(y1 - y2) + x_offset + y_offset
    path_lengths.append(length)

submit(sum(path_lengths))
# print(sum(path_lengths))
