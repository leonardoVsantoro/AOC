# --- Day 13: Claw Contraption ---

# filename = 'test_13.txt'
filename = 'input_13.txt'
import re
import numpy as np # type: ignore

p1, p2 = 0, 0 
for configuration in open(filename).read().split('\n\n'):
    dx_A, dx_B, dy_A, dy_B, xp, yp =  list(map(int, re.findall(r'\d+', configuration)))
    A_mat = [[dx_A, dx_B], [dy_A, dy_B]]
    y_vec = [ xp,yp]

    solution = np.round(np.linalg.solve(A_mat, y_vec))
    if np.allclose(A_mat @ solution, y_vec) and all(solution >= 0):
        p1 += sum([solution[0] * 3 + solution[1]])

    y_vec = [ 10000000000000 + xp, 10000000000000 + yp] 
    solution = np.round(np.linalg.solve(A_mat, y_vec))
    if np.allclose(A_mat @ solution, y_vec,  rtol=1e-15) and all(solution >= 0):
        p2 += sum([solution[0] * 3 + solution[1]])

print(f'part 1: {int(p1)}')
print(f'part 2: {int(p2)}')



