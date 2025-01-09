# filename = 'test25.txt'
filename = 'input25.txt'

keys = []
locks = []
for data in [_.splitlines() for _ in open(filename).read().split('\n\n')]:
    if data[0] == ''.join(['.']*len(data[0])):
        keys.append(data)
    elif data[0] == ''.join(['#']*len(data[0])):
        locks.append(data)
depth = len(data)

def get_enc(data):
    heights = []
    for j in range(len(data[0])):
        for i in range(len(data)):
            if data[i][j] != '#':
                heights.append(i-1)
                break
    return heights

enc_keys = [get_enc(data[::-1]) for data in keys]
enc_locks = [get_enc(data) for data in locks]

def are_compatible(key, lock):
    sums = [k + l for k, l in zip(key, lock)]
    return max(sums) < depth -1

p1 = 0
for key in enc_keys:
    for lock in enc_locks:
        if are_compatible(key, lock):
            p1 +=1
print(p1)

# and part 2 comes for free :) 
