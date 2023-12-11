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

for y, row in enumerate(expanded):
    for x, col in enumerate(row):
        if col == '#':
            galaxies.append((x, y))

path_lengths = []
for g1, g2 in combinations(galaxies, 2):
    x1, y1 = g1
    x2, y2 = g2

    length = abs(x1 - x2) + abs(y1 - y2)
    path_lengths.append(length)

submit(sum(path_lengths))
