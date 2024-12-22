import re
from collections import deque
from functools import lru_cache


keypad = {'7' :(0,0), '8':(0,1), '9':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '1':(2,0), '2':(2,1), '3':(2,2), '0' : (3,1), 'A': (3,2)}
joypad = {'^': (0,1), '<': (1,0), '>': (1,2), 'v': (1,1), 'A':(0,2)}
manh_dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
nbrs_keypad = {key: [keynbr for keynbr in keypad.keys() if manh_dist(keypad[keynbr], keypad[key]) == 1] for key in keypad.keys()}
nbrs_joypad = {key: [keynbr for keynbr in joypad.keys() if manh_dist(joypad[keynbr], joypad[key]) == 1] for key in joypad.keys()}
steps_from_path = {(1,0) : 'v', (-1,0) : '^', (0,1) : '>', (0,-1) : '<'}


def travel_all(start, end, pad = keypad, nbrs = nbrs_keypad):
    def dfs(current, path):
        if current == end:
            steps = [steps_from_path[(pad[path[i+1]][0] - pad[path[i]][0], pad[path[i+1]][1] - pad[path[i]][1])] for i in range(len(path)-1)]
            all_steps_sequences.append(steps)
            return
        for neighbor in nbrs[current]:
            if neighbor not in path:
                dfs(neighbor, path + [neighbor])
    all_steps_sequences = []
    dfs(start, [start])
    minlen = min([len(steps) for steps in all_steps_sequences])
    all_steps_sequences = [steps + ['A'] for steps in all_steps_sequences if len(steps) == minlen]
    return all_steps_sequences

@lru_cache
def get_countcode(current, target, n_robots):
    if n_robots ==1:
        pos_current = joypad[current]
        pos_target = joypad[target]
        dx = pos_target[0] - pos_current[0]
        dy = pos_target[1] - pos_current[1]
        return dx + dy +1
    else:
        lower_layer_possible_commands = [ ['A'] + _  for _ in travel_all(current, target, pad = joypad, nbrs = nbrs_joypad)]
        return min([ sum([get_countcode(_c,_t, n_robots-1) for _c,_t in zip(lower_layer_command, lower_layer_command[1:])]) 
                    for lower_layer_command in lower_layer_possible_commands])

def elapse(code, n_robots = 2, debug = False):
    current_key = 'A'
    min_len = 0
    for key in code:
        keypadSequences = travel_all(current_key, key)
        current_key = key
        last_layer_lens = []
        for sequence in keypadSequences:
            sequence = ['A'] + sequence
            last_layer_lens.append( sum([get_countcode(_c,_t, n_robots+1) for _c,_t in zip(sequence, sequence[1:])]) )
        min_len += min(last_layer_lens)
    return min_len

def main(filename, n_robots = 2):
    data = open(filename).read().splitlines()
    out = 0
    for code in data:
        num_part = list(map(int, re.findall(r'-?\d+', code)))[0]
        len_commands = elapse(code, n_robots)
        out += len_commands*num_part
    return out



filename = 'input_21.txt'
p1 = main(filename, 2)
print(f'part 1 : {p1}')

p2 = main(filename, 25)
print(f'part 1 : {p2}')



