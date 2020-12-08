import argparse
from collections import namedtuple
import re

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()

Inst = namedtuple('inst', 'op arg')

op_map = {'nop': lambda pc, acc, arg: (pc + 1, acc),
          'acc': lambda pc, acc, arg: (pc + 1, acc + arg),
          'jmp': lambda pc, acc, arg: (pc + arg, acc)}

with open(args.fname) as f:
    program = [line.split(' ') for line in f]
program = [Inst(line[0], int(line[1])) for line in program]


def run(pc, acc, program):
    op, arg = program[pc]
    return op_map[op](pc, acc, arg)

seen = set()
pc = acc = 0
while pc < len(program):
    if pc in seen:
        print('part 1: {}'.format(acc))
        break
    seen.add(pc)
    pc, acc = run(pc, acc, program)

programs = (program[:lineno] + [Inst('nop' if line.op == 'jmp' else 'jmp',line.arg)] + program[lineno + 1:] for lineno, line in enumerate(program) if line[0] in ('jmp', 'nop'))

for pgrm in programs:
    seen = set()
    pc = acc = 0
    while pc < len(pgrm):
        if pc in seen:
            break
        seen.add(pc)
        pc, acc = run(pc, acc, pgrm)
    else:
        print('part 2: {}'.format(acc))
        break
