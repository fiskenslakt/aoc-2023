from math import prod

from aocd import data, submit

# data = '''Time:      7  15   30
# Distance:  9  40  200'''

times, dists = data.splitlines()

real_t = int(''.join(times.split()[1:]))
real_d = int(''.join(dists.split()[1:]))
times = map(int, times.split()[1:])
dists = map(int, dists.split()[1:])

# print(real_t)
# print(real_d)

# x = []
# for time, dist in zip(times, dists):
#     y = 0
#     for i in range(1, time):
#         if i * (time - i) > dist:
#             y += 1

#     x.append(y)


# submit(prod(x))

ways = 0
for i in range(1, real_t):
    if i * (real_t - i) > real_d:
        ways += 1

print(ways)
submit(ways)
raise SystemExit

x = y = real_t // 2
ways = 0
while True:
    # print(x, y, x * y)
    if x * y > real_d:
        ways += 1
    else:
        break

    x += 1
    y -= 1

print(ways)
