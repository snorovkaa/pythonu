try:
    matrix = [[int(j) for j in i.split(" ")] for i in open("1.txt").read().splitlines()]
    length = len(matrix)
    dct = {}
    for x in range(length):
        dct[x] = [y for y in range(length) if matrix[x][y]]

    print(dct)

    flag = False

    def check_is_tree_line(item, st, step=0):
        if step == length: return True
        new_st = set()
        for el1 in st:
            for el2 in dct[el1]:
                if item in dct[el1] and el1 not in dct[item] or el1 in dct[el1]: return False
                new_st.add(el2) 
        return check_is_tree_line(item, new_st, step+1)


    print(all([check_is_tree_line(x, dct[x]) for x in range(length)]))
except: 
    print("Ошибка")