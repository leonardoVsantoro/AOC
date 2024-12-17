# filename = 'test_03.txt'
filename = 'input_03.txt'

def find_first_closed_bracket(string):
    for i, char in enumerate(string):
        if char == ')':
           return i
    return None

part_1 = 0
mycandidate = None
for candidate in  ['do'] + open(filename).read().split('mul(')  :
    candidate = candidate[:find_first_closed_bracket(candidate)]
    split_candidate = candidate.split(',')
    if len(split_candidate)==2:
        try:
            prod = int(split_candidate[0]) * int(split_candidate[1])
            part_1 +=prod
        except:
            pass
print(f'part 1 : {part_1}')

part_2 = 0
skip_next = False
for candidate in  ['do'] + open(filename).read().split('mul(')  :
    split_candidate = candidate[:find_first_closed_bracket(candidate)].split(',')
    if len(split_candidate)==2:
        try:
            prod = int(split_candidate[0]) * int(split_candidate[1])
            if not skip_next:
                part_2 +=prod
        except:
            pass
    if candidate.rfind("do()") < candidate.rfind("don't()"):
        skip_next = True
        continue
    if candidate.rfind("do()") > candidate.rfind("don't()"):
        skip_next = False
        continue

print(f'part 2 : {part_2}')