import re
from math import prod
from operator import gt, lt

from aocd import data


class Rule:
    def __init__(self, rule):
        self.value = rule
        self.condition = '>' in rule or '<' in rule
        if self.condition:
            category, op, n = re.search(r'(.)([<>])(\d+)', rule).groups()
            self.category = category
            self.n = int(n)
            if op == '>':
                self.op = gt
            else:
                self.op = lt

    # def __repr__(self):
    #     return self.value


class RuleTree:
    def __init__(self, rules):
        prev_rule = None
        for rule in rules:
            if prev_rule is None:
                prev_rule = Rule(rule)
                self.head = prev_rule
            else:
                r1, r2 = rule.split(',')
                prev_rule.true = Rule(r1)
                prev_rule.false = Rule(r2)
                prev_rule = prev_rule.false


def traverse_workflow(part, rule):
    xmas = dict(zip('xmas', map(int, re.findall(r'\d+', part))))

    if not rule.condition:
        return rule.value

    if rule.op(xmas[rule.category], rule.n):
        return rule.true.value
    else:
        return traverse_workflow(part, rule.false)


def sort_part(part, workflow_name):
    if workflow_name in 'RA':
        return workflow_name
    workflow = workflows[workflow_name]
    return sort_part(part, traverse_workflow(part, workflow.head))


def _findall_accepted(rule, xmas):
    accepted = 0
    if not rule.condition:
        return findall_accepted(rule.value)

    if rule.op is gt:
        true = xmas.copy()
        true[rule.category] = range(max(true[rule.category].start, rule.n+1), true[rule.category].stop)
        accepted += findall_accepted(rule.true.value, true)

        false = xmas.copy()
        false[rule.category] = range(false[rule.category].start, min(false[rule.category].stop, rule.n+1))
        if rule.false.condition:
            accepted += _findall_accepted(rule.false, false)
        else:
            accepted += findall_accepted(rule.false.value, false)
    else:
        true = xmas.copy()
        true[rule.category] = range(true[rule.category].start, min(true[rule.category].stop, rule.n))
        accepted += findall_accepted(rule.true.value, true)

        false = xmas.copy()
        false[rule.category] = range(max(false[rule.category].start, rule.n), false[rule.category].stop)
        if rule.false.condition:
            accepted += _findall_accepted(rule.false, false)
        else:
            accepted += findall_accepted(rule.false.value, false)

    return accepted


def findall_accepted(workflow_name, xmas):
    if workflow_name == 'A':
        # return prod([r.stop - r.start for r in xmas.values()])
        return prod(map(len, xmas.values()))
    elif workflow_name == 'R':
        return 0

    rule = workflows[workflow_name].head
    return _findall_accepted(rule, xmas)


workflows_raw, parts = data.split('\n\n')
workflows = {}
for workflow in workflows_raw.splitlines():
    name, *rules = re.split(r'{|:', workflow[:-1])
    workflows[name] = RuleTree(rules)

rating_numbers_total = 0
for part in parts.splitlines():
    if sort_part(part, 'in') == 'A':
        rating_numbers_total += sum(map(int, re.findall(r'\d+', part)))

print('Part 1:', rating_numbers_total)
# import pudb;pu.db
xmas = dict(zip('xmas', [range(1, 4001)]*4))
p2 = findall_accepted('in', xmas)
# submit(p2)
print('Part 2:', p2)
# print(f'{abs(p2 - 167409079868000):,}')
# assert p2 == 167409079868000
