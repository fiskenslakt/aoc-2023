from aocd import data, submit


times, dists = data.splitlines()

times = list(map(int, times.split()[1:]))
dists = list(map(int, dists.split()[1:]))

# print(times)
# print(dists)
x = []
for time, dist in zip(times, dists):
    y = 0
    for i in range(1, time):
        if i * (time - i) > dist:
            y += 1

    x.append(y)

from math import prod
submit(prod(x))
