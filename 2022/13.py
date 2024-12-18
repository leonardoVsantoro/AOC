import ast
data = open('input_13.txt').read().strip().split("\n\n")

def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            return (a > b) - (a < b)
        return compare([a], b)
    if type(b) == int:
        return compare(a, [b])
    for aa, bb in zip(a, b):
        if r := compare(aa, bb):
            return r
    return compare(len(a), len(b))

_raveled_data = []
scores = []
for ix in range(len(data)):
    L,R = data[ix].split('\n'); L, R = ast.literal_eval(L), ast.literal_eval(R)
    scores.append(compare(L,R))
    _raveled_data.append(L); _raveled_data.append(R)
scores = np.array(scores)

part1 = (np.where(scores==-1)[0] +1).sum()
print('Part 1: {}'.format(part1))

# ====

_raveled_data.append([[2]]); _raveled_data.append([[6]])
# _raveled_data.sort(key=cmp_to_key(compare))

part2 = 1
for i, p in enumerate(_raveled_data):
        if p == [[2]]:
            part2 *= i + 1
        if p == [[6]]:
            part2 *= i + 1
print('Part 1: {}'.format(part2))
