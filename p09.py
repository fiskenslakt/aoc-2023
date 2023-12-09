from aocd import data, submit

# data = '''0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45'''


def oasis(history):
    # if all(n == 0 for n in history):
    #     return
    if len(set(history)) == 1:
        return history[-1]

    new_history = []
    for a, b in zip(history, history[1:]):
        new_history.append(b - a)

    return history[-1] + oasis(new_history)


x = 0
nums = []
for line in data.splitlines():
    nums.append([int(n) for n in line.split()])

    x += oasis(nums[-1])

submit(x)
