import sys

numbers = [int(line.strip()) for line in sys.stdin]

invalid = next((num for idx, num in enumerate(numbers[25:]) if not any(((num - x) in numbers[idx:25+idx]) for x in numbers[idx:25+idx])))

print(f'part 1: {invalid}')

start, end = 0, 1
while end < len(numbers):
    sub_sum = sum(numbers[start:end])
    if sub_sum == invalid:
        break
    if sub_sum < invalid:
        end += 1
    else:
        start += 1

smallest, largest = min(numbers[start:end]), max(numbers[start:end])
print('part 2: {}'.format(smallest + largest))
