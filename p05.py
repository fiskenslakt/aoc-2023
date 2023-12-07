from collections import deque
from more_itertools import chunked

from aocd import data


def overlap(r1, r2):
    return r1.stop > r2.start and r2.stop > r1.start


seeds, *maps = data.split('\n\n')

seeds = list(map(int, seeds.split()[1:]))
seed_pairs = chunked(seeds, 2)
seed_ranges = []
for sr in seed_pairs:
    seed_ranges.append(range(sr[0], sr[0]+sr[1]))

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

print('Part 1:', min(locations))

for i, m in enumerate(maps, 1):
    new_seed_ranges = []
    for sr in seed_ranges:
        range_queue = deque([sr])
        while range_queue:
            cr = range_queue.popleft()
            for mr in m:
                _, source, length = map(int, mr)
                mr = range(source, source + length)
                if overlap(cr, mr):
                    inner = range(max(sr.start, mr.start), min(sr.stop, mr.stop))
                    left_outer = range(min(sr.start, mr.start), max(sr.start, mr.start))
                    right_outer = range(min(sr.stop, mr.stop), max(sr.stop, mr.stop))

                    if inner not in new_seed_ranges:
                        new_seed_ranges.append(inner)
                    else:
                        break

                    if len(left_outer) and overlap(left_outer, cr):
                        range_queue.append(left_outer)
                    if len(right_outer) and overlap(right_outer, cr):
                        range_queue.append(right_outer)

                    break
            else:
                new_seed_ranges.append(cr)

    seed_ranges = []
    for sr in new_seed_ranges:
        for mr in m:
            dest, source, length = map(int, mr)
            mr = range(source, source + length)

            if overlap(sr, mr):
                offset = dest - source
                nr = range(sr.start + offset, sr.stop + offset)
                seed_ranges.append(nr)
                break
        else:
            seed_ranges.append(sr)

print('Part 2:', min(seed_ranges, key=lambda r: r.start).start)
