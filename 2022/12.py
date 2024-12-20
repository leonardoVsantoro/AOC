from string import ascii_lowercase
from collections import defaultdict
import numpy as np

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) 
def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return []

filename = 'input_12.txt'

with open(filename) as fp:
    lines = fp.read().splitlines()
data = np.array([list(line) for line in lines])
_letters_to_num_ = {v:k for k,v in enumerate(ascii_lowercase)}
_letters_to_num_.update({"S":_letters_to_num_['a']});
_letters_to_num_.update({"E":_letters_to_num_['z']});


class vertex_class (object):
    def __init__(self, i,j):
            self.letter = data[i,j];
            self.height = _letters_to_num_[data[i,j]]   
            self.ix = (i,j)
    def __repr__(self):
        return self.letter
    
vertices = np.array([ vertex_class(i,j) for i in range(data.shape[0])  for j in range(data.shape[1])  ])

edges = set()
graph = defaultdict(list)

for vertex_i in vertices:
    for vertex_j in vertices:
        if  (manhattan(vertex_i.ix, vertex_j.ix) ==1):
            if (vertex_j.height - vertex_i.height) <= 1 :
                edges.add((vertex_i.ix,vertex_j.ix))

graph = defaultdict(list)
for edge in edges:
    a, b = edge[0], edge[1]; graph[a].append(b); 

            

start_vertex = [vertex.ix for vertex in vertices if  vertex.letter =='S'][0]
end_vertex = [vertex.ix for vertex in vertices if  vertex.letter =='E'][0]

sp = BFS_SP(graph, start_vertex, end_vertex); 
print('Part 1 : {}'.format(len(sp)-1)  )

start_vertices = [vertex.ix for vertex in vertices if  (vertex.height ==0 )]

_lens = [ len( BFS_SP(graph, start_vertex, end_vertex))-1 for start_vertex in start_vertices]
_lens = [_ for _ in _lens if _>= 0]
print('Part 2 : {}'.format(min(_lens))  )



# === alternative
filename = 'input_12.txt'
# filename = 'test_12.txt'

with open(filename) as fp:
    lines = fp.read().splitlines()
data = np.array([list(line) for line in lines])
_letters_to_num_ = {v:k for k,v in enumerate(ascii_lowercase)}
_letters_to_num_.update({"S":_letters_to_num_['a']});
_letters_to_num_.update({"E":_letters_to_num_['z']});


class vertex_class (object):
    def __init__(self, i,j):
            self.letter = data[i,j];
            self.height = _letters_to_num_[data[i,j]]   #ord(data[i,j])
            self.ix = (i,j)
    def __repr__(self):
        return self.letter
    
vertices = np.array([ vertex_class(i,j) for i in range(data.shape[0])  for j in range(data.shape[1])  ])

edges = set()
graph = defaultdict(list)

for vertex_i in vertices:
    for vertex_j in vertices:
        if  (manhattan(vertex_i.ix, vertex_j.ix) ==1):
            if (vertex_j.height - vertex_i.height) <= 1 :
                edges.add((vertex_i.ix,vertex_j.ix))

graph = defaultdict(list)
for edge in edges:
    a, b = edge[0], edge[1]; graph[a].append(b); 

            

start_vertex = [vertex.ix for vertex in vertices if  vertex.letter =='S'][0]
end_vertex = [vertex.ix for vertex in vertices if  vertex.letter =='E'][0]

sp = BFS_SP(graph, start_vertex, end_vertex); 
print('Part 1 : {}'.format(len(sp)-1)  )
start_vertices = [vertex.ix for vertex in vertices if  (vertex.height ==0 )]

_lens = [ len( BFS_SP(graph, start_vertex, end_vertex))-1 for start_vertex in start_vertices]
_lens = [_ for _ in _lens if _>= 0]
print('Part 2 : {}'.format(min(_lens))  )