if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        count = 0
        for line_count, line in enumerate(f):
            ins, outs = line.split('|')

            inputs = ins.split()
            outputs = outs.split()

            solved_letters = {}
            solved_words = {}

            for item in outputs:
                if len(item) == 2:
                    count += 1
                    # this item must be a 1
                    solved_words[1] = item

                if len(item) == 3:
                    count += 1
                    # this item must be 7
                    solved_words[7] = item

                if len(item) == 4:
                    count += 1
                    # this item must be a 4
                    solved_words[4] = item
                
                if len(item) == 7:
                    count += 1
                    # this item must be a 8
                    solved_words[8] = item


            #print(inputs, outputs)
            #break
        
        print(count)