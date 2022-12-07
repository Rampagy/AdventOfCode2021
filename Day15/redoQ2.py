from astar import astar_search
from Position import Position
import helpers
import time

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        grid = []
        for line_count, line in enumerate(f):
            line = line.strip()

            row0 = [int(char) for char in line]
            row1 = [(val + 1) % 10 if (val + 1) % 10 != 0 else 1 for val in row0 ]
            row2 = [(val + 1) % 10 if (val + 1) % 10 != 0 else 1 for val in row1 ]
            row3 = [(val + 1) % 10 if (val + 1) % 10 != 0 else 1 for val in row2 ]
            row4 = [(val + 1) % 10 if (val + 1) % 10 != 0 else 1 for val in row3 ]
            grid += [row0+row1+row2+row3+row4]

    grid1 = []
    grid2 = []
    grid3 = []
    grid4 = []
    for row in grid:
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        for val in row:
            row1 += [(val + 1) % 10 if (val + 1) % 10 != 0 else 1]
            row2 += [(row1[-1] + 1) % 10 if (row1[-1] + 1) % 10 != 0 else 1]
            row3 += [(row2[-1] + 1) % 10 if (row2[-1] + 1) % 10 != 0 else 1]
            row4 += [(row3[-1] + 1) % 10 if (row3[-1] + 1) % 10 != 0 else 1]
        grid1 += [row1]
        grid2 += [row2]
        grid3 += [row3]
        grid4 += [row4]

    grid += grid1+grid2+grid3+grid4

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

    # My algorithm returns 2845, but the correct is 2844. Could be that A* is not guaranteed to return the best path.
    # Maybe I should have used djikstras....
    print('Python path found in {:0.4f} seconds with cost {:.0f}'.format(total_time, count))