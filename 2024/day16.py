from collections import defaultdict, deque

filename = "input_16.txt"
# filename = "test_16.txt"

data = [[_ for _ in line] for line in open(filename).read().splitlines()]

for i,line in enumerate(data):
    for j, chr in enumerate(line):
        if chr == "S":
            start = (i,j)
        if chr == "E":
            end = (i,j)

nbrs = defaultdict(list)
for i, line in enumerate(data):
    for j, chr in enumerate(line):
        if chr != '#':
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + ii, j + jj
                if 0 <= ni < len(data) and 0 <= nj < len(data[0]) and data[ni][nj] != '#':
                    nbrs[(i, j)].append((ni, nj))

def find_best_path(nbrs, start, end):
    best_path = []
    best_score = 1e10
    opt_sequence = defaultdict(list)
    visited_score = defaultdict(int)
    queue = deque([(start, [start], (0,1), 0)])
    while queue:
        current_node, path, direction, path_score = queue.popleft()
        if current_node == end:
            if path_score <= best_score:
                best_score = path_score
                best_path = path
                opt_sequence[path_score].append(path)
            continue
        for neighbor in nbrs[current_node]:
            score = path_score
            if neighbor not in path:
                new_direction = (neighbor[0] - current_node[0], neighbor[1] - current_node[1])
                if new_direction != direction:
                    score+=1000
                score+=1
                if score-1000 <= visited_score[neighbor] or visited_score[neighbor] < 1:
                    visited_score[neighbor] = score
                    queue.append((neighbor, path + [neighbor], new_direction, score))
    if len(best_path) > 1:
        direction = (best_path[-1][0] - best_path[-2][0], best_path[-1][1] - best_path[-2][1])
        return best_score, opt_sequence
        return None, None

best_score, opt_paths = find_best_path(nbrs, start, end)
p1 = best_score
print(f'part 1: {p1}')
opt_spots = set()
for path in opt_paths[best_score]:
    opt_spots.update(set(path))
p2 = len(opt_spots) 
print(f'part 2: {p2}')
