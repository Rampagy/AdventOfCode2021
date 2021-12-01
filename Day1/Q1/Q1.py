if __name__ == '__main__':
    # read in text file
    numbers = []
    with open('input.txt', 'r') as f:
        for line in f:
            numbers += [float(line.strip())]

    prev_measurement = numbers[0]
    numbers.pop(0)
    count = 0
    for num in numbers:
        if num - prev_measurement > 0:
            count += 1
        prev_measurement = num

    print(count)

