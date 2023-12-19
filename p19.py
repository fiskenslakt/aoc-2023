import re
from operator import gt, lt

from aocd import data, submit

# data = '''px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}'''


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

    def __repr__(self):
        return self.value


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
    x, m, a, s = map(int, re.findall(r'\d+', part))
    xmas = {'x': x, 'm': m, 'a': a, 's': s}

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


workflows_raw, parts = data.split('\n\n')

workflows = {}
# import pudb;pu.db
for workflow in workflows_raw.splitlines():
    name, *rules = re.split(r'{|:', workflow[:-1])

    workflows[name] = RuleTree(rules)

rating_numbers_total = 0
for part in parts.splitlines():
    if sort_part(part, 'in') == 'A':
        rating_numbers_total += sum(map(int, re.findall(r'\d+', part)))

submit(rating_numbers_total)
