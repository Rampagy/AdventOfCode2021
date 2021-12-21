import numpy as np

def unpad(x, pad_width):
    new_x = []
    for row in x[pad_width:-pad_width]:
        new_x += [row[pad_width:-pad_width]]
    return new_x

def generate_new_picture(picture, img_enhance_alg):
    new_picture = []
    expanded_pic = np.pad(picture, 3)

    for row_num, row in enumerate(expanded_pic):
        new_row = []
        for col_num, pix in enumerate(row):
            img_enhance_alg_num = 0
            bit_shift = 8
            for row_mod in range(-1, 2):
                for col_mod in range(-1, 2):

                    img_enhance_val = 0
                    if row_num+row_mod >= 0 and row_num+row_mod < len(expanded_pic[0]) and \
                            col_num+col_mod >= 0 and col_num+col_mod < len(expanded_pic):
                        img_enhance_val = expanded_pic[row_num+row_mod][col_num+col_mod]

                    img_enhance_alg_num |= (img_enhance_val << bit_shift)
                    bit_shift -= 1

            # once we know the img enhance alg num, look it up and determine the new output pixel
            new_row += [img_enhance_alg[img_enhance_alg_num]]
        new_picture += [new_row]

    return new_picture

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        img_enhance_alg = []
        picture = []
        buildPictureFlag = False
        for line_count, line in enumerate(f):
            row = []
            if not buildPictureFlag:
                for char in line:
                    if char != '\n' and char != ' ' and char != 0x9:
                        if char == '#':
                            img_enhance_alg += [1]
                        else:
                            img_enhance_alg += [0]
                    elif char == '\n' and line == '\n':
                        # transition to building picture
                        buildPictureFlag = True
            else:
                # build picture
                for char in line:
                    if char != '\n' and char != ' ' and char != 0x9:
                        if char == '#':
                            row += [1]
                        else:
                            row += [0]

                if row != []:
                    picture += [row]

    for i in range(50):
        picture = generate_new_picture(picture, img_enhance_alg)

        if i % 2 == 1:
            picture = unpad(picture, 4)

    accum = 0
    for row in picture:
        for num in row:
            accum += num

    print(accum)

    '''
    for row in picture:
        for num in row:
            if num == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()
    '''

    '''
    print()
    for row in picture_count:
        for num in row:
            if num == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()
    '''





