#!/bin/python3

import argparse
from collections import namedtuple
import re

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()

required_fields = {'byr': (r'[0-9]{4}$', lambda x: 1920 <= int(x) <= 2002), 
                   'iyr': (r'[0-9]{4}$', lambda x: 2010 <= int(x) <= 2020),
                   'eyr': (r'[0-9]{4}$', lambda x: 2020 <= int(x) <= 2030),
                   'hgt': (r'[0-9]+(cm|in)$', lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193) or (x.endswith('in') and 59 <= int(x[:-2]) <= 76)),
                   'hcl': (r'#[0-9a-f]{6}$', lambda x: True),
                   'ecl': (r'[a-z]{3}$', lambda x: x in tuple(('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))),
                   'pid': (r'[0-9]{9}$', lambda x: True)}

def valid_field_types(string):            
    return all(field + ':' in string for field in required_fields)

def valid_each_field(string):
    num_valid = 0
    for key, value in required_fields.items():
        match = re.search(r'{}:(\S*)'.format(key), string)
        if match:
            fvalue = match.groups()[0]
            if re.match(value[0], fvalue):
                num_valid += value[1](fvalue)
    return num_valid == len(required_fields)



part1 = 0
part2 = 0
with open(args.fname) as f:
    lines = list()
    for line in f:
        if line == '\n':
            part1 += valid_field_types(' '.join(lines))
            part2 += valid_each_field(' '.join(lines))
            lines = list()
        else:
            lines.append(line.strip())
    part1 += valid_field_types(' '.join(lines))
    part2 += valid_each_field(' '.join(lines))


print(f'part 1: {part1}')
print(f'part 2: {part2}')
