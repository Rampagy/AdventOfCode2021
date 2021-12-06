if __name__ == '__main__':
    fishes = []
    with open('input.txt', 'r') as f:
        for line_count, line in enumerate(f):
            fishes = line.split(',')
            #fish = fish[:-1]

    for i, fish in enumerate(fishes.copy()):
        fishes[i] = int(fish)

    for i in range(80):
        for j, fish in enumerate(fishes.copy()):
            fishes[j] -= 1

            if fishes[j] < 0:
                fishes[j] = 6
                fishes.append(8)

    print(len(fishes))



