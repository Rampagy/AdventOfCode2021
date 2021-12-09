def checkNeighborsAreMin(position, grid):
    is_minimum = False
    row = position[0]
    col = position[1]

    for i in range(-1, 2):
        for j in range(-1, 2):
            if abs(i) + abs(j) >= 2:
                # skip diagonals
                continue
            elif i + j == 0:
                # is self
                continue

            new_row = row+i
            new_col = col+j

            try:
                grid[new_row][new_col]
            except IndexError:
                # poor mans bound check :)
                continue

            if grid[new_row][new_col] <= grid[row][col]:
                is_minimum = True

    return is_minimum


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        grid = []
        for line_count, line in enumerate(f):
            row = [int(i) for i in line if i != '\n']
            grid += [row]
        
        zone = 0
        zoneMapping = {}
        startLocations = []
        for row_count, row in enumerate(grid):
            for col_count, idx in enumerate(row):
                if not checkNeighborsAreMin([row_count, col_count], grid):
                    zoneMapping[(row_count, col_count)] = zone
                    zone += 1
                    startLocations += [(row_count, col_count)]

        zone_sizes = []

        # breadth first search to see how big the zone is
        for row, col in startLocations:
            zone_size = 0
            already_visited = {(row, col)}
            nogo = set()

            while (len(already_visited) > 0):
                row, col = already_visited.pop()
                nogo.add((row, col))
                zone_size += 1

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if abs(i) + abs(j) >= 2:
                            # skip diagonals
                            continue
                        elif i + j == 0:
                            # skip self
                            continue

                        new_row = row+j
                        new_col = col+i

                        
                        try:
                            grid[new_row][new_col]
                        except IndexError:
                            #nogo.add((new_row, new_col)) # OOR edge
                            # poor mans bound check
                            continue

                        if new_row < 0 or new_row > len(grid):
                            continue
                        if new_col < 0 or new_col > len(grid[0]):
                            continue


                        if grid[new_row][new_col] < 9 and \
                                (new_row, new_col) not in nogo:
                            already_visited.add((new_row, new_col))
                        elif grid[new_row][new_col] >= 9:
                            nogo.add((new_row, new_col))

            zone_sizes += [zone_size]

        zone_sizes.sort()
        print(zone_sizes[-1] * zone_sizes[-2] * zone_sizes[-3])



