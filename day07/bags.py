#!/bin/python3

import argparse
from collections import namedtuple
import re

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()

Node = namedtuple('Node', 'this next')

with open(args.fname) as f:
    # {color: [(int, color), ...]}
    graph = {bags[0]: [desc.split(' ', 1) for desc in re.findall(r'(?: ([0-9]+ \S+ \S+) bags?[,.])', bags[1])] for bags in (re.match(r'(.*) bags contain(.*)', string).groups() for string in f)}


max_depth = len(graph)

get_to_gold = set()
for outer in graph:
    seen = set()
    nodes = [(outer, 0)]
    stack = list()
    while nodes:
        node, depth = nodes.pop()
        while len(stack) > depth:  # prune stack
            stack.pop()
        if node == 'shiny gold' or node in get_to_gold:  # anything in stack can get to gold
            get_to_gold.update(stack)
            break
        if depth >= max_depth or node in seen:  # kill loops
            continue

        stack.append(node)
        seen.add(node)
        nodes.extend((n[1], depth + 1) for n in graph[node])  # graph[node] = (int, color)

print('part 1: {}'.format(len(get_to_gold)))


def bag_count(color, init=0):
    return init + sum(map(lambda x: int(x[0]) * bag_count(x[1], init=1), graph[color]))

print('part 2: {}'.format(bag_count('shiny gold')))
