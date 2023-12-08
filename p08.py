import re
# from itertools import repeat
from collections import deque

from aocd import data, submit

lri, nodes = data.split('\n\n')

node_p = re.compile(r'\w+')

graph = {}

for node in nodes.splitlines():
    src, left, right = node_p.findall(node)
    graph[src] = (left, right)

cur_node = 'AAA'
steps = 0
idx = 0
# for i in repeat(lri):
# while True:
#     i = lri[idx % len(lri)]
#     idx += 1
#     if i == 'L':
#         cur_node = graph[cur_node][0]
#     elif i == 'R':
#         cur_node = graph[cur_node][1]
#     else:
#         raise Exception(f'wtf: cur_node={cur_node}, i={i}')

#     steps += 1

#     if cur_node == 'ZZZ':
#         break

# submit(steps)
# queue = deque()
end_a = []
for node in graph:
    if node.endswith('A'):
        # queue.append(node)
        end_a.append(node)

end_z = []

for node in end_a:
    cur_node = node
    # found = False
    idx = 0
    steps = 0
    while True:
        i = lri[idx % len(lri)]
        idx += 1

        if i == 'L':
            cur_node = graph[cur_node][0]
        elif i == 'R':
            cur_node = graph[cur_node][1]
        else:
            raise Exception(f'wtf: cur_node={cur_node}, i={i}')

        steps += 1
        if cur_node.endswith('Z'):
            # import pudb;pu.db
            # if found:
            end_z.append((node, cur_node, steps))
            break
            # else:
            #     found = True
            #     steps = 0

print(end_z)

# import pudb;pu.db

# while queue:
#     if all(node.endswith('Z') for node in queue):
#         break
#     n_nodes = len(queue)
#     for _ in range(n_nodes):
#         cur_node = queue.popleft()

#         i = lri[idx % len(lri)]

#         if i == 'L':
#             queue.append(graph[cur_node][0])
#         elif i == 'R':
#             queue.append(graph[cur_node][1])
#         else:
#             raise Exception('shit')

#     steps += 1
#     idx += 1

# submit(steps)
from math import lcm
steps = lcm(*[s for _, _, s in end_z])
submit(steps)
