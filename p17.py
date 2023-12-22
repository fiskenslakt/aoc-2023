from heapq import heappop, heappush, heapify

from aocd import data, submit

# data = '''2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533'''

city_map = {}

for y, row in enumerate(data.splitlines()):
    for x, block in enumerate(row):
        city_map[(x, y)] = int(block)

factory = (x, y)

start_node = [x + y, 0, 0, 0, 0, None, None, [(0, 0)]]
nodes = {(0, 0, None): start_node}
queue = [start_node]
# import pudb;pu.db
while queue:
    # print(len(queue))
    cost, incurred_heat_loss, consecutive, x, y, d, prev, path = heappop(queue)

    if (x, y) == factory:
        break

    for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx = x + i
        ny = y + j
        if (nx, ny) not in city_map:
            continue

        new_path = path.copy()
        new_path.append((nx, ny))

        new_heat_loss = city_map[(nx, ny)]
        new_cost = abs(nx - factory[0]) + abs(ny - factory[1]) + new_heat_loss + incurred_heat_loss

        if (nx, ny) == prev:
            continue

        if i == 1:
            nd = '>'
        elif i == -1:
            nd = '<'
        elif j == 1:
            nd = 'v'
        elif j == -1:
            nd = '^'

        if (nx, ny, nd) in nodes:
            if new_cost < nodes[(nx, ny, nd)][0]:
                update = True
            elif consecutive != nodes[(nx, ny, nd)][2]:
                pass
            else:
                continue
        else:
            update = False

        if nd == d:
            if consecutive + 1 > 3:
                continue

            node = [new_cost, incurred_heat_loss + new_heat_loss, consecutive + 1, nx, ny, d, (x, y), new_path]

            if update:
                nodes[(nx, ny, nd)][:] = node
                heapify(queue)
            else:
                nodes[(nx, ny, nd)] = node
                heappush(queue, node)
        else:
            node = [new_cost, incurred_heat_loss + new_heat_loss, 1, nx, ny, nd, (x, y), new_path]

            if update:
                nodes[(nx, ny, nd)][:] = node
                heapify(queue)
            else:
                nodes[(nx, ny, nd)] = node
                heappush(queue, node)

print('Part 1:', incurred_heat_loss)
# print(path)
submit(incurred_heat_loss)
