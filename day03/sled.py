#!/bin/python3

import argparse
from collections import namedtuple
import re

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()

with open(args.fname) as f:
    base = tuple(line.strip() for line in f.readlines())

TREE = '#'
FREE = '.'

def count_collisions(base, dx, dy):
    WIDTH = len(base[0])
    tree_count = 0
    idx = 0
    # right 3 down 1
    for line in base[::dy]:
        tree_count += 1 if line[idx % WIDTH] == TREE else 0
        idx += dx
    return tree_count

# part 1
print('right 3 down 1: {}'.format(count_collisions(base, 3, 1)))

# part 2
slopes = tuple(((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))
print('product: {}'.format(reduce(lambda a, b: a * b, map(lambda d: count_collisions(base, d[0], d[1]), slopes))))
