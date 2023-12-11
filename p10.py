from aocd import data, submit

PIPE_TYPES = {'north': '|7F', 'south': '|JL', 'west': '-LF', 'east': '-J7'}
DIRECTIONS = ((0, 1, 'south'), (1, 0, 'east'), (0, -1, 'north'), (-1, 0, 'west'))
NEXT_PIPE = {
    '|': ((0,1), (0,-1)), '-': ((1,0), (-1,0)),
    '7': ((-1,0), (0,1)), 'F': ((1,0), (0,1)),
    'J': ((-1,0), (0,-1)), 'L': ((1,0), (0,-1)),
}


# def next_pipe(coord):
#     x, y = coord
#     for i, j, direction in DIRECTIONS:
#         nx = x + i
#         ny = y + j
#         pipe = graph[(nx, ny)]

#         if pipe in PIPE_TYPES[direction]:
#             return (nx, ny)

# data = '''.....
# .S-7.
# .|.|.
# .L-J.
# .....'''

# data = '''-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF'''

# data = '''..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...'''

# data = '''7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ'''

graph = {}

for y, row in enumerate(data.splitlines()):
    for x, cell in enumerate(row):
        graph[(x, y)] = cell

        if cell == 'S':
            start = (x, y)

x, y = start
pipes = []
for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
    nx = x + i
    ny = y + j

    if (nx, ny) not in graph:
        continue

    pipe = graph[(nx, ny)]

    if i == 1 and pipe in PIPE_TYPES['east']:
        pipes.append((nx, ny))
    elif i == -1 and pipe in PIPE_TYPES['west']:
        pipes.append((nx, ny))
    elif j == 1 and pipe in PIPE_TYPES['south']:
        pipes.append((nx, ny))
    elif j == -1 and pipe in PIPE_TYPES['north']:
        pipes.append((nx, ny))

cpipe1, cpipe2 = pipes
prev_pipe1 = prev_pipe2 = start
steps = 1
# import pudb;pu.db
while cpipe1 != cpipe2:
    pipe1 = graph[cpipe1]
    pipe2 = graph[cpipe2]

    for i, j in NEXT_PIPE[pipe1]:
        x, y = cpipe1
        nx = x + i
        ny = y + j
        if (nx,ny) != prev_pipe1:
            prev_pipe1 = cpipe1
            cpipe1 = (nx, ny)
            break

    for i, j in NEXT_PIPE[pipe2]:
        x, y = cpipe2
        nx = x + i
        ny = y + j
        if (nx,ny) != prev_pipe2:
            prev_pipe2 = cpipe2
            cpipe2 = (nx, ny)
            break

    steps += 1

print(cpipe1, steps)
submit(steps)
