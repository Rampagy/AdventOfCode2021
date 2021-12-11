if __name__ == '__main__':
    fishes = []
    with open('input1.txt', 'r') as f:
        for line_count, line in enumerate(f):
            fishes = line.split(',')

    for i, fish in enumerate(fishes.copy()):
        fishes[i] = int(fish)

    for i in range(256):
        print(i)
        for j, fish in enumerate(fishes.copy()):
            fishes[j] -= 1

            if fishes[j] < 0:
                fishes[j] = 6
                fishes.append(8)

    print(len(fishes))



