try:
    matrix = [[int(j) for j in i.split(" ")] for i in open("1.txt").read().splitlines()]
    length = len(matrix)
    print(f"Количество изолированных вершин: {length - sum([any([matrix[x][y] for y in range(length) if x != y]) for x in range(length)])}")
except:
    print("Ошибка")