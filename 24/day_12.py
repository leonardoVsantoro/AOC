from collections import deque, defaultdict

filename = 'input_12.txt'
# filename = 'test_12.txt'

data = open(filename).read().splitlines()
nrows = len(data); ncols = len(data[0])

def find_connected_component(queue, component, perimeter):
    if len(queue)==0:
        return component, perimeter
    else:
        loc = queue.popleft()
        component.add(loc)
        i,j = loc
        neighbours = []
        for newloc in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0 <= newloc[0] < nrows and 0 <= newloc[1] < ncols:
                if data[newloc[0]][newloc[1]] == data[i][j]:
                    neighbours.append(newloc)
        perimeter += 4 - len(neighbours)
        for neib_loc in neighbours:
            if neib_loc not in component:
                component.add(neib_loc)
                queue.append(neib_loc)
        return find_connected_component(queue, component, perimeter)

perimeters = []; components = []
visited = set()
for i in range(nrows) :
    for j in range(ncols):
        if (i,j) not in visited:
            component, perimeter  = find_connected_component(deque([(i,j)]), set(),  0)
            visited.update(component)
            components.append(component)
            perimeters.append(perimeter)

part1 = sum([len(component)*perimeter for component, perimeter in zip(components, perimeters)])

def get_n_sides(component):
    n_sides = 0 
    complement = [(i,j) for i in range(nrows) for j in range(ncols) if (i,j) not in component]
    for i ,j in component:
        if (i+1,j) not in component and (i, j-1) not in component:
            n_sides +=1
        if (i+1,j) not in component and (i,j+1) not in component: 
            n_sides +=1
        if (i-1,j) not in component and (i,j+1) not in component:
            n_sides +=1
        if (i-1,j) not in component and (i,j-1) not in component:
            n_sides +=1
    
    for i ,j in complement:
        if (i+1,j) in component and (i, j-1) in component and (i+1,j-1) in component:
            n_sides +=1
        if (i+1,j) in component and (i,j+1) in component and (i+1,j+1) in component: 
            n_sides +=1
        if (i-1,j) in component and (i,j+1) in component and (i-1,j+1) in component:
            n_sides +=1
        if (i-1,j) in component and (i,j-1) in component and (i-1,j-1) in component:
            n_sides +=1
    return n_sides

part2 = sum([ len(component)*get_n_sides(component) for component in components])

print('part 1:', part1)
print('part 2:', part2)



