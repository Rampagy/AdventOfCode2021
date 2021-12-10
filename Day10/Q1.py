if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        points = 0
        for line_count, line in enumerate(f):
            line = line.strip()

            for I in range(11):
                line = line.replace('()', '')
                line = line.replace('[]', '')
                line = line.replace('{}', '')
                line = line.replace('<>', '')
            
            wrongChar = [letter for letter in line if letter not in '{[<(']
            
            if len(wrongChar) > 0:
                wrongChar = wrongChar[0]


            if wrongChar == ')':
                points += 3
            elif wrongChar == ']':
                points += 57
            elif wrongChar == '}':
                points += 1197
            elif wrongChar == '>':
                points += 25137

        print(points)
