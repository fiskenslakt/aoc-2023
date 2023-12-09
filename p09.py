from aocd import data


def oasis(history, backwards=False):
    if len(set(history)) == 1:
        return history[-1]

    new_history = []
    for a, b in zip(history, history[1:]):
        new_history.append(b - a)

    if backwards:
        return history[0] - oasis(new_history, backwards=True)
    else:
        return history[-1] + oasis(new_history)


next_sum = 0
prev_sum = 0

for line in data.splitlines():
    history = [int(n) for n in line.split()]

    next_sum += oasis(history)
    prev_sum += oasis(history, backwards=True)

print('Part 1:', next_sum)
print('Part 2:', prev_sum)
