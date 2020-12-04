#!/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()

with open(args.fname) as f:
    nums = sorted([int(num.strip()) for num in f.readlines()])


def add_to(target, options):
    for num in options:
        if target - num in options:
            return num * (target - num)
    return 0

# part 1
print('one', add_to(2020, nums))

# part2
for num in nums:
    partial = add_to(2020 - num, nums)
    if partial:
        print('two', num * partial)
        break
