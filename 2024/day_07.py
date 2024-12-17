# --- Day 7: Bridge Repair ---

# filename = 'test_07.txt'
filename = 'input_07.txt'

all_target = []
all_parts = []

with open(filename) as file:
    for row in file:
        target, parts = row.split(': ')
        all_target.append(int(target))
        all_parts.append(list(map(int, parts.split())))

from itertools import product

def do_operation(a,b,symbol):
    if symbol == '+':
        return a+b
    elif symbol == '*':
        return a*b
    elif symbol == '|':
        return int(str(a) + str(b))
    
from collections import deque 

def main(all_target, all_parts, all_combinations):
    result = 0
    for target, parts, combinations in zip(all_target, all_parts, all_combinations):
        for one_combination in combinations:
            dequed_parts, dequed_combination = deque(parts), deque(one_combination)
            res = 1 if dequed_combination[0] == '*' else 0
            while len(dequed_combination)>0:
                res = do_operation(res,dequed_parts[0],dequed_combination[0]) 
                dequed_combination.popleft(); dequed_parts.popleft()
                if res > target:
                    break
            if res == target:
                result += target
                break
    return result

all_combinations_1 = [list( product('*+', repeat=len(part)))  for part in all_parts]
part_1 = main(all_target, all_parts, all_combinations_1)
print(f'part 1: {part_1}')

all_combinations_2 = [list( product('*+|', repeat=len(part)))  for part in all_parts]
part_2 = main(all_target, all_parts, all_combinations_2)
print(f'part 2: {part_2}')




