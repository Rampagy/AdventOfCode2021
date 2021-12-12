class ExploreCave:
    def __init__(self):
        self.came_from_tree = {}
        self.path = []

    # breadth first search
    def ExploreCaveDepth(self, node, cave_system, came_from):
        if node in cave_system:
            self.path += [node]
            if node in self.came_from_tree:
                self.came_from_tree[node] += [came_from]
            else:
                self.came_from_tree[node] = [came_from]

            if node.islower():
                nodes = cave_system.pop(node)
            else:
                nodes = cave_system[node]

            # all of these new nodes have parent of node
            came_from = node

            for node in nodes:
                if node == 'end':
                    # return the path
                    if node in self.came_from_tree:
                        self.came_from_tree['end'] += [came_from]
                    else:
                        self.came_from_tree['end'] = [came_from]

                    return self.came_from_tree
                else:
                    self.ExploreCaveDepth(node, cave_system, came_from)

        return


if __name__ == '__main__':
    with open('input2.txt', 'r') as f:
        cave_system = {}
        for line_count, line in enumerate(f):
            start, dest = line.strip().split('-')
            if start not in cave_system:
                cave_system[start] = [dest]
            else:
                cave_system[start] += [dest]

            if dest not in cave_system:
                cave_system[dest] = [start]
            else:
                cave_system[dest] += [start]

        print(cave_system)

        # go from start to end
        caveObj = ExploreCave()
        came_from = 'start'
        cave_system_copy = cave_system.copy()
        nodes = cave_system_copy.pop(came_from)
        tree = []
        for node in nodes:
            output = caveObj.ExploreCaveDepth(node, cave_system_copy, came_from)
            if output != None:
                tree += [output]


        '''
        print()
        print(tree[0])
        count = 0
        for key, val in tree[0].items():
            count += len(val)
        print(count)
        '''


        '''
        paths = []
        for _ in range(1):
            came_from = 'start'
            cave_system_copy = cave_system.copy()
            nodes = cave_system_copy.pop(came_from)

            for node in nodes:
                path = caveObj.ExploreCaveDepth(node, cave_system_copy, came_from)
                if path != None:
                    paths += [path]

        print(paths[0])
        '''

