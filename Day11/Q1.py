def FlashOctopus(octopus, row_num, col_num, grid, flashed_this_turn):
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row = row_num+i
            new_col = col_num+j

            # bound check
            if new_row < 0 or new_row >= len(grid):
                continue
            if new_col < 0 or new_col >= len(grid[0]):
                continue

            grid[new_row][new_col] += 1

    # flash all 9 octopus
    for row_num1, row in enumerate(grid):
        for col_num1, octopus in enumerate(row):
                if octopus > 9 and (row_num1, col_num1) not in flashed_this_turn:
                    flashed_this_turn += [(row_num1, col_num1)]
                    FlashOctopus(octopus, row_num1, col_num1, grid, flashed_this_turn)

    return

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        grid = []
        for line_count, line in enumerate(f):
            line = line.strip()

            grid += [[int(letter) for letter in line]]

        flash_count = 0
        for step in range(100):
            # increase all octopus by 1
            for row_num, row in enumerate(grid):
                for col_num, octopus in enumerate(row):
                    grid[row_num][col_num] += 1

            flashed_this_turn = []
            # flash all 9 octopus
            for row_num, row in enumerate(grid):
                for col_num, octopus in enumerate(row):
                    if octopus > 9 and (row_num, col_num) not in flashed_this_turn:
                        flashed_this_turn += [(row_num, col_num)]
                        FlashOctopus(octopus, row_num, col_num, grid, flashed_this_turn)
            
            # take all the spots octopuses that flashed and set them to zero
            for row_num, col_num in flashed_this_turn:
                grid[row_num][col_num] = 0

            # increment flash count
            flash_count += len(flashed_this_turn)

        print(flash_count)

