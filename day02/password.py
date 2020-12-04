import argparse
from collections import namedtuple
import re

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()

password = namedtuple('password', 'min max letter password')

def parse_password(line):
    mi, ma, letter, passwd = re.match(r'([0-9]+)-([0-9]+) ([a-zA-Z]): (.*)\s*', line).groups()

    return password(int(mi), int(ma), letter, passwd)

with open(args.fname) as f:
    passwords = [parse_password(line) for line in f.readlines()]

# part 1
valid = [passwd for passwd in passwords if passwd.min <= passwd.password.count(passwd.letter) <= passwd.max]
print('one {}'.format(len(valid)))

# part2
valid = [passwd for passwd in passwords if (passwd.password[passwd.min - 1] == passwd.letter) ^ (passwd.password[passwd.max - 1] == passwd.letter)]
print('two {}'.format(len(valid)))
