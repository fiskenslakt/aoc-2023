from collections import deque

from aocd import data, submit

# data = r'''.|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....'''

DIRECTIONS = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
REFLECTIONS = {'/': {'^': '>', '>': '^', 'v': '<', '<': 'v'},
               '\\': {'^': '<', '>': 'v', 'v': '>', '<': '^'}}

contraption = {}

for y, row in enumerate(data.splitlines()):
    for x, tile in enumerate(row):
        # print(tile, end='')
        contraption[(x, y)] = tile
    # print()

queue = deque([(-1, 0, '>')])
energized_tiles = set()
seen = set()
# import pudb;pu.db
while queue:
    n_beams = len(queue)
    for _ in range(n_beams):
        x, y, d = queue.popleft()
        if (x, y) in contraption:
            energized_tiles.add((x, y))
        i, j = DIRECTIONS[d]
        nx = x + i
        ny = y + j

        while (nx, ny) in contraption:
            energized_tiles.add((nx, ny))
            tile = contraption[(nx, ny)]
            if tile == '.':
                i, j = DIRECTIONS[d]
                nx += i
                ny += j
            elif tile == '|':
                if d in '^v':
                    i, j = DIRECTIONS[d]
                    nx += i
                    ny += j
                    continue
                if (nx, ny, '^') not in seen:
                    queue.append((nx, ny, '^'))
                    seen.add((nx, ny, '^'))
                if (nx, ny, 'v') not in seen:
                    queue.append((nx, ny, 'v'))
                    seen.add((nx, ny, 'v'))
                break
            elif tile == '-':
                if d in '><':
                    i, j = DIRECTIONS[d]
                    nx += i
                    ny += j
                    continue
                if (nx, ny, '<') not in seen:
                    queue.append((nx, ny, '<'))
                    seen.add((nx, ny, '<'))
                if (nx, ny, '>') not in seen:
                    queue.append((nx, ny, '>'))
                    seen.add((nx, ny, '>'))
                break
            elif tile in REFLECTIONS and (nx, ny, nd := REFLECTIONS[tile][d]) not in seen:
                queue.append((nx, ny, nd))
                seen.add((nx, ny, nd))
                break
            else:
                break

print('Part 1:', len(energized_tiles))
submit(len(energized_tiles))
