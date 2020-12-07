#!/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()


with open(args.fname) as f:
    tickets = sorted(int(line.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), base=2) for line in f)

# part 1
print('part 1: {}'.format(tickets[-1]))

# part 2
prev_ticket = tickets[0]
for ticket in tickets[1:]:
    if ticket - prev_ticket == 2:
        print('part 2: {}'.format(ticket - 1))
        break
    prev_ticket = ticket
