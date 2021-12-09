def replaceChars(theString, lettersToRemove):

    for letter in lettersToRemove:
        theString = theString.replace(letter, '')

    return theString


if __name__ == '__main__':
    solution = 0
    with open('input.txt', 'r') as f:
        for line_count, line in enumerate(f):
            ins, outs = line.split('|')

            inputs = ins.split()
            outputs = outs.split()

            solved_letters = {}
            solved_words = {}

            for item in inputs:
                if len(item) == 2:
                    # this item must be a 1
                    solved_words[item] = [1]

                if len(item) == 3:
                    # this item must be 7
                    solved_words[item] = [7]

                if len(item) == 4:
                    # this item must be a 4
                    solved_words[item] = [4]

                if len(item) == 5:
                    solved_words[item] = [2, 3, 5]

                if len(item) == 6:
                    solved_words[item] = [0, 6, 9]

                if len(item) == 7:
                    # this item must be a 8
                    solved_words[item] = [8]

            one_item   = [key for key, val in solved_words.items() if 1 in val][0]
            four_item  = [key for key, val in solved_words.items() if 4 in val][0]
            seven_item = [key for key, val in solved_words.items() if 7 in val][0]
            eight_item = [key for key, val in solved_words.items() if 8 in val][0]

            for segment in ['a', 'g', 'd', 'b', 'e', 'c', 'f']:
                for key, val in solved_words.items():

                    if set(key) < set(seven_item) and 1 in val and 'a' not in solved_letters and segment == 'a':
                        # 'a' (7 - 1)
                        solved_letters[segment] = replaceChars(seven_item, key)
                        break

                    if set(four_item) < set(key) and 9 in val and 'g' not in solved_letters and 'a' in solved_letters and segment == 'g':
                        # 'g' (9 - 4 - 'a')
                        solved_letters[segment] = replaceChars(key, four_item+solved_letters['a'])
                        break

                    if set(one_item) < set(key) and 3 in val and 'd' not in solved_letters and 'a' in solved_letters and 'g' in solved_letters and segment == 'd':
                        # 'd' (3 - 1 - 'a' - 'g')
                        solved_letters[segment] = replaceChars(key, one_item+solved_letters['a']+solved_letters['g'])
                        break

                    if 'd' in solved_letters and 'b' not in solved_letters and segment == 'b':
                        # 'b' (4 - 1 - 'd')
                        solved_letters[segment] = replaceChars(four_item, one_item+solved_letters['d'])
                        break

                    if set(four_item) < set(key) and 9 in val and 'e' not in solved_letters and segment == 'e':
                        # 'e' (8 - 9)
                        solved_letters[segment] = replaceChars(eight_item, key)
                        break

                    if 2 in val and 'a' in solved_letters and 'd' in solved_letters and \
                            'e' in solved_letters and 'g' in solved_letters and \
                            solved_letters['a'] in key and solved_letters['d'] in key and \
                            solved_letters['e'] in key and solved_letters['g'] in key and \
                            'c' not in solved_letters and segment == 'c':
                        # 'c' (2 - 'a' - 'd' - 'e' - 'g')
                        solved_letters[segment] = replaceChars(key, solved_letters['a']+solved_letters['d']+solved_letters['e']+solved_letters['g'])
                        break

                    if 'c' in solved_letters and 'f' not in solved_letters and segment == 'f':
                        # 'f' (1 - 'c')
                        solved_letters[segment] = replaceChars(one_item, solved_letters['c'])
                        break

            # swap key and value
            solved_letters = { val: key for key, val in solved_letters.items() }

            # sort the dictionary
            solved_letters = dict(sorted(solved_letters.items()))

            multiplier = 1000
            accumulator = 0
            for word in outputs:
                if len(word) == 2:
                    accumulator += int(1 * multiplier)
                
                elif len(word) == 3:
                    accumulator += int(7 * multiplier)

                elif len(word) == 4:
                    accumulator += int(4 * multiplier)

                elif len(word) == 5:
                    new_word = ''
                    for letter in word:
                        new_word += solved_letters[letter]

                    if set('acdeg') == set(new_word):
                        accumulator += int(2 * multiplier)
                    elif set('acdfg') == set(new_word):
                        accumulator += int(3 * multiplier)
                    elif set('abdfg') == set(new_word):
                        accumulator += int(5 * multiplier)

                elif len(word) == 6:
                    new_word = ''
                    for letter in word:
                        new_word += solved_letters[letter]

                    if set('abcefg') == set(new_word):
                        accumulator += int(0 * multiplier)
                    elif set('abdefg') == set(new_word):
                        accumulator += int(6 * multiplier)
                    elif set('abcdfg') == set(new_word):
                        accumulator += int(9 * multiplier)

                elif len(word) == 7:
                    accumulator += int(8 * multiplier)

                multiplier /= 10

            solution += accumulator

    print(solution)






