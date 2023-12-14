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


def reflections(layers):
    for i in range(1, len(layers)):
        yield zip(layers[i-1::-1], layers[i:])


def incidence(pattern):
    rows = pattern.splitlines()
    cols = list(zip(*rows))

    most_horizontal = (0, 0)
    most_vertical = (0, 0)

    for reflection in reflections(list(enumerate(rows, 1))):
        reflection = list(reflection)
        poi = reflection[0][0][0]
        mirrored = 0
        for (i, r1), (j, r2) in reflection:
            if r1 != r2:
                break
            mirrored += 1
        else:
            most_horizontal = max(most_horizontal, (mirrored, poi))

    for reflection in reflections(list(enumerate(cols, 1))):
        reflection = list(reflection)
        poi = reflection[0][0][0]
        mirrored = 0
        for (i, r1), (j, r2) in reflection:
            if r1 != r2:
                break
            mirrored += 1
        else:
            most_vertical = max(most_vertical, (mirrored, poi))

    return most_horizontal, most_vertical


patterns = data.split('\n\n')

notes = 0
for pattern in patterns:
    poi_h, poi_v = incidence(pattern)
    # print(pattern)
    # print(poi_h, poi_v, 'h' if poi_h[0] > poi_v[0] else 'v')
    if poi_v[0] > poi_h[0]:
        notes += poi_v[1]
        # print(poi_v, 'vert')
    else:
        notes += 100 * poi_h[1]
        # print(poi_h, 'horiz')

    # print()
submit(notes)
