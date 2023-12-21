from aocd import data


def smudge_found(layer1, layer2):
    l1 = int(layer1.replace('#', '1').replace('.', '0'), 2)
    l2 = int(layer2.replace('#', '1').replace('.', '0'), 2)
    return (l1 ^ l2).bit_count() == 1


def reflections(layers):
    for i in range(1, len(layers)):
        yield i, zip(layers[i-1::-1], layers[i:])


def find_reflections(layers, orientation):
    points_of_incidence = []

    for poi, reflection in reflections(layers):
        had_smudge = False
        for r1, r2 in reflection:
            if r1 != r2:
                if smudge_found(r1, r2):
                    had_smudge = True
                else:
                    break
        else:
            points_of_incidence.append((poi, orientation, had_smudge))

    return points_of_incidence


def incidence(pattern):
    rows = pattern.splitlines()
    cols = [''.join(col) for col in zip(*rows)]

    return find_reflections(rows, 'h') + find_reflections(cols, 'v')


patterns = data.split('\n\n')
notes = 0
notes_with_smudge = 0

for pattern in patterns:
    points_of_incidence = incidence(pattern)
    for poi, orientation, had_smudge in points_of_incidence:
        if had_smudge:
            notes_with_smudge += poi * (100 if orientation == 'h' else 1)
        else:
            notes += poi * (100 if orientation == 'h' else 1)

print('Part 1:', notes)
print('Part 2:', notes_with_smudge)
