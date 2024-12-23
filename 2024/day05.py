# --- Day 5: Print Queue ---
import functools

# filename = 'test_05.txt'
filename = 'input_05.txt'

data = open(filename).read().split('\n\n')
all_printing_orders =  [_.split(',') for _ in data[1].splitlines()]
rules =  [_.split('|') for _ in data[0].splitlines()]

def get_sorting_order(a,b):
    for rule in rules:
        if a == rule[0] and b == rule[1]:
            return -1
        elif a == rule[1] and b == rule[0]:
            return 1
    return 0

part_1 = 0; part_2 = 0
for order in all_printing_orders:    
    sorted_order = sorted(order , key = functools.cmp_to_key(get_sorting_order))
    if order == sorted_order:
        part_1 +=  int(order[len(order) // 2])
    else:
        part_2 += int(sorted_order[len(sorted_order) // 2])
        
print(f'part 1: {part_1}')
print(f'part 2: {part_2}')