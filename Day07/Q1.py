if __name__ == '__main__':
    horizontal_positions = []
    with open('input.txt', 'r') as f:
        for line_count, line in enumerate(f):
            horizontal_positions = line.split(',')
    
    positions = []
    for pos in horizontal_positions.copy():
        positions += [int(pos)]
    del horizontal_positions

    min_fuel = 99999999999999999999999999
    for i in range(max(positions)):
        alist = [i]*(len(positions))

        current_fuel = sum([abs(a - b) for a, b in zip(alist, positions)])

        if current_fuel < min_fuel:
            min_fuel = current_fuel
    
    print(min_fuel)
