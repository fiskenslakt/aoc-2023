import re
from itertools import combinations

from aocd import data, submit
from shapely.geometry import LineString

# data = '''19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3'''

# TEST_AREA = range(7, 27+1)
TEST_AREA = range(200_000_000_000_000, 400_000_000_000_000 + 1)

hailstones = []
for line in data.splitlines():
    px, py, pz, vx, vy, vz = map(int, re.findall(r'-?\d+', line))

    hailstones.append((px, py, pz, vx, vy, vz))

intersections = 0
for hailstone_a, hailstone_b in combinations(hailstones, 2):
    x1, y1, *_, vx1, vy1, _ = hailstone_a
    x2, y2, *_, vx2, vy2, _ = hailstone_b

    min_nano_seconds = max(
        abs(x1 - TEST_AREA.start if vx1 < 0 else TEST_AREA.stop) // abs(vx1),
        abs(x2 - TEST_AREA.start if vx2 < 0 else TEST_AREA.stop) // abs(vx2),
        abs(y1 - TEST_AREA.start if vy1 < 0 else TEST_AREA.stop) // abs(vy1),
        abs(y2 - TEST_AREA.start if vy2 < 0 else TEST_AREA.stop) // abs(vy2),
    )

    nx1 = x1 + vx1 * min_nano_seconds
    ny1 = y1 + vy1 * min_nano_seconds
    nx2 = x2 + vx2 * min_nano_seconds
    ny2 = y2 + vy2 * min_nano_seconds
    # nx1, ny1 = x1, y1
    # nx2, ny2 = x2, y2

    # while all(axis in TEST_AREA for axis in (nx1, ny1, nx2, ny2)):
    #     nx1 += vx1
    #     ny1 += vy1
    #     nx2 += vx2
    #     ny2 += vy2


    a = LineString([(x1, y1), (nx1, ny1)])
    b = LineString([(x2, y2), (nx2, ny2)])

    if a.intersects(b):
        ix, iy = a.intersection(b).xy
        if int(ix[0]) in TEST_AREA and int(iy[0]) in TEST_AREA:
            intersections += 1

submit(intersections)
print(intersections)
