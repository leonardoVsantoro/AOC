# --- Day 14: Restroom Redoubt ---

import re
from tqdm import tqdm # type: ignore
filename = 'input_14.txt';  WIDE = 101; TALL = 103
# filename = 'test_14.txt';  WIDE = 11; TALL = 7

data = []
for line in open(filename).read().splitlines():
    c, r, dc, dr = list(map(int, re.findall(r'-?\d+', line)))
    data.append((c,r,dc,dr))

def elapse(num_steps=1):
    return [((r + num_steps*dr)%TALL, (c + num_steps*dc)%WIDE) for c,r,dc,dr in data]

def get_quadrant(r,c, WIDE = WIDE, TALL = TALL):
    if c < WIDE//2 and r < TALL//2: return 1
    elif c < WIDE//2 and r > TALL//2: return 2
    elif c > WIDE//2 and r < TALL//2: return 3
    elif c > WIDE//2 and r > TALL//2: return 4
    else: return None

def get_safety_factor(num_steps=1):
    sf = 1
    robots_in_quadrant = {quadrant : 0 for quadrant in range(0,5)} 
    for endr, endc in elapse(num_steps):
        quadrant = get_quadrant(endr,endc)
        if quadrant: robots_in_quadrant[quadrant] +=1
    for quadrant in range(1,5):
        sf *= robots_in_quadrant[quadrant]
    return sf
p1 = get_safety_factor(100)
print(f'Part 1: {p1}')

import math# type: ignore
periods = [ math.lcm( WIDE // math.gcd(dc, WIDE), TALL // math.gcd(dr, TALL)) for c,r,dc,dr in data] 

p2 = None; min_sf = p1
for i in tqdm(range(max(periods))):
    sf = get_safety_factor(i)
    if sf < min_sf:
        p2 = i; min_sf = sf 
print(f'Part 2: {p2}')

from scipy.stats import entropy as get_entropy# type: ignore
p2 = None; max_entropy = -1
for i in tqdm(range(max(periods))):
    configuration = set(elapse(i))
    encoded = [1 if (r,c) in configuration else 0 for r in range(TALL) for c in range(WIDE)] 
    entropy = get_entropy(encoded)
    if entropy > max_entropy:
        p2 = i; max_entropy = entropy
print(f'Part 2: {p2}')

# i= p2; configuration = set(elapse(data,TIME = i))
# dummyconf = [['.' for _ in range(WIDE)]  for _ in range(TALL)]
# for i, j in configuration:
#     dummyconf[i][j] = 'X'
# for row in dummyconf:
#     print(''.join(row))
