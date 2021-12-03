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

    with open('input.txt', 'r') as f:
        for line in f:
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

    gamma = 0
    if MostCommon(let1, count):
        gamma |= 0x800

    if MostCommon(let2, count):
        gamma |= 0x400

    if MostCommon(let3, count):
        gamma |= 0x200

    if MostCommon(let4, count):
        gamma |= 0x100

    if MostCommon(let5, count):
        gamma |= 0x80

    if MostCommon(let6, count):
        gamma |= 0x40

    if MostCommon(let7, count):
        gamma |= 0x20

    if MostCommon(let8, count):
        gamma |= 0x10

    if MostCommon(let9, count):
        gamma |= 0x8

    if MostCommon(let10, count):
        gamma |= 0x4

    if MostCommon(let11, count):
        gamma |= 0x2

    if MostCommon(let12, count):
        gamma |= 0x1

    print(gamma * ((~gamma)&0xFFF))
