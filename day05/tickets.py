#!/bin/python3

import argparse
from collections import namedtuple, defaultdict
import functools

Ticket = namedtuple('Ticket', 'row column')

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()


def to_num(zero, one, string):
    return int(string.replace(zero, '0').replace(one, '1'), base=2)


calc_row = functools.partial(to_num, 'F', 'B')
calc_col = functools.partial(to_num, 'L', 'R')


with open(args.fname) as f:
    tickets = [Ticket(calc_row(line[:7]), calc_col(line[7:])) for line in f]

# part 1
print('part 1: {}'.format(max(ticket.row * 8 + ticket.column for ticket in tickets)))

# part 2
row_count = defaultdict(int)
for ticket in tickets:
    row_count[ticket.row] += 1

my_row = -1
for row, count in sorted(row_count.items()):
    if count < 8:
        my_row = row
        break

my_col = -1
for col in range(8):
    if Ticket(my_row, col) not in tickets:
        my_col = col
        break

print('part 2: {}'.format(my_row * 8 + my_col))
