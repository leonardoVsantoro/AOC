# --- Day 17: Chronospatial Computer ---
import re
filename = "input_17.txt"
# filename = "test_17.txt"
data = open(filename).read().split('\n\n')
programs = list(map(int, re.findall(r'-?\d+', data[1])))
register_values_in = list(map(int, re.findall(r'-?\d+', data[0])))


def combo(val, registers):
    if val in {0,1,2,3}:
        return val
    if val == 4:
        return registers['A']
    if val == 5:
        return registers['B']
    if val == 6:
        return registers['C']
    else:
        return None
    
def compute(opcode, registers, val):
    jumps = False
    outval = None
    if opcode == 0:
        registers['A'] = registers['A'] // 2**combo(val, registers)
    if opcode == 1:
        registers['B'] = registers['B'] ^ val
    if opcode == 2:
        registers['B'] = combo(val, registers) % 8
    if opcode == 3:
        if registers['A'] != 0:
            jumps = True
    if opcode == 4:
        registers['B'] = registers['B'] ^ registers['C']
    if opcode == 5:
        outval = combo(val, registers)%8
    if opcode == 6:
        registers['B'] =  registers['A'] // 2**combo(val, registers)
    if opcode == 7:
        registers['C'] = registers['A'] // 2**combo(val, registers)
    return outval, jumps, registers

def elapse(newA = None):
    registers = {key : val for key, val in zip('ABC', register_values_in)}
    if newA is not None:
        registers['A'] = newA
    op_index = 0
    outvals = []
    while True:
        # print(registers)
        if op_index >= len(programs)-1:
            break
        opcode = programs[op_index]
        literal_operand =programs[op_index+1]
        outval, jumps, registers = compute(opcode, registers, literal_operand)
        if outval is not None:
            for _ in str(outval):
                outvals.append(int(_)) 
        if jumps:
            op_index = literal_operand
        else:
            op_index += 2
    return outvals
                    
p1 = ','.join(map(str, elapse()))
print('part 1 : ' + p1)

to_check = set(range(8))
for k in range(1, len(programs)+1):
    if to_check == set(): break
    target = programs[-k:]
    new_check = set()
    for candidate in to_check:
        lower = candidate*8; upper = (candidate +1 )*8 
        for x in range(lower, upper):
            if elapse(x) == target:
                new_check.add(x)
    to_check = new_check

p2 = min(to_check) 
print(f'part 2 : {p2}')

