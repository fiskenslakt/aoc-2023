from math import prod

from aocd import data

times, dists = data.splitlines()

real_t = int(''.join(times.split()[1:]))
real_d = int(''.join(dists.split()[1:]))
times = map(int, times.split()[1:])
dists = map(int, dists.split()[1:])

total_ways = []
for time, dist in zip(times, dists):
    ways = 0
    for i in range(1, time):
        ways += i * (time - i) > dist

    total_ways.append(ways)

ways = 0
for i in range(1, real_t):
    ways += i * (real_t - i) > real_d

print('Part 1:', prod(total_ways))
print('Part 2:', ways)
