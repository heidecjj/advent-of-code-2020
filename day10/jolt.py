import sys
from collections import defaultdict

adapters = [0] + sorted([int(line.strip()) for line in sys.stdin])

adapters.append(adapters[-1] + 3)

diffs = defaultdict(int)
for first, second in zip(adapters[:-1], adapters[1:]):
    diffs[second-first] += 1

product = diffs[1] * diffs[3]
print(f'part 1: {product}')


def cached(func):

    def wrapper(arg):
        try:
            return cached.d[arg]
        except KeyError:
            val = func(arg)
            cached.d[arg] = val
        return val
    return wrapper

cached.d = dict()

@cached
def num_choices(index):
    if not index:
        return 1
    reachable = (idx for idx in range(index-3 if index > 3 else 0, index) if adapters[index] - adapters[idx] <= 3)
    return sum(map(num_choices, reachable))

print('part 2: {}'.format(num_choices(len(adapters) - 1)))    
