# --- Day 6: Guard Gallivant ---

# filename = 'test_06.txt'
filename = 'input_06.txt'
data = [list(line.strip()) for line in open(filename)]
n = len(open(filename).read().splitlines())

for i, row in enumerate(data):
    if '^' in row:
        init_point = ((i, row.index('^')))
        break

def rotate_data_counterclockwise(matrix,k):
    for _ in range(k % 4):
        matrix = [list(row) for row in list(zip(*matrix))[::-1]]
    return matrix
    
def rotate_position_clockwise(loc, k):
    i,j = loc
    for _ in range(k % 4):
        i, j = j, n - 1 - i
    return (i, j)

def main(input_data):
    rotated_datas = [rotate_data_counterclockwise(input_data, k) for k in range(4)]
    k = 0
    start = init_point
    visited = set()
    while True:
        rotated_data = rotated_datas[k].copy()
        first_obstacle = ''.join([rotated_data[i][start[1]] for i in range(start[0])]).rfind('#')
        for i in range(first_obstacle, start[0]):
            newloc = (rotate_position_clockwise((i+1, start[1]), k), k)
            if newloc in visited:
                return True, visited
            visited.add(newloc)
        if first_obstacle == -1:
            return False, visited
        start = rotate_position_clockwise(( first_obstacle + 1, start[1] + 1 ), 3)
        k = k+1; k = k % 4

input_data = [list(line.strip()) for line in open(filename)]
visited_locs = set( _[0] for _ in main(input_data)[1])
part_1 = len(visited_locs)
print('part 1: {}'.format(part_1))

part_2 = 0
from tqdm import tqdm # type: ignore
for i, j in tqdm(visited_locs):
    input_data = [list(line.strip()) for line in open(filename)]
    input_data[i][j] = '#'
    has_loop, visited = main(input_data)
    if has_loop:
        part_2 += 1

        # input_data[i][j] = 'O'
        # for i, j in set( [_[0] for _ in visited]):    
        #     input_data[i][j] = 'X'
        # input_data[init_point[0]][init_point[1]] = '^'
        # print(pd.DataFrame(input_data))
        # print('')


print('part 2: {}'.format(part_2))



