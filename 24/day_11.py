filename = 'input_11.txt'
# filename = 'test_11.txt'
data = list(map(int, open(filename).read().split()))


def change(num):
    if num == 0:
        return [1]
    length = len(str(num))
    if length%2 == 0:
        return [int(str(num)[:length//2]), int(str(num)[length//2:])]
    else:
        return [int(num*2024)]
    
def solve(data, num_blinks):
    for blink in range(num_blinks):
        new_data = []
        for stone in data:
            new_data += change(stone)
        data = new_data
    return len(data)

num_blinks = 25
part1 = solve(data, num_blinks)
print('part 1:', part1)

from collections import defaultdict
def smarter_solve(data_counter):
    updated_counter = defaultdict(int)
    for stone in list(data_counter.keys()):
        for new_stone in change(stone):
            updated_counter[new_stone] += data_counter[stone]
    return updated_counter

from collections import Counter
updated_counter = Counter(data)  
num_blinks = 75
for _ in range(num_blinks):
    updated_counter = smarter_solve(updated_counter)
part2 = sum(updated_counter.values())
print('part 2:', part2)



