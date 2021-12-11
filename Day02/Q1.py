if __name__ == '__main__':
    horizontal_counter = 0
    vertical_counter = 0
    aim = 0

    # read in text file
    invalues = []
    with open('input.txt', 'r') as f:
        commands = []
        for line in f:
            commands = line.split(' ')
            commands[1] = commands[1][:-1]

            if commands[0] == 'forward':
                horizontal_counter += int(commands[1])
            elif commands[0] == 'down':
                vertical_counter += int(commands[1])
            elif commands[0] == 'up':
                vertical_counter -= int(commands[1])


    print(horizontal_counter * vertical_counter)