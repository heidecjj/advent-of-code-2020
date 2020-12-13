import sys
import timeit

initial_state = [[char for char in line.strip()] for line in sys.stdin]

start = timeit.default_timer()

max_row = len(initial_state)
max_col = len(initial_state[0])

def next_seat(row, col, state):
    seat = state[row][col]
    if seat == '.':
        return seat

    num_occupied = sum(state[r][c] == '#' for c in range(max(col - 1, 0), min(col + 2, max_col)) for r in range(max(row - 1, 0), min(row + 2, max_row)) if not (r == row and c == col))

    if seat == 'L' and num_occupied == 0:
        return '#'
    if seat == '#' and num_occupied >= 4:
        return 'L'
    return seat

def states(state):
    next_state = state
    while True:
        next_state = [[next_seat(row, col, next_state) for col in range(max_col)] for row in range(max_row)]
        yield next_state

prev_state = initial_state
for state in states(initial_state):
    if state == prev_state:
        break
    prev_state = state

print('part 1: {}'.format(sum(state[row][col] == '#' for row in range(max_row) for col in range(max_col))))
print('time: {}'.format(timeit.default_timer() - start))


start = timeit.default_timer()

current_idx = 0
seat_state = [[[initial_state[row][col], None, []] for col in range(max_col)] for row in range(max_row)]
# each entry in seat_state is a list of [current value, next value, list(adjacent chairs)]


def get_adjacent(row, col, drow, dcol, state):
    while True: 
        row, col = row + drow, col + dcol
        if not (-1 < row < max_row and -1 < col < max_col):
            return None
        seat = state[row][col]
        if seat[0] != '.':
            return seat

# create links to adjacent seats
for row in range(max_row):
    for col in range(max_col):
        seat = seat_state[row][col]
        if seat[0] == '.':
            continue
        adjacent = (get_adjacent(row, col, drow, dcol, seat_state) for drow in range(-1, 2) for dcol in range(-1, 2) if not (drow == 0 and dcol == 0))
        seat[2] = [s for s in adjacent if s is not None]


def next_state2(state):
    idx = False
    while True:
        for row in range(max_row):
            for col in range(max_col):
                seat = state[row][col]
                if seat[idx] == '.':
                    seat[not idx] = '.'
                    continue
                num_occupied = sum(s[idx] == '#' for s in seat[2])
                if seat[idx] == 'L' and num_occupied == 0:
                    seat[not idx] = '#'
                elif seat[idx] == '#' and num_occupied >= 5:
                    seat[not idx] = 'L'
                else:
                    seat[not idx] = seat[idx]
        idx = not idx
        yield

for _ in next_state2(seat_state):
    if all(seat_state[row][col][0] == seat_state[row][col][1] for row in range(max_row) for col in range(max_col)):
        break

print('part 2: {}'.format(sum(seat_state[row][col][0] == '#' for row in range(max_row) for col in range(max_col))))
print('time: {}'.format(timeit.default_timer() - start))
