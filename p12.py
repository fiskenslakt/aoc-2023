from aocd import data, submit

# data = '''???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1'''
# data = '''#??.. 2
# ??#.. 2
# ??..#? 2'''


def arrangements(record):
    a = 0
    r1, r2 = record
    broken = 0
    cur_broke = 0
    r3 = []
    for i, c in enumerate(r1):
        if c == '?':
            a += arrangements((r1[:i] + '.' + r1[i+1:], r2))
            a += arrangements((r1[:i] + '#' + r1[i+1:], r2))
            return a
        elif c == '#':
            broken += 1
            if broken > r2[cur_broke]:
                return 0 + a
        elif c == '.':
            if broken > 0:
                if broken < r2[cur_broke]:
                    return 0 + a
                assert broken == r2[cur_broke]
                r3.append(broken)
                if tuple(r3) == r2 and '#' not in r1[i+1:]:
                    # print(r1)
                    return 1 + a
                broken = 0
                cur_broke += 1
                if cur_broke >= len(r2):
                    return 0 + a

    # if broken == r2[cur_broke] and cur_broke == len(r2) - 1:
    #     print(r1)
    return int(broken == r2[cur_broke] and cur_broke == len(r2) - 1) + a


records = []

for line in data.splitlines():
    r1, r2 = line.split()
    r2 = tuple(map(int, r2.split(',')))
    records.append((r1, r2))

# # import pudb;pu.db
# arrangements(records[-1])
counts = []
for record in records:
    # print(record, arrangements(record))
    counts.append(arrangements(record))

submit(sum(counts))
# print(sum(counts))
