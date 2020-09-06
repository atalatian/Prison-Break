def lock_unlock(cells):
    dic = {-1: cells}
    cells_new = cells[:]
    for i in range(0, len(cells_new)):
        if cells_new[i] == 1:
            cells_new[i] = 0
        elif cells_new[i] == 0:
            cells_new[i] = 1
    dic[1] = cells_new

    return dic


def get_free_prisoners():
    dic = lock_unlock([0, 1, 1, 1])
    dic_index = -1
    list_index = 0
    counter = 0
    while True:
        if list_index >= len(dic[dic_index]):
            break
        if dic[dic_index][list_index] == 1:
            counter += 1
            dic_index = -dic_index
        list_index += 1

    if counter > 0:
        print("Number of freed prisoners are: {}".format(counter))
    elif counter == 0:
        print("Couldn't free any prisoner.")


get_free_prisoners()
