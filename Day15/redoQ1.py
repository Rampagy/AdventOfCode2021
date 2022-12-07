import helpers
import time

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        grid = []
        for line_count, line in enumerate(f):
            line = line.strip()
            row = [int(char) for char in line]
            grid += [row]

    start = helpers.Position(0, 0)
    goal = helpers.Position(len(grid[0])-1, len(grid)-1)

    total_time = 0
    path = []

    start_time = time.time()

    path = helpers.djikstra_search(grid, start, goal)

    end_time = time.time()
    total_time += end_time - start_time

    count = 0
    for pos in path:
        count += grid[pos.y][pos.x]

    print(count)
    print('Python path found in {:0.4f} seconds'.format(total_time))