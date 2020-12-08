#!/bin/python3

import argparse
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()


with open(args.fname) as f:
    fcontents = f.read()
    
print('part 1: {}'.format(sum(len(set(group.replace('\n', ''))) for group in fcontents.split('\n\n'))))

print('part 2: {}'.format(sum(len(reduce(lambda a, b: a & b, map(set, raw_group.strip().split('\n')))) for raw_group in fcontents.split('\n\n'))))
