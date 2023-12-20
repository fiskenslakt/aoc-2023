from collections import deque
from shapely import Polygon

from aocd import data, submit

# data = '''R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)'''

x = y = 0
rx = ry = 0
lagoon = set()
min_x = min_y = float('inf')
max_x = max_y = float('-inf')
coords = [(0, 0)]
real_coords = [(0, 0)]
real_perimeter = 0

for line in data.splitlines():
    direction, amount, hex_value = line.split()
    amount = int(amount)

    real_amount = int(hex_value[2:-2], 16)
    real_direction = hex_value[-2]
    real_perimeter += real_amount

    if real_direction == '0':    # R
        rx += real_amount
    elif real_direction == '1':  # D
        ry += real_amount
    elif real_direction == '2':  # L
        rx -= real_amount
    elif real_direction == '3':  # U
        ry -= real_amount

    real_coords.append((rx, ry))

    for _ in range(amount):
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y -= 1
        elif direction == 'D':
            y += 1

        lagoon.add((x, y))
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    coords.append((x, y))

queue = deque([(min_x-1, min_y-1)])
seen = {(min_x-1, min_y-1)}
# import pudb;pu.db
while queue:
    x, y = queue.popleft()

    for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nx = x + i
        ny = y + j

        if (min_x-1 <= nx <= max_x+1
                and min_y-1 <= ny <= max_y+1):
            if (nx, ny) in lagoon or (nx, ny) in seen:
                continue

            seen.add((nx, ny))
            queue.append((nx, ny))

bounding_box_area = (abs((min_x - 1) - (max_x + 1)) + 1) * (abs((min_y - 1) - (max_y + 1)) + 1)
lagoon_area = bounding_box_area - len(seen)
print('Part 1:', lagoon_area)
# assert lagoon_area == 50465

polygon = Polygon(coords)
print(polygon.area + len(lagoon) // 2 + 1)

real_polygon = Polygon(real_coords)
real_area = int(real_polygon.area + real_perimeter // 2 + 1)
submit(real_area)
