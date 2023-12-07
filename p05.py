from collections import deque
# from more_itertools import chunked

# from aocd import data, submit


def overlap(r1, r2):
    return r1.stop > r2.start and r2.stop > r1.start


def chunked(seq, n):
    return zip(*[iter(seq)]*n)


with open('5_real.in') as f:
    data = f.read()

seeds, *maps = data.split('\n\n')

seeds = list(map(int, seeds.split()[1:]))
seed_pairs = chunked(seeds, 2)
seed_ranges = []
for sr in seed_pairs:
    seed_ranges.append(range(sr[0], sr[0]+sr[1]))

maps = [list(map(str.split, m))[1:] for m in  map(lambda s: s.split('\n'), maps)]
# print(maps)
# raise SystemExit

# locations = []

# for seed in seeds:
#     n = int(seed)
#     for m in maps:
#         for r in m:
#             dest, source, length = map(int, r)
#             if n in range(source, source + length):
#                 n = dest + (n - source)
#                 break

#     locations.append(n)

# print(locations)
# print(min(locations))

# import pudb;pu.db
# print('maps:', len(maps))
for i, m in enumerate(maps, 1):
    print('current map:', i)
    new_seed_ranges = []
    for sr in seed_ranges:
        range_queue = deque([sr])
        while range_queue:
            # print('range queue:', range_queue)
            # if range_queue == deque([range(1585502931, 1729527586)]):
            #     import pudb;pu.db
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

print(seed_ranges)
print(min(seed_ranges, key=lambda r: r.start))
print(min(seed_ranges, key=lambda r: r.start).start)
