def get_all_connected_groups(graph):
    already_seen = set()
    result = []
    for node in graph:
        if node not in already_seen:
            connected_group, already_seen = get_connected_group(node, already_seen)
            result.append(connected_group)
    return result
def get_connected_group(node, already_seen):
        result = []
        nodes = set([node])
        while nodes:
            node = nodes.pop()
            already_seen.add(node)
            nodes = nodes or graph[node] - already_seen
            result.append(node)
        return result, already_seen

class vertex_class (object):
    def __init__(self, i):
            self.name= '{}'.format(i);
            self.loc = i;
            self.xyz = data[i];
            self.x = data[i][0]; self.y = data[i][1]; self.z = data[i][2];
    def __repr__(self):
        return self.name

def manhattan_distance(vertex_1,vertex_2):
    return abs(vertex_1.x - vertex_2.x) + abs(vertex_1.y - vertex_2.y) + abs(vertex_1.z - vertex_2.z)

def share_a_side(vertex_1, vertex_2):
    return True if manhattan_distance(vertex_1,vertex_2) ==1 else False

def surface_of_connected_component(component):
    surface = 0
    for i in component:
        surface = surface + 6 - len(graph[i])
    return surface

data = [eval(_) for _ in open('test_18.txt').read().split("\n")]

vertices = [ vertex_class(i) for i in range(len(data)) ]

edges = []
for i, vertex_1 in enumerate(vertices):
    for vertex_2 in vertices[i+1:]:
        if share_a_side(vertex_1, vertex_2):
            edges.append((vertex_1.loc, vertex_2.loc))
        
graph = {vertex.loc : set() for vertex in vertices}
for edge in edges:
    a, b = edge[0], edge[1]; graph[a].add(b); graph[b].add(a)

components = get_all_connected_groups(graph)
print(len(components))

print('\nPart 1 : {}'.format( sum([ surface_of_connected_component(component) for component in components])))