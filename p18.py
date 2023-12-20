from shapely import Polygon

from aocd import data

x = y = 0
rx = ry = 0
coords = [(0, 0)]
perimeter = 0
real_coords = [(0, 0)]
real_perimeter = 0

for line in data.splitlines():
    direction, amount, hex_value = line.split()
    amount = int(amount)

    perimeter += amount

    if direction == 'R':
        x += amount
    elif direction == 'L':
        x -= amount
    elif direction == 'U':
        y -= amount
    elif direction == 'D':
        y += amount

    coords.append((x, y))

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

polygon = Polygon(coords)
area = int(polygon.area + perimeter // 2 + 1)
print('Part 1:', area)

real_polygon = Polygon(real_coords)
real_area = int(real_polygon.area + real_perimeter // 2 + 1)
print('Part 2:', real_area)
