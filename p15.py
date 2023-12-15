from aocd import data, submit

# data = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''

steps = data.split(',')

sequence_sum = 0

for step in steps:
    hash_value = 0

    for char in step:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256

    sequence_sum += hash_value

submit(sequence_sum)
