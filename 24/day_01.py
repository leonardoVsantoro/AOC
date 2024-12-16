import numpy as np # type: ignore

filename = 'input_01.txt'
# filename = 'test_01.txt'

data = [line.split() for line in open(filename).read().strip().split("\n")]
data = np.array([[int(num) for num in row] for row in data])
first_list = np.sort(data[:,0])
second_list =  np.sort(data[:,1])

part_1 = np.abs(first_list - second_list).sum()
print(f'part 1: {part_1}')

# =============================================================================

part_2 = 0
for el in first_list:
    part_2 += np.sum(second_list == el)*el
print(f'part 2: {part_2}')