from aocd import data, submit

# data = '''#.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#'''


def hike(x, y, prev=None):
    steps = 0 if prev is None else 1

    while True:
        next_step = []

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + i
            ny = y + j

            if graph.get((nx, ny), ' ') not in '.<>^v' or (nx, ny) == prev:
                continue

            if (i == 1 and graph[(nx, ny)] == '<'
                    or i == -1 and graph[(nx, ny)] == '>'
                    or j == 1 and graph[(nx, ny)] == '^'
                    or j == -1 and graph[(nx, ny)] == 'v'):
                continue

            next_step.append((nx, ny))

        if len(next_step) == 1:
            steps += 1
            prev = (x, y)
            x, y = next_step.pop()
        else:
            prev = (x, y)
            break

    most_steps = 0
    for nx, ny in next_step:
        most_steps = max(hike(nx, ny, prev), most_steps)

    return steps + most_steps


graph = {}

for y, line in enumerate(lines := data.splitlines()):
    if y == 0:
        start = (line.index('.'), y)
    elif y == len(lines) - 1:
        end = (line.index('.'), y)

    for x, cell in enumerate(line):
        graph[(x, y)] = cell

# import pudb;pu.db
# print(hike(*start))
submit(hike(*start))
