if __name__ == '__main__':
    fishes = []
    with open('input1.txt', 'r') as f:
        for line_count, line in enumerate(f):
            fishes = line.split(',')

    for i, fish in enumerate(fishes.copy()):
        fishes[i] = int(fish)


    fishes_cons = dict()
    for fish in fishes:
        if fish in fishes_cons:
            fishes_cons[fish] += 1
        else:
            fishes_cons[fish] = 1


    for i in range(80):
        print(fishes_cons)
        new_fishes = dict()
        for days_reproduce, num_fish in fishes_cons.copy().items():

            # decrement these fishies
            if days_reproduce-1 in new_fishes:
                new_fishes[days_reproduce-1] += num_fish
            elif days_reproduce >= 0:
                new_fishes[days_reproduce-1] = num_fish

            if days_reproduce < 0:

                # reset existing fish back to 6
                days_reproduce = 6
                if days_reproduce in new_fishes:
                    new_fishes[days_reproduce] += num_fish
                else:
                    new_fishes[days_reproduce] = num_fish

                # add new fish at 8
                days_reproduce = 8
                if days_reproduce in new_fishes:
                    new_fishes[days_reproduce] += num_fish
                else:
                    new_fishes[days_reproduce] = num_fish

        fishes_cons = new_fishes


    print(sum(fishes_cons.values()))


