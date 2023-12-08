import re
from itertools import repeat

from aocd import data, submit

lri, nodes = data.split('\n\n')
# raise SystemExit
node_p = re.compile(r'\w+')

graph = {}

for node in nodes.splitlines():
    src, left, right = node_p.findall(node)
    graph[src] = (left, right)

cur_node = 'AAA'
steps = 0
idx = 0
# for i in repeat(lri):
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

    if cur_node == 'ZZZ':
        break

submit(steps)
