if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        scores = []
        for line_count, line in enumerate(f):
            line = line.strip()

            for I in range(11):
                line = line.replace('()', '')
                line = line.replace('[]', '')
                line = line.replace('{}', '')
                line = line.replace('<>', '')
            
            if ')' in line or '}' in line or '>' in line or ']' in line:
                # skip corrupt line
                continue

            # now all that remains are incomplete lines
            autocomplete_string = ''
            points = 0
            for letter in reversed(line):
                if letter == '(':
                    autocomplete_string += ')'
                    points = (points * 5) + 1
                elif letter == '{':
                    autocomplete_string += '}'
                    points = (points * 5) + 3
                elif letter == '[':
                    autocomplete_string += ']'
                    points = (points * 5) + 2
                elif letter == '<':
                    autocomplete_string += '>'
                    points = (points * 5) + 4

            print(line, autocomplete_string)
            scores += [points]

    scores.sort()
    print(scores[int(len(scores)/2)])
