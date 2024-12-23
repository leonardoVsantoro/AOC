from collections import defaultdict, deque

filename = 'input_18.txt'; size = 70

locs = [] 
for line in open(filename).read().splitlines(): 
    vals = list(map(int, line.split(','))) 
    locs.append((vals[1], vals[0]))


def shortest_path(start, end, n_fallen):
    setlocs= set(locs[:n_fallen])
    nbrs = defaultdict(list)
    for i in range(size +1):
        for j in range(size +1):
            for ni, nj in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if (ni, nj) not in setlocs:
                    if 0 <= ni <= size and 0 <= nj <= size:
                        nbrs[(i,j)].append((ni,nj))
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        (current, path) = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        for neighbor in nbrs[current]:
            if neighbor == end:
                return True, path + [end]
            else:
                queue.append((neighbor, path + [neighbor]))

    return False, []

# Example usage:
start = (0, 0); end = (size, size)
reachable, path = shortest_path(start, end, 1024)
p1 = len(path) - 1
print(f'Part 1: {p1}')

for n_fallen in range(370, len(locs)):
    reachable, path = shortest_path(start, end, n_fallen)
    if not reachable:
        p2 = (locs[n_fallen-1][1], locs[n_fallen-1][0])
        break
print(f'Part 2: {p2}')
