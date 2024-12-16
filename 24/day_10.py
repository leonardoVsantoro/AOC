# filename = 'test_10.txt'
filename = 'input_10.txt'

data = [list(map(int, line)) for line in open(filename).read().splitlines()]
nrows = len(data)
ncols = len(data[0])

def get_neighbours(loc):
    x,y = loc
    nbrs = []
    current_height = data[x][y]
    if x+1 < ncols:
        if current_height + 1 == data[x+1][y]:
            nbrs.append((x+1,y))
    if x-1 >= 0:
        if current_height + 1 == data[x-1][y]:
            nbrs.append((x-1,y))
    if y+1 < nrows:
        if current_height + 1 == data[x][y+1]:
            nbrs.append((x,y+1))
    if y-1 >= 0:
        if current_height + 1 == data[x][y-1]:
            nbrs.append((x,y-1))
    return nbrs

start_locs = [(i,j) for i in range(ncols) for j in range(nrows) if data[i][j] == 0]
top_locs = [(i,j) for i in range(ncols) for j in range(nrows) if data[i][j] == 9]

def reaches_top(data, start_loc, top_loc):
    nbrs = get_neighbours(start_loc)
    if len(nbrs) == 0:
        return False
    elif top_loc in nbrs:
        return True
    else:
        return any([reaches_top(data, nbr, top_loc) for nbr in nbrs]) 

part1 = 0
for loc in start_locs:
    for top_loc in top_locs:
        part1 += int(reaches_top(data, loc, top_loc))
print(f'part 1 : {part1}')


def find_all_trails(start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in get_neighbours(start):
        new_paths = find_all_trails(neighbor, end, path)
        for p in new_paths:
            paths.append(p)
    return paths


alltrails = set()
for start_loc in start_locs:
    for top_loc in top_locs:
        trails = find_all_trails(start_loc, top_loc)
        for path in trails:
            alltrails.add(tuple(path))
part2 = len(alltrails)
print(f'part 2: {part2}')
