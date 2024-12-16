# --- Day 15: Warehouse Woes ---
# filename = 'input_15.txt'
filename = 'test_15.txt'  

first_in, second_in = open(filename).read().split('\n\n')
moves_in = [move for line in second_in.splitlines() for move in line ]
field_in = [[char for char in line] for line in first_in.splitlines()]

def get_robot_pos(field):  
    for i, line in enumerate(field):
        for j, char in enumerate(line):
            if char == '@': 
                return (i,j) 
move_to_incr = {'<' : (0,-1), '>' : (0,1), '^' : (-1,0), 'v' : (1,0)}

def elapse(field, move, pos):
    if field is None:
        field = [[char for char in line] for line in first_in.splitlines()]
    i, j = pos
    incr = move_to_incr[move]
    next_i, next_j = i + incr[0], j + incr[1]
    while field[next_i][next_j] == 'O':
        newfield = elapse(field, move, (next_i, next_j))
        if field == newfield:
            break
        else:
            field = newfield
        next_i, next_j = i + incr[0], j + incr[1]
    if field[next_i][next_j] == '.':
        field[next_i][next_j] = field[i][j]
        field[i][j] = '.'
    return field


robot_pos = get_robot_pos(field_in)
newfield = None
for move in moves_in:
    newfield = elapse(newfield,move, robot_pos)
    robot_pos = get_robot_pos(newfield)
p1 = 0
for i,line in enumerate(newfield):
    for j,char in enumerate(line):
        if char == 'O':
            p1 += i*100 + j
print(f'part 1 : {p1}')



# ===== part 2 =====

def the_other_pos(field, move, pos):
    i,j = pos
    chr = field[i][j]
    if (chr, move) in [('[', '^'), ('[', 'v')]:
        return (i, j + 1)
    if (chr, move) in [(']', '^'), (']', 'v')]:
        return (i, j - 1)
    else:
        return (i, j)
    
def can_move(field, move, pos, visited=None):
    if visited is None:
        visited = set()  
    i, j = pos
    visited.add(pos) 
    incr = move_to_incr[move]
    next_i, next_j = i + incr[0], j + incr[1]
    next_pos = (next_i, next_j)
    if field[next_i][next_j] == '.':
        return True, visited
    if field[next_i][next_j] == '#':
        return False, visited
    if field[next_i][next_j] in ['[', ']']:
        if move in ['<', '>']:
            result, visited = can_move(field, move, next_pos, visited)
            return result, visited
        else:
            result1, visited = can_move(field, move, next_pos, visited)
            result2, visited = can_move(field, move, the_other_pos(field, move, next_pos), visited)
            return result1 and result2, visited

duplicate_char = {'#': ['#', '#'],  'O' : ['[', ']'], '.': ['.', '.'], '@': ['@', '.']}
def elapse(field, move, pos):
    if field is None:
        field = [[_ for char in line for _ in duplicate_char[char]] for line in first_in.splitlines()]  
    go, visited = can_move(field, move, pos)
    if go: 
        dx,dy = move_to_incr[move]
        newfield = [[char for char in line] for line in field]
        for x,y in visited:
            newfield[x][y] = '.'
        for x,y in visited:
            newfield[x + dx][y + dy] = field[x][y]
        field = newfield
    return field
    

duplicate_field_in = [[_ for char in line for _ in duplicate_char[char]] for line in first_in.splitlines()]  
robot_pos = get_robot_pos(duplicate_field_in)
newfield = None
for move in moves_in:
    newfield = elapse(newfield,move, robot_pos)
    robot_pos = get_robot_pos(newfield)

p2 = 0
for i,line in enumerate(newfield):
    for j,char in enumerate(line):
        if char == '[':
            p2 += i*100 + j
print(f'part 2 : {p2}')