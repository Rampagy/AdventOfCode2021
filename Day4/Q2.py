import numpy as np

def CheckBingo(Board, MostRecent):
    score = 0
    win = False

    running_sum = 0.
    for row in Board:
        horizontal_bingo_count = 0
        running_sum += sum(row)
        for val in row:
            if val == 0:
                horizontal_bingo_count += 1
        if horizontal_bingo_count >= 5:
            win = True
    if win:
        score = running_sum * MostRecent


    if not win:
        # check for vertical win
        # tranpose the board
        Board = list(np.transpose(Board))

        running_sum = 0.
        for row in Board:
            vertical_bingo_count = 0
            running_sum += sum(row)
            for val in row:
                if val == 0:
                    vertical_bingo_count += 1
            if vertical_bingo_count >= 5:
                win = True
        if win:
            score = running_sum * MostRecent

    return win, score


if __name__ == '__main__':
    tiles = []
    boards = []
    current_board = []

    with open('input.txt', 'r') as f:
        for line_count, line in enumerate(f):
            if line_count == 0:
                tiles = line.split(',')
                tiles = tiles[:-1]
                tiles = [int(tile) for tile in tiles]
                continue

            if line == '\n':
                if current_board:
                    # so add the current board we just built to the list of boards
                    boards += [current_board]

                # reset current board
                current_board = []
                continue

            line_entry = [int(val) for val in line.split()]
            current_board += [line_entry]

    # make a duplicate board
    found_tiles = boards.copy()

    winners = []
    exit = False
    for val in tiles:
        for board_num, board in enumerate(boards):
            for row_num, row in enumerate(board):
                if val in row:
                    # keep track of all locations and remove them together at the end
                    val_num = row.index(val)
                    found_tiles[board_num][row_num][val_num] = 0

                    # now do a quick check to see if the board has won
                    winner, score = CheckBingo(found_tiles[board_num], val)

                    if winner:
                        if board_num not in winners:
                            # Add the board_num to the winners
                            winners += [board_num]

                        # do a quick check to see how many boards are left
                        if len(winners) == len(boards):
                            print(score)
                            exit = True

                    if exit:
                        break
                if exit:
                    break
            if exit:
                break
        if exit:
            break
    

                




