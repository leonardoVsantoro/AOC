
import sympy # type: ignore
filename = 'input24.txt'

wire_in, rules_in = open(filename).read().split('\n\n')
wires = {line.split(': ')[0] : int(line.split(': ')[1]) for line in wire_in.splitlines()}
wires_sym = {wire: sympy.symbols(wire) for wire in wires.keys()}

rules = dict()
for line in rules_in.splitlines():
    inop = line.split(' -> ')[0].split(' ')
    rules[line.split(' -> ')[1]] = ( inop[0], inop[2], inop[1])


from collections import deque
def computez(wires, rules):
    def do_op(in1, in2, op):
        if op == 'AND': return wires[in1] & wires[in2]
        elif op == 'OR': return wires[in1] | wires[in2]
        elif op == 'XOR': return wires[in1] ^ wires[in2]
        else: return None
    tosee = deque(rules.keys())
    while tosee:
        z = tosee[-1]
        in1, in2, op = rules[z]
        if in1 in wires and in2 in wires:
            wires[z] = do_op(*rules[z])
            tosee.pop()
        else:
            tosee.extend([_ for _ in rules[z][:2] if _ not in wires])
    return wires

reconstructed = computez(wires, rules)
all_zwires = [_ for _ in rules if _[0]=='z']; all_zwires.sort(reverse=True)
p1 = int( ''.join([str(int(reconstructed[z])) for z in all_zwires ]), 2)
print(f'Part 1: {p1}')

def lookforvalue(thevaluetolookfor):
    for w in sym_out:
        if sym_out[w] == thevaluetolookfor:
            return w

all_zwires = [_ for _ in rules if _[0]=='z']; all_zwires.sort(reverse=False)  
touched = []
while True:
    sym_out = computez(wires_sym, rules)
    carry = False
    for i,z in enumerate(all_zwires):
        sym_out = computez(wires_sym, rules)
        try:
            _x =  sym_out['x{}'.format(str(i).zfill(2))]
            _y =  sym_out['y{}'.format(str(i).zfill(2))]
        except:
            _x = False; _y = False
        shouldbez = (_x ^ _y) ^ carry
        oldcarry = carry
        carry = (_x & _y) | (carry & (_x ^ _y))

        if sym_out[z] != shouldbez:
            # print(f'Error at {z}')
            if 'XOR' == rules[z][2]:
                current = set([rules[z][0], rules[z][1]])
                w0 = lookforvalue(_x ^ _y); w1 = lookforvalue(oldcarry)
                if w0 is not None and w1 is not None:
                    ws = set([w1, w0])
                    ws, current = ws - current, current - ws
                    for w,c in zip(ws, current):
                        rules[w], rules[c] = rules[c], rules[w]
                        touched += [(w,c)]
                        # print('switched {} with {}'.format(c,w))
                    break
            else:
                w = lookforvalue(shouldbez)
                if w is not None:
                    rules[w], rules[z] =  rules[z], rules[w]
                    touched += [(w,z)]
                    # print('switched {} with {}'.format(z,w))
                    break
            
    if i  == len(all_zwires)-1:
        break

sorted_wires = sorted(set(sum(touched, ())))
p2 = ','.join(sorted_wires)
print('Part 2 : {}'.format(p2))

