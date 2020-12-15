import sys

starting_numbers = [int(x) for x in sys.stdin.readline().strip().split(',')]


def spoken_after(n, starting_numbers):
    history = dict()
    for turn, num in enumerate(starting_numbers[:-1]):
        history[num] = turn
    
    turn += 1
    last_num = starting_numbers[-1]
    while turn < n - 1:
        next_num = turn - history.get(last_num, turn)
        history[last_num] = turn 
        turn += 1
    
        last_num = next_num
    return last_num



print('part 1: {}'.format(spoken_after(2020, starting_numbers)))
print('part 2: {}'.format(spoken_after(30000000, starting_numbers)))
