filename = 'test_19.txt'
filename = 'input_19.txt'

_ = open(filename).read().split('\n\n')
available_patterns_in = _[0].split(', ')
desired_designs_in = _[1].splitlines()

def can_create_design(design, available_patterns):
    if len(design)==0:
        return True
    for pattern in available_patterns:
        if pattern == design[:len(pattern)]:
            if can_create_design(design[len(pattern):],available_patterns):
                return True
    return False  

reduced_available_patterns = []
for pattern in available_patterns_in:
    available_patterns_tocheck = available_patterns_in.copy()
    available_patterns_tocheck.remove(pattern)
    if not can_create_design(pattern, available_patterns_tocheck):
        reduced_available_patterns.append(pattern)

p1 = sum([can_create_design(design,reduced_available_patterns) for design in desired_designs_in])
print(f'part 1: {p1}')


from functools import lru_cache
@lru_cache
def get_design_combs(design):
    count = 0
    if len(design)==0:
        count +=1 
    for pattern in available_patterns_in:
        if pattern == design[:len(pattern)]:
            count += get_design_combs(design[len(pattern):])      
    return count  

p2 = sum([get_design_combs(design) for design in desired_designs_in])
print(f'part 2: {p2}')


