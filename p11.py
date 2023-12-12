from itertools import combinations

from aocd import data

rows = data.splitlines()
row_length = len(rows[0])
cols = list(zip(*rows))

empty_rows = [i for i, row in enumerate(rows) if '#' not in row]
empty_cols = [i for i, col in enumerate(cols) if '#' not in col]

galaxies = []

for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col == '#':
            galaxies.append((x, y))

path_lengths = []
path_lengths_very_expanded = []
for g1, g2 in combinations(galaxies, 2):
    x1, y1 = g1
    x2, y2 = g2

    x_offset = 0
    y_offset = 0
    big_x_offset = 0
    big_y_offset = 0

    for i in empty_rows:
        if min(y1,y2) < i < max(y1,y2):
            big_y_offset += int(1e6) - 1
            y_offset += 1

    for i in empty_cols:
        if min(x1,x2) < i < max(x1,x2):
            big_x_offset += int(1e6) - 1
            x_offset += 1

    length = abs(x1 - x2) + abs(y1 - y2) + x_offset + y_offset
    big_length = abs(x1 - x2) + abs(y1 - y2) + big_x_offset + big_y_offset
    path_lengths.append(length)
    path_lengths_very_expanded.append(big_length)

print('Part 1:', sum(path_lengths))
print('Part 2:', sum(path_lengths_very_expanded))
