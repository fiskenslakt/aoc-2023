from aocd import data, submit

# with open('5.in') as f:
#     data = f.read()

seeds, *maps = data.split('\n\n')

seeds = list(map(int, seeds.split()[1:]))
maps = [list(map(str.split, m))[1:] for m in  map(lambda s: s.split('\n'), maps)]

locations = []

for seed in seeds:
    n = int(seed)
    for m in maps:
        for r in m:
            dest, source, length = map(int, r)
            if n in range(source, source + length):
                n = dest + (n - source)
                break

    locations.append(n)

# print(locations)
submit(min(locations))
