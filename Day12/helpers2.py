import parse # python -m pip install parse
import heapq
import queue

# line parsing functions
def ParseLine(search_pattern, line):
    # https://pypi.org/project/parse/
    result = parse.search(search_pattern, line)
    return list(result.fixed)


# A* functions and classes (with 2d map)
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_surrounding_positions(self):
        return [Position(self.x + 0, self.y - 1), # North
                Position(self.x + 1, self.y + 0), # East
                Position(self.x + 0, self.y + 1), # South
                Position(self.x - 1, self.y + 0)] # West

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.x,
                                   self.y)

    def __hash__(self):
        #return ((self.x+self.y) * (self.x+self.y+1) >> 1) + self.y # cantors pairing
        return self.x * self.x + self.x + self.y if self.x >= self.y else self.x + self.y * self.y # szudziks function

def heuristic(a, b):
    return abs( (a.x - b.x) + (a.y - b.y) )

def astar_search(weighted_map, start, goal):
    # 255 is unwalkable in the weighted map
    # returns list of Position objects
    # start and goal should be Position objects
    # diagonals not currently allowed

    mapWidth = len(weighted_map[0])
    mapHeight = len(weighted_map)

    path = []
    if (start.x < 0) or (start.y < 0) or (goal.x >= mapWidth) or (goal.y >= mapHeight) or \
            (start == goal) or (mapWidth < 2) or (mapHeight < 2):
        return path

    close_set = set()
    came_from = dict()
    gscore = {start: 0}
    fscore = {start : heuristic(start, goal)}
    oheap_copy = { start : fscore[start] }
    oheap = []
    heapq.heappush(oheap, (fscore[start], start))


    while ( len(oheap) > 0 ):
        current = heapq.heappop(oheap)[1]
        oheap_copy.pop(current)

        if current == goal:
            # path found!
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.reverse()
            return path

        neighbors = current.get_surrounding_positions()

        for neighbor in neighbors:

            # if the neighbor is a vlid position
            if (neighbor.x >= 0 and neighbor.y >= 0 and
                    neighbor.y < mapHeight and neighbor.x < mapWidth and
                    weighted_map[neighbor.y][neighbor.x] < 255):

                neighbor_gscore = gscore[current] + weighted_map[neighbor.y][neighbor.x] + \
                                    heuristic(neighbor, current)
                neighbor_fscore = neighbor_gscore + heuristic(neighbor, goal)

                # if this neighbor is already on the open list with a smaller fscore, skip it
                open_neighbor = oheap_copy.get(neighbor)
                if (open_neighbor != None):
                    if open_neighbor <= neighbor_fscore:
                        continue
                # check if it is on the closed list
                elif neighbor in close_set:
                    if fscore.get(neighbor) <= neighbor_fscore:
                        continue
                # add to the open list
                else:
                    # track the node's parent
                    came_from[neighbor] = current

                    # gscore = cost to get from start to the curernt position
                    # hscore = estimated cost to get from the current position to the goal
                    # fscore = gscore + hscore
                    gscore[neighbor] = neighbor_gscore
                    fscore[neighbor] = neighbor_fscore

                    # add to the open list
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))
                    oheap_copy[neighbor] = fscore[neighbor]

        # add current position to the already searched list
        close_set.add(current)

    return path


# djikstra functions and classes (with 2d map)
def djikstra_search(weighted_map, start, goal, diagonals=False):
    # 255 is unwalkable in the weighted map
    # returns list of Position objects
    # start and goal should be position objects
    # diagonals not currently allowed

    mapWidth = len(weighted_map[0])
    mapHeight = len(weighted_map)

    path = []
    if (start.x < 0) or (start.y < 0) or (goal.x >= mapWidth) or (goal.y >= mapHeight) or \
            (start == goal) or (mapWidth < 2) or (mapHeight < 2):
        return path

    close_set = set()
    came_from = dict()
    gscore = {start: 0}
    oheap_copy = { start : gscore[start] }
    oheap = []
    heapq.heappush(oheap, (gscore[start], start))

    count = 0
    while ( len(oheap) > 0 ):
        count += 1
        current = heapq.heappop(oheap)[1]
        oheap_copy.pop(current)
        close_set.add(current)

        neighbors = current.get_surrounding_positions()

        for neighbor in neighbors:

            # if the neighbor is a vlid position
            if (neighbor.x >= 0 and neighbor.y >= 0 and
                    neighbor.y < mapHeight and neighbor.x < mapWidth and
                    weighted_map[neighbor.y][neighbor.x] < 255):

                neighbor_gscore = gscore[current] + weighted_map[neighbor.y][neighbor.x] + \
                                    heuristic(neighbor, current)

                # if this neighbor is already on the open list with a smaller gscore, skip it
                open_neighbor = oheap_copy.get(neighbor)
                if (open_neighbor != None and neighbor_gscore < gscore[neighbor]):
                    # track nodes parent
                    came_from[neighbor] = current

                    # gscore = cost to get from start to the current position
                    gscore[neighbor] = neighbor_gscore

                    # update the neighbors values
                    oheap_copy[neighbor] = neighbor_gscore

                    # remove the old gscore
                    for i in range(oheap.count):
                        if oheap[i][1] == neighbor:
                            oheap.clear(i)
                            break

                    # add to the open list
                    heapq.heappush(oheap, (gscore[neighbor], neighbor))
                    continue

                # check if it is on the closed list
                if neighbor in close_set and neighbor_gscore < gscore[neighbor]:
                    # remove neighbor from closed list
                    close_set.clear(neighbor)

                # add to the open list
                if neighbor not in close_set and open_neighbor == None:
                    # track the node's parent
                    came_from[neighbor] = current

                    # gscore = cost to get from start to the current position
                    gscore[neighbor] = neighbor_gscore

                    # Add to the open list
                    oheap_copy[neighbor] = neighbor_gscore
                    heapq.heappush(oheap, (gscore[neighbor], neighbor))

    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path


# depth first search (using graph)
def DFS(graph, start, end):
    path_set = [] # create the path_set
    DFS_Path(graph, [start], end, path_set)# use this function to find all paths
    return path_set

def DFS_Path(graph, path, end, path_set):
    '''
    You need to use recursion in this function.
    You need to judge whether the state reach the end.
    If it does, calculate the cost and add this path to the path_set.
    Otherwise you need to add the connection state to the path and call this function again inside this function.
    '''
    state = path[-1] # always get the latest node from the end of path
    # your code starts here

    if state != end:
        for p in graph[state]:
            DFS_Path(graph, path + [p], end, path_set)
    else:
        path_set.append(path)

    # your code ends here

# breadth first search (using graph)
def BFS(graph, start, end):
    '''
    There are many ways to do the BFS.
    Here I choose to firstly find the parent of all nodes in the graph and
        then starts from our goal to find the paths to the start.
    You can search reference of other methods on the internet if you want.
    '''
    parent = BFS_parent(graph, start, end)
    path_set = [] # create the path_set
    BFS_Path(parent, [end], start, path_set) # use this function to find all paths
    return path_set

# breadth first search (using graph)
def BFS_parent(graph, start, end):
    '''
    We use this function to find the parent of all nodes in the graph.
    So in this function, we will use queue to make a traversal of the graph and update the dictionary "parent" like this: parent.update({2:[1]}).
    If a node has multiple parents, the key of that node in the dictionary should look like this: 5: [3, 4]
    '''
    q=queue.Queue()
    q.put([start])
    parent={}
    node_count = {}
    # your code starts here

    while not q.empty():
        vs = q.get()
        for v in vs:
            if v == end:
                pass
            if v in graph:
                for search_v in graph[v]:
                    if search_v in parent:
                        if v not in parent[search_v]:
                            parent[search_v] = parent[search_v] + [v]
                    else:
                        parent[search_v] = [v]

                    if search_v.isupper() or \
                            (search_v not in node_count and search_v.islower() and search_v != 'end'):
                        q.put([search_v])

                        if search_v not in node_count:
                            node_count[search_v] = 1
                        else:
                            node_count[search_v] += 1

    # your code ends here
    return parent

# breadth first search (using graph)
def BFS_Path(parent, path, start, path_set):
    '''
    You need to use recursion in this function.
    You need to judge whether the state reach the start.
    If it does, calculate the cost, reverse the path and add this path to the path_set.
    Otherwise you need to add the parent node to the path and call this function
        again inside this function.
    '''
    state = path[-1] # always get the latest node from the end of path
    # your code starts here

    if state != start:
        for p in parent[state]:
            num_nodes_greaterthan1 = [1 for node in path if (node.islower() and path.count(node) > 1)]
            if p.isupper() or (p.islower() and path.count(p) < 2 and sum(num_nodes_greaterthan1) < 3):
                BFS_Path(parent, path + [p], start, path_set)
    else:
        path.reverse()
        path_set.append(path)

    # your code ends here

# A* search (using graph)
def Astar(graph, start, end):
    '''
    For Astar search, you should try to build your own code.
    '''
    path_set = []
    # your code starts here
    h = [100, 50, 50, 50, 30, 20, 0]
    open = {start: h[start]}
    parent = {}

    open = {start: h[start]}
    closed = {}

    while open:
        current_node = min(open.keys(), key=(lambda k: open[k]))
        current_node_f = open.pop(current_node)
        for child, g in graph[current_node].items():
            if child in parent:
                parent[child] += [current_node]
            else:
                parent[child] = [current_node]

            if child == end:
                path_set = [child]
                while start != path_set[-1]:
                    path_set += parent[path_set[-1]]
                path_set.reverse()
                return [path_set]

            if child in open:
                if open[child] > g + h[child]:
                    open[child] = g + h[child]
            elif child in closed and closed[child] < g + h[child]:
                pass
            else:
                open[child] = g + h[child]
        closed[current_node] = current_node_f
    # your code ends here

    return path_set


if __name__ == '__main__':
    # ParseLine examples
    vals = ParseLine('{:d}-{:d},{:d}-{:d}', '51-88,52-87\n')
    print('ParseLine result: {}'.format(vals))

    # create 2d map for pathfinding
    map = [
        [0, 255, 0,   0, 0],
        [0, 255, 0, 255, 0],
        [0, 255, 0, 255, 0],
        [0, 255, 0, 255, 0],
        [0,   0, 0, 255, 0]
    ]

    # A* example (using 2d map)
    path = astar_search(map, Position(0, 0), Position(4, 4))
    print('\nA* result: {}'.format(path))

    # Djikstra example (using 2d map)
    path = djikstra_search(map, Position(0,0), Position(4,4))
    print('\nDjikstra result: {}'.format(path))

    # create graph for pathfinding
    a, b, c, d, e, f, g = range(7)
    graph = [
      {b:50, c:50},
      {d:10, e:20},
      {g:50},
      {f:30},
      {f:10},
      {g:20},
      {}
    ]

    # Breadth first search example (using graph)
    paths = BFS(graph, a, g)
    print('\nBreadth first search paths: {}'.format(paths))

    # Depth first search example (using graph)
    paths = DFS(graph, a, g)
    print('\nDepth first search paths: {}'.format(paths))

    # A* search example (using graph)
    paths = Astar(graph, a, g)
    print('\nA* first search paths: {}'.format(paths))