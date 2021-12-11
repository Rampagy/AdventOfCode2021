def MostCommon(count, total):
    isMostCommon = True
    if count * 2 < total:
        isMostCommon = False
    return isMostCommon

def LeastCommon(count, total):
    isLeastCommon = False
    if count * 2 <= total:
        isLeastCommon = True
    return isLeastCommon

if __name__ == '__main__':
    numbers = []
    count = 0
    let1 = 0
    let2 = 0
    let3 = 0
    let4 = 0
    let5 = 0
    let6 = 0
    let7 = 0
    let8 = 0
    let9 = 0
    let10 = 0
    let11 = 0
    let12 = 0

    with open('input1.txt', 'r') as f:
        for line in f:
            numbers += [line.strip()]
            count += 1

            if line[0] == '1':
                let1 += 1
            if line[1] == '1':
                let2 += 1
            if line[2] == '1':
                let3 += 1
            if line[3] == '1':
                let4 += 1
            if line[4] == '1':
                let5 += 1

    ones_count = [let1, let2, let3, let4, let5, let6, let7, let8, let9, let10, let11, let12]

    EXIT = False
    oxygen = numbers.copy()
    for round in range(5):
        print('oxygen round:', round)
        for number in oxygen.copy():
            # determine if one is the most common
            if MostCommon(ones_count[round], count): 
                if number[round] == '0': #(int(number) & bit_mask) == 0:
                    # the current number did not have a 1 in that position, so remove it
                    if len(oxygen) <= 2 and number[round] == '1':
                            EXIT = False
                            break
                    oxygen.remove(number)
            
            # determine if zero is the most common
            if MostCommon(count-ones_count[round], count):
                if number[round] == '1': #(int(number) & bit_mask) == 1:
                    # the current number did not have a 0 in that position, so remove it
                    if len(oxygen) <= 2 and number[round] == '1':
                            EXIT = False
                            break
                    oxygen.remove(number)

        print(oxygen)

        if EXIT:
            break

        # recalculate all the counts at each round
        count = 0
        let1 = 0
        let2 = 0
        let3 = 0
        let4 = 0
        let5 = 0
        for line in oxygen:
            count += 1
            if line[0] == '1':
                let1 += 1
            if line[1] == '1':
                let2 += 1
            if line[2] == '1':
                let3 += 1
            if line[3] == '1':
                let4 += 1
            if line[4] == '1':
                let5 += 1

            ones_count = [let1, let2, let3, let4, let5, let6, let7, let8, let9, let10, let11, let12]

    print()

    EXIT = False
    scrubber = numbers.copy()
    for round in range(5):
        print('scrubber round: ', round)
        for number in scrubber.copy():
            if LeastCommon(ones_count[round], count):
                # if one is least common and the bit AND comes out to be a zero it need to be removed
                if number[round] == '0': #(int(number) & bit_mask) == 1:
                    if len(scrubber) <= 2 and number[round] == '0':
                        EXIT = True
                        break
                    scrubber.remove(number)

            if LeastCommon(count-ones_count[round], count):
                # if zero is least common and the bit AND comes out to be a one it need to be removed
                if number[round] == '1': #(int(number) & bit_mask) == 0:
                    if len(scrubber) <= 2 and number[round] == '0':
                        EXIT = True
                        break
                    scrubber.remove(number)

        print(scrubber)

        if EXIT:
            break

        # recalculate all the counts at each round
        count = 0
        let1 = 0
        let2 = 0
        let3 = 0
        let4 = 0
        let5 = 0
        for line in scrubber:
            count += 1
            if line[0] == '1':
                let1 += 1
            if line[1] == '1':
                let2 += 1
            if line[2] == '1':
                let3 += 1
            if line[3] == '1':
                let4 += 1
            if line[4] == '1':
                let5 += 1

            ones_count = [let1, let2, let3, let4, let5, let6, let7, let8, let9, let10, let11, let12]


    print(oxygen, scrubber)


