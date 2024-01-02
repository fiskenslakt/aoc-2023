from aocd import data

PIPE_TYPES = {'north': '|7F', 'south': '|JL', 'west': '-LF', 'east': '-J7'}
DIRECTIONS = ((0, 1, 'south'), (1, 0, 'east'), (0, -1, 'north'), (-1, 0, 'west'))
ELBOWS = {'F', '7', 'J', 'L'}
NEXT_PIPE = {
    '|': ((0,1), (0,-1)), '-': ((1,0), (-1,0)),
    '7': ((-1,0), (0,1)), 'F': ((1,0), (0,1)),
    'J': ((-1,0), (0,-1)), 'L': ((1,0), (0,-1)),
}

graph = {}

for y, row in enumerate(data.splitlines()):
    for x, cell in enumerate(row):
        graph[(x, y)] = cell

        if cell == 'S':
            start = (x, y)

x, y = start
pipes = []
start_pipe = ''
for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
    nx = x + i
    ny = y + j

    if (nx, ny) not in graph:
        continue

    pipe = graph[(nx, ny)]

    if i == 1 and pipe in PIPE_TYPES['east']:
        pipes.append((nx, ny))
        start_pipe += 'e'
    elif i == -1 and pipe in PIPE_TYPES['west']:
        pipes.append((nx, ny))
        start_pipe += 'w'
    elif j == 1 and pipe in PIPE_TYPES['south']:
        pipes.append((nx, ny))
        start_pipe += 's'
    elif j == -1 and pipe in PIPE_TYPES['north']:
        pipes.append((nx, ny))
        start_pipe += 'n'

elbows = {'nw': 'J', 'en': 'L', 'sw': '7', 'se': 'F'}
start_elbow = elbows.get(start_pipe)
cpipe1, cpipe2 = pipes
prev_pipe1 = prev_pipe2 = start
steps = 1
loop = {start}

while cpipe1 != cpipe2:
    pipe1 = graph[cpipe1]
    pipe2 = graph[cpipe2]
    loop.add(cpipe1)
    loop.add(cpipe2)

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
loop.add(cpipe1)  # add furthest pipe

enclosed = 0
for y, row in enumerate(data.splitlines()):
    inside = False
    last_elbow = None
    for x, cell in enumerate(row):
        if (x, y) in loop:
            cur_pipe = graph[(x, y)]
            if cur_pipe == 'S':
                cur_pipe = start_elbow
            if cur_pipe in ELBOWS:
                if last_elbow is None:
                    last_elbow = cur_pipe
                elif last_elbow == 'F' and cur_pipe == 'J':
                    inside = not inside
                elif last_elbow == 'L' and cur_pipe == '7':
                    inside = not inside

                if cur_pipe in 'J7':
                    last_elbow = None
            elif cur_pipe == '|':
                inside = not inside
        else:
            enclosed += inside

print('Part 1:', steps)
print('Part 2:', enclosed)
