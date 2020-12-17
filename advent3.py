with open('toboggan.txt') as file:
    hashtag_list = [line.rstrip() for line in file]


def slope_calc(data, right, down):
    tree = 0
    open_space = 0
    first = True
    position = right
    line_count = 0

    for line in data:
        if line != "":
            line_read = line.rstrip("\n")
            if first:
                first = False
            else:
                if line_count % down == 0:
                    if line_read[position] == ".":
                        open_space += 1
                    else:
                        if line_read[position] == "#":
                            tree += 1
                    position += right
                    if position > len(line_read)-1:
                        position = position-len(line_read)
        line_count += 1

    print("Tree = {}, Open = {}".format(tree, open_space))
    return tree

def multiply_slopes():
    tob1 = (slope_calc(hashtag_list, 1, 1))
    tob2 = (slope_calc(hashtag_list, 3, 1))
    tob3 = (slope_calc(hashtag_list, 5, 1))
    tob4 = (slope_calc(hashtag_list, 7, 1))
    tob5 = (slope_calc(hashtag_list, 1, 2))
    return print(tob1 * tob2 * tob3 * tob4 * tob5)

multiply_slopes()