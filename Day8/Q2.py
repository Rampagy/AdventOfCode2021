def replaceChars(theString, lettersToRemove):

    for letter in lettersToRemove:
        theString = theString.replace(letter, '')

    return theString


if __name__ == '__main__':

    with open('input1.txt', 'r') as f:
        for line_count, line in enumerate(f):
            ins, outs = line.split('|')

            inputs = ins.split()
            outputs = outs.split()

            solved_letters = {}
            solved_words = {}

            for item in inputs:
                if len(item) == 2:
                    # this item must be a 1
                    solved_words[item] = 1

                if len(item) == 3:
                    # this item must be 7
                    solved_words[item] = 7

                if len(item) == 4:
                    # this item must be a 4
                    solved_words[item] = 4

                if len(item) == 5:
                    solved_words[item] = [2, 3, 5]

                if len(item) == 6:
                    solved_words[item] = [0, 6, 9]

                if len(item) == 7:
                    # this item must be a 8
                    solved_words[item] = 8

            eight_item = [key for key, val in solved_words.items() if val == 8 ][0]
            seven_item = [key for key, val in solved_words.items() if val == 7 ][0]
            one_item   = [key for key, val in solved_words.items() if val == 1 ][0]

            for segment in ['a', 'e', 'c', 'd', 'f', 'b', 'g']:
                
                for key, val in solved_words.items():
                    if set(key) < set(seven_item) and val == 1:
                        # 'a' (7 - 2)
                        solved_letters[segment] = replaceChars(seven_item, key)
                        break

                    if key in eight_item and 9 in [val] and key is not eight_item:
                        # 'e' (8 - 9)
                        solved_letters[segment] = replaceChars(eight_item, key)
                        break

                    if key in eight_item and 6 in [val] and key is not eight_item:
                        # 'c' (8 - 6)
                        solved_letters[segment] = replaceChars(eight_item, key)
                        break

                    if key in eight_item and 0 in [val] and key is not eight_item:
                        # 'd' (8 - 0)
                        solved_letters[segment] = replaceChars(eight_item, key)
                        break

                    if val == 7 and 'a' in key and 'c' in key:
                        # 'f' (7 - 'a' - 'c')
                        solved_letters[segment] = replaceChars(key, 'ac') #key.replace('ac', '')
                        break

                    if val == 4 and 'd' in solved_letters:
                        # 'b' (4 - 1 - 'd')
                        solved_letters[segment] = replaceChars(key, one_item+solved_letters['d']) #key.replace(seven_item + solved_letters['d'], '')
                        break

                    if set(key) < set(eight_item) and val == 4 and 'a' in solved_letters and 'd' in solved_letters:
                        # 'g' (8 - 4 - 'a' - 'e')
                        solved_letters[segment] = replaceChars(eight_item, key+solved_letters['a']+solved_letters['e']) #eight_item.replace(key+solved_letters['a']+solved_letters['e'])
                        break


            # sort the dictionary
            solved_letters = dict(sorted(solved_letters.items()))
            print(solved_letters)






