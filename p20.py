import re
from collections import defaultdict, deque
from dataclasses import dataclass, field

from aocd import data, submit

# data = '''broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a'''


@dataclass
class Module:
    name: str
    destinations: list = field(default_factory=list)
    mtype: str = 'module'


@dataclass
class FlipFlop(Module):
    # False = "off"
    # True = "on"
    state: bool = False
    mtype: str = 'flipflop'

    def flip_state(self):
        self.state = not self.state

    def output_signal(self):
        return 'high' if self.state else 'low'


@dataclass
class Conjunction(Module):
    input_modules: dict = field(default_factory=dict)
    mtype: str = 'conjunction'

    def output_signal(self):
        if all(signal == 'high' for signal in self.input_modules.values()):
            return 'low'
        return 'high'


input_pattern = re.compile(r'([%&])?(\w+)')

modules = {}
input_map = defaultdict(list)

for line in data.splitlines():
    i, o = line.split(' -> ')
    source = input_pattern.search(i)
    destinations = o.split(', ')

    for d in destinations:
        input_map[d].append(source[2])

    source_type = source[1]
    if source_type is None:
        module = Module(source[2], destinations)
    elif source_type == '%':
        module = FlipFlop(source[2], destinations)
    elif source_type == '&':
        module = Conjunction(source[2], destinations)

    modules[source[2]] = module

for d, sources in input_map.items():
    if d not in modules:
        continue
    module = modules[d]
    if module.mtype == 'conjunction':
        for s in sources:
            module.input_modules[s] = 'low'

sent_signals = {'low': 0, 'high': 0}
# import pudb;pu.db
signal_queue = deque()
for button_press in range(1_000):
    sent_signals['low'] += 1
    for d in modules['broadcaster'].destinations:
        signal_queue.append((d, 'low', 'broadcaster'))

    while signal_queue:
        module_name, signal, source = signal_queue.popleft()
        if module_name in modules:
            module = modules[module_name]
        else:
            module = Module(module_name)
            modules[module.name] = module
        sent_signals[signal] += 1

        if module.mtype == 'flipflop':
            if signal == 'high':
                continue

            module.flip_state()
            for d in modules[module.name].destinations:
                new_signal = 'high' if module.state else 'low'
                signal_queue.append((d, module.output_signal(), module.name))

        if module.mtype == 'conjunction':
            module.input_modules[source] = signal
            for d in modules[module.name].destinations:
                signal_queue.append((d, module.output_signal(), module.name))

print(sent_signals)
submit(sent_signals['low'] * sent_signals['high'])
