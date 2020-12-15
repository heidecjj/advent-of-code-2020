import sys

earliest = int(sys.stdin.readline())
raw_busses = [x if x == 'x' else int(x) for x in sys.stdin.readline().strip().split(',')]


busses = sorted([x for x in raw_busses if x != 'x'])

timetable = dict()
for bus in reversed(busses):
    factor = earliest // bus
    timetable[bus * factor] = timetable[bus * (factor + 1)] = bus

wait = 0
while True:
    bus = timetable.get(earliest + wait)
    if bus:
        print('part 1: {}'.format(bus * wait))
        break
    wait += 1


busses = [(idx, bus) for idx, bus in enumerate(raw_busses) if bus != 'x']

def find_mod_numerator(period, offset, denomonator, goal):
    # (i * period + offset) % denomonator = goal
    # return lowest i * period + offset
    goal = goal % denomonator
    i = 1
    while True:
        if (i * period + offset) % denomonator == goal:
            return i * period + offset
        i += 1

t = 1
period = 1
for idx, bus in busses:
    t = find_mod_numerator(period, t, bus, -idx)
    period *= bus

print(f'part 2: {t}')

