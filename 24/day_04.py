# --- Day 4: Ceres Search ---

# filename = 'test_04.txt'
filename = 'input_04.txt'
# 
data = open(filename).read().splitlines()

get_square_locs = lambda i, j: [[( i + m , j +k)  for m in range(4)] for k in range(4)] \
            + [[( i + k, j +k) for k in range(4)]] \
            + [[( i + 3 - k, j +k ) for k in range(4)]] \
            + [[( i + m , j + k)  for k in range(4)] for m in range(4)] 

part_1 = 0
all_locs_with_XMAS = []
for i in range(len(data) - 3):
    for j in range(len(data[0]) - 3):            
        for locs in  get_square_locs(i, j):
            word = ''.join([data[_i][_j] for _i, _j in locs])
            if (word == 'XMAS' or word == 'SAMX') and (locs not in all_locs_with_XMAS):
                part_1 += 1
                all_locs_with_XMAS.append(locs)
print(f'part 1: {part_1}')


part_2 = 0
for i in range(len(data) - 2):
    for j in range(len(data[0]) - 2):            
        word1 = ''.join([data[_i][_j] for _i, _j in [( i + k, j + k) for k in range(3)]])
        word2 = ''.join([data[_i][_j] for _i, _j in [( i + 2 - k, j + k ) for k in range(3)]])
        if word1 == 'MAS' or word1 == 'SAM':
            if word2 == 'MAS' or word2 == 'SAM':
                part_2 += 1
print(f'part 2: {part_2}')
