filename= 'input23.txt'
# filename= 'test23.txt'
data = [line.split('-') for line in open(filename).read().splitlines()]

from collections import defaultdict
nbrs = defaultdict(set)

for a,b in data:
    nbrs[a].add(b); nbrs[b].add(a)

loops_of_len_3 = set()
for startnode in nbrs:
    for neigh_1 in nbrs[startnode]:
        for neigh_2 in nbrs[neigh_1]:
            if startnode in nbrs[neigh_2]:
                loop = frozenset([startnode, neigh_1, neigh_2])
                if any( [_.startswith('t') for _ in loop]):
                    loops_of_len_3.add(loop)

p1 = len(loops_of_len_3)
print('Part 1:', p1)


def bron_kerbosch(R, P, X):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(R.union([v]), P.intersection(nbrs[v]), X.intersection(nbrs[v]))
        X.add(v)

max_clique = max(bron_kerbosch(set(), set(nbrs.keys()), set()), key=len)
p2 = sorted(max_clique)
print('Part 2:', ','.join(p2))