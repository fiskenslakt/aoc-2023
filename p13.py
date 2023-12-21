from math import log2

from aocd import data, submit

# data = '''#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#'''


def smudge_found(layer1, layer2):
    l1 = int(layer1.replace('#', '1').replace('.', '0'), 2)
    l2 = int(layer2.replace('#', '1').replace('.', '0'), 2)
    return log2(l1 ^ l2).is_integer()


def reflections(layers):
    for i in range(1, len(layers)):
        yield zip(layers[i-1::-1], layers[i:])


def incidence(pattern, find_smudge=False):
    rows = pattern.splitlines()
    cols = list(zip(*rows))

    # most_horizontal = (0, 0)
    # most_vertical = (0, 0)
    pois = []

    for reflection in reflections(list(enumerate(rows, 1))):
        had_smudge = False
        reflection = list(reflection)
        poi = reflection[0][0][0]
        # mirrored = 0
        for (i, r1), (j, r2) in reflection:
            if r1 != r2:
                if find_smudge and smudge_found(r1, r2):
                    had_smudge = True
                else:
                    break
            # mirrored += 1
        else:
            pois.append((poi, 'h', had_smudge))
            # most_horizontal = max(most_horizontal, (mirrored, poi))

    for reflection in reflections(list(enumerate(cols, 1))):
        had_smudge = False
        reflection = list(reflection)
        poi = reflection[0][0][0]
        # mirrored = 0
        for (i, r1), (j, r2) in reflection:
            if r1 != r2:
                if find_smudge and smudge_found(''.join(r1), ''.join(r2)):
                    had_smudge = True
                else:
                    break
            # mirrored += 1
        else:
            pois.append((poi, 'v', had_smudge))
            # most_vertical = max(most_vertical, (mirrored, poi))

    # return most_horizontal, most_vertical
    return pois


patterns = data.split('\n\n')
# import pudb;pu.db
notes = 0
for pattern in patterns:
    # poi_h, poi_v = incidence(pattern, find_smudge=True)
    pois = incidence(pattern, find_smudge=True)
    for poi, orientation, had_smudge in pois:
        if had_smudge:
            break
    print(pattern)
    print(poi, orientation)
    # print(poi_h, poi_v, 'h' if poi_h[0] > poi_v[0] else 'v')
    # if poi_v[0] > poi_h[0]:
    if orientation == 'v':
        # notes += poi_v[1]
        notes += poi
        # print(poi_v, 'vert')
    else:
        # notes += 100 * poi_h[1]
        notes += 100 * poi
        # print(poi_h, 'horiz')

    print()
# submit(notes)
submit(notes)
