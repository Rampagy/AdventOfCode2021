def MostCommon(count, total):
    isMostCommon = False
    if count > total / 2:
        isMostCommon = True
    return isMostCommon

if __name__ == '__main__':
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
            count += 1
            print(line[0], line[1], line[2], line[3], line[4])

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

    gamma = 0
    if MostCommon(let1, count):
        gamma |= 0x800
        #gamma |= 0x1
    
    if MostCommon(let2, count):
        gamma |= 0x400
        #gamma |= 0x2
    
    if MostCommon(let3, count):
        gamma |= 0x200
        #gamma |= 0x4

    if MostCommon(let4, count):
        gamma |= 0x100
        #gamma |= 0x8

    if MostCommon(let5, count):
        gamma |= 0x80
        #gamma |= 0x10


    print(let1, let2, let3, let4, let5)
    print(gamma, gamma * ~gamma)
