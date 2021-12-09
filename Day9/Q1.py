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
        
        accumulator = 0
        for row_count, row in enumerate(grid):
            for col_count, idx in enumerate(row):
                if not checkNeighborsAreMin([row_count, col_count], grid):
                    accumulator += idx + 1

        print(accumulator)


