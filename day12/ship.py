import sys

instructions = [(s[0], int(s[1:].strip())) for s in sys.stdin]


easy_cos = {0: 1, 90: 0, 180: -1, 270: 0}
easy_sin = {0: 0, 90: 1, 180: 0, 270: -1}

commands = {'N': lambda val, x, y, heading: (x, y + val, heading),
            'S': lambda val, x, y, heading: (x, y - val, heading), 
            'E': lambda val, x, y, heading: (x + val, y, heading), 
            'W': lambda val, x, y, heading: (x - val, y, heading), 
            'L': lambda val, x, y, heading: (x, y, heading + val), 
            'R': lambda val, x, y, heading: (x, y, heading - val), 
            'F': lambda val, x, y, heading: (x + easy_cos[heading % 360] * val, y + easy_sin[heading % 360] * val, heading)}


def navigate(instructions):
    x = y = heading = 0
    for direction, value in instructions:
        x, y, heading = commands[direction](value, x, y, heading)

    return x, y

x, y = navigate(instructions)
print('part 1: {}'.format(abs(x) + abs(y)))




commands = {'N': lambda val, x, y: (x, y + val),
            'S': lambda val, x, y: (x, y - val), 
            'E': lambda val, x, y: (x + val, y), 
            'W': lambda val, x, y: (x - val, y), 
            'L': lambda val, x, y: (easy_cos[val % 360] * x - easy_sin[val % 360] * y, easy_sin[val % 360] * x + easy_cos[val % 360] * y), 
            'R': lambda val, x, y: (easy_cos[-val % 360] * x - easy_sin[-val % 360] * y, easy_sin[-val % 360] * x + easy_cos[-val % 360] * y)}

def naviagte_waypoint(instructions):
    wx, wy = 10, 1
    sx = sy = 0
    for direction, value in instructions:
        if direction == 'F':
            sx, sy = sx + value * wx, sy + wy * value
        else:
            wx, wy = commands[direction](value, wx, wy)
    return sx, sy

x, y = naviagte_waypoint(instructions)
print('part 2 {}'.format(abs(x) + abs(y)))
