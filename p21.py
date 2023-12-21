from collections import deque

from aocd import data, submit

# data = '''...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........'''

grid = {}

for y, line in enumerate(data.splitlines()):
    for x, cell in enumerate(line):
        grid[(x, y)] = cell
        if cell == 'S':
            start = (x, y)

queue = deque([start])
steps = 0

while queue:
    possibilities = 0
    seen = set()
    # print(steps, len(queue))
    if steps == 64:
        break

    n_plots = len(queue)

    for _ in range(n_plots):
        x, y = queue.popleft()

        for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx = x + i
            ny = y + j

            if (nx, ny) not in grid:
                continue

            if (nx, ny) in seen:
                possibilities += 1
                continue

            if grid[(nx, ny)] == '#':
                continue

            queue.append((nx, ny))
            seen.add((nx, ny))
            possibilities += 1

    steps += 1
    # print(steps, possibilities)

# submit(len(seen))
# print(len(seen))
submit(len(queue))
