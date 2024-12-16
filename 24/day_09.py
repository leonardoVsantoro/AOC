import math
# filename = 'test_09.txt'
filename = 'input_09.txt'
data = list(map( int,  open(filename).read()))

occupied = [x for i,x in enumerate(data) if i % 2 == 0]
empty = [x for i,x in enumerate(data) if i % 2 == 1] + [0]

resolved = {}
for i, (oc, em)  in enumerate(zip(occupied,empty)):
   resolved[i]  =  {i : oc, 'empty' : em}



n_drives = len(resolved)
j = n_drives - 1 
i = 0
while j > i:
   while resolved[i]['empty'] > 0 :
      if j <= i:
         break
      elif resolved[j][j] != 0:
         can_move = min(resolved[j][j], resolved[i]['empty'])
         resolved[i].update( {j : can_move})    
         resolved[j][j] -=  can_move
         resolved[i]['empty']-= can_move
      else:
         j-=1
         
   del resolved[i]['empty']  
   i += 1


string = []
for i in resolved.keys():
   for key in resolved[i].keys():
      if key != 'empty':
         string += [key] * resolved[i][key]
   
part1 = 0
for i, el in enumerate(string):
   part1 += el * i

print(f'part 1: {part1}')
# print(f'part 2: {part2}')



resolved = {}
for i, (oc, em)  in enumerate(zip(occupied,empty)):
   resolved[i]  =  {i : oc, 'emptyL' :0, 'emptyR' : em}

n_drives = len(resolved)
i = 0

for j in list(resolved.keys())[::-1]:
    size_to_move = resolved[j][j]
    possible_moves_to = [resolved[key]['emptyR'] >=  size_to_move for key in list(resolved.keys()) if key < j]
    if any(possible_moves_to):
        move_to = possible_moves_to.index(True)
        resolved[move_to].update( {j : size_to_move})
        del resolved[j][j]
        resolved[j]['emptyL'] += size_to_move
        new_empty = resolved[move_to]['emptyR']- size_to_move
        del resolved[move_to]['emptyR']
        resolved[move_to].update({'emptyR': new_empty})

string = []
for i in resolved.keys():
    for key in resolved[i].keys():
        if isinstance(key, int):
            string += [key] * resolved[i][key]
        else:
            string += [0] * resolved[i][key]
part2 =     0
for i, el in enumerate(string):
    part2 += el * i

print(f'part 2: {part2}')

