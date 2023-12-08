import re
from math import lcm
from itertools import cycle

from aocd import data

instructions, nodes = data.split('\n\n')
node_p = re.compile(r'\w+')
graph = {}
for node in nodes.splitlines():
    src, left, right = node_p.findall(node)
    graph[src] = (left, right)


def camel_walk(start):
    cur_node = start
    for steps, i in enumerate(cycle(instructions), 1):
        if i == 'L':
            cur_node = graph[cur_node][0]
        elif i == 'R':
            cur_node = graph[cur_node][1]

        if cur_node.endswith('Z'):
            return steps


print('Part 1:', camel_walk('AAA'))

end_a = [node for node in graph if node.endswith('A')]
steps = lcm(*[camel_walk(node) for node in end_a])
print('Part 2:', steps)
