from collections import deque, defaultdict

# filename = 'test_20.txt'
filename = 'input_20.txt'
data = open(filename).read().splitlines()

nrows, ncols = len(data), len(data[0])
nbrs = defaultdict(list)
for i in range(nrows):
    for j in range(ncols):
        if data[i][j] == 'S': start = (i,j)
        if data[i][j] == 'E': end = (i,j)
        for di,dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            if 0 <= i+di < nrows and 0 <= j+dj < ncols and data[i+di][j+dj] != '#': 
                nbrs[(i,j)].append((i+di,j+dj))

def bfs_shortest_path(start, end, nbrs):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (current, path) = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        for neighbor in nbrs[current]:
            if neighbor == end:
                return path + [end]
            else:
                queue.append((neighbor, path + [neighbor]))        
    return None

def solve(timegap, saved):
    track = bfs_shortest_path(start, end, nbrs); 
    out = 0
    for ix, node in enumerate(track):
        for jumptoix, jumptonode in enumerate(track[ix+1:]):
            cheatlenght = abs(jumptonode[0] - node[0]) + abs(jumptonode[1] - node[1])
            if cheatlenght <= timegap:
                gained = jumptoix - cheatlenght + 1 
                if gained >= saved:
                    out +=1
    return out

p1 = solve(2,100)
print(f'Part 1 : {p1}')

p2 = solve(20,100)
print(f'Part 1 : {p2}')
