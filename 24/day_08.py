# --- Day 8: Resonant Collinearity ---

from itertools import combinations
import math

# filename = 'test_08.txt'
filename = 'input_08.txt'

data = [list(line.strip()) for line in open(filename)]
n = len(data)

occupied = set()
frequencies = set(_ for row in data for _ in row); frequencies.discard('.')
for freq in frequencies:
    syn_data = [[_ if _ == freq else '.' for _ in row] for row in data]
    antennas_locs = [(i, j) for i,row in enumerate(syn_data) for j,el in enumerate(row) if el == freq]
    for (loc1, loc2) in list(combinations(antennas_locs, 2)):
        vec = (loc2[0] - loc1[0], loc2[1] - loc1[1])
        antinodes = [(loc1[0] + 2*vec[0], loc1[1] + 2*vec[1]),(loc2[0] - 2*vec[0], loc2[1] - 2*vec[1]) ]
        for _ in antinodes:
            if 0 <= _[0] < n and 0 <= _[1] < n:
                occupied.add(_)

part1 = len(occupied)
print(f'part 1: {part1}')


occupied = set()
frequencies = set(_ for row in data for _ in row); frequencies.discard('.')
for freq in frequencies:
    syn_data = [[_ if _ == freq else '.' for _ in row] for row in data]
    antennas_locs = [(i, j) for i,row in enumerate(syn_data) for j,el in enumerate(row) if el == freq]
    for (loc1, loc2) in list(combinations(antennas_locs, 2)):
        for loc1,loc2 in [(loc1, loc2), (loc2, loc1)]:
            vec = (loc2[0] - loc1[0], loc2[1] - loc1[1])
            normvec = (vec[0]// math.gcd(vec[0], vec[1]), vec[1]// math.gcd(vec[0], vec[1]) )
            k = 0
            while True:
                antinode = (loc2[0] + k*normvec[0], loc2[1] + k*normvec[1])
                if antinode[0] < 0 or antinode[0] >= n or antinode[1] < 0 or antinode[1] >= n:
                    break
                occupied.add(antinode)
                k += 1

part2 = len(occupied)
print(f'part 2: {part2}')

