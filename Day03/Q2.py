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

def ConvertToDecimal(BCDString):
    decimal_val = 0
    for i in range(12):
        if BCDString[i] == '1':
            decimal_val |= 1 << (11-i)
    return decimal_val

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

    with open('input.txt', 'r') as f:
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
            if line[5] == '1':
                let6 += 1
            if line[6] == '1':
                let7 += 1
            if line[7] == '1':
                let8 += 1
            if line[8] == '1':
                let9 += 1
            if line[9] == '1':
                let10 += 1
            if line[10] == '1':
                let11 += 1
            if line[11] == '1':
                let12 += 1

    ones_count = [let1, let2, let3, let4, let5, let6, let7, let8, let9, let10, let11, let12]

    EXIT = False
    oxygen = numbers.copy()
    for round in range(12):
        for number in oxygen.copy():
            # determine if one is the most common
            if MostCommon(ones_count[round], count): 
                if number[round] == '0':
                    # the current number did not have a 1 in that position, so remove it
                    if len(oxygen) <= 1:
                            EXIT = True
                            break
                    oxygen.remove(number)
            
            # determine if zero is the most common
            elif MostCommon(count-ones_count[round], count):
                if number[round] == '1':
                    # the current number did not have a 0 in that position, so remove it
                    if len(oxygen) <= 1:
                            EXIT = True
                            break
                    oxygen.remove(number)

        if EXIT:
            break

        # recalculate all the counts at each round
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
            if line[5] == '1':
                let6 += 1
            if line[6] == '1':
                let7 += 1
            if line[7] == '1':
                let8 += 1
            if line[8] == '1':
                let9 += 1
            if line[9] == '1':
                let10 += 1
            if line[10] == '1':
                let11 += 1
            if line[11] == '1':
                let12 += 1

        ones_count = [let1, let2, let3, let4, let5, let6, let7, let8, let9, let10, let11, let12]


    EXIT = False
    scrubber = numbers.copy()
    for round in range(12):
        for number in scrubber.copy():
            if LeastCommon(count-ones_count[round], count):
                # if zero is least common and the bit AND comes out to be a one it need to be removed
                if number[round] == '1':
                    if len(scrubber) <= 1:
                        EXIT = True
                        break
                    scrubber.remove(number)

            elif LeastCommon(ones_count[round], count):
                # if one is least common and the bit AND comes out to be a zero it need to be removed
                if number[round] == '0':
                    if len(scrubber) <= 1:
                        EXIT = True
                        break
                    scrubber.remove(number)

        if EXIT:
            break

        # recalculate all the counts at each round
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
            if line[5] == '1':
                let6 += 1
            if line[6] == '1':
                let7 += 1
            if line[7] == '1':
                let8 += 1
            if line[8] == '1':
                let9 += 1
            if line[9] == '1':
                let10 += 1
            if line[10] == '1':
                let11 += 1
            if line[11] == '1':
                let12 += 1

        ones_count = [let1, let2, let3, let4, let5, let6, let7, let8, let9, let10, let11, let12]

    # 2981085
    print(oxygen, scrubber, ConvertToDecimal(oxygen[0]) * ConvertToDecimal(scrubber[0]))


