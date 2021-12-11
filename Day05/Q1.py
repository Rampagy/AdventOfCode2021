if __name__ == '__main__':
    map = []
    for _ in range(1000):
        row = []
        for _ in range(1000):
            row += [0]
        map += [row]

    with open('input.txt', 'r') as f:
        for line_count, line in enumerate(f):
            points = line.split()
            x1, y1 = points[0].split(',')
            x2, y2 = points[2].split(',')

            x1 = int(x1)
            y1 = int(y1)

            x2 = int(x2)
            y2 = int(y2)


            # determine if horizontal or vertical line
            horizontal_line = False
            vertical_line = False
            if x1 == x2:
                vertical_line = True
            elif y1 == y2:
                horizontal_line = True

            if horizontal_line:
                # horizontal line
                iterations = None
                if x2 > x1:
                    xstep = 1
                    iterations = range(x1, x2+xstep, xstep)
                else:
                    xstep = -1
                    iterations = range(x1, x2+xstep, xstep)

                for x in iterations:
                    map[y1][x] += 1

            elif vertical_line:
                # vertical line
                iterations = None
                if y2 > y1:
                    ystep = 1
                    iterations = range(y1, y2+ystep, ystep)
                else:
                    ystep = -1
                    iterations = range(y1, y2+ystep, ystep)

                for y in iterations:
                    map[y][x1] += 1

    count = 0
    for row in map:
        for val in row:
            if val >= 2:
                count += 1

    print(count)

