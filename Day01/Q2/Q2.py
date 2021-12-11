if __name__ == '__main__':
    # read in text file
    numbers = []
    with open('input.txt', 'r') as f:
        for line in f:
            numbers += [float(line.strip())]

    # Sliding window average
    averaged_numbers = []
    for i in range(0, len(numbers)-2):
        averaged_numbers += [sum(numbers[i:i+3])]

    print(len(averaged_numbers), len(numbers))

    prev_measurement = averaged_numbers[0]
    averaged_numbers.pop(0)
    count = 0
    for num in averaged_numbers:
        if num - prev_measurement > 0:
            count += 1
        prev_measurement = num

    print(count)