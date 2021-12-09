def part_1():
    import numpy as np

    def neighbours(i, j, heightmap):
        num_rows, num_cols = heightmap.shape
        res = list()
        if i > 0:
            res.append(heightmap[j][i - 1])
        if i < num_cols - 1:
            res.append(heightmap[j][i + 1])
        if j > 0:
            res.append(heightmap[j - 1][i])
        if j < num_rows - 1:
            res.append(heightmap[j + 1][i])

        return res

    def is_lowest(i, j, heightmap):
        return all([n > heightmap[j][i] for n in neighbours(i, j, heightmap)])

    lines = open("input.txt", "r").readlines()
    heightmap = np.array([[int(i) for i in l.strip()] for l in lines])
    lowest = list()
    num_rows, num_cols = heightmap.shape
    for i in range(0, num_cols):
        for j in range(0, num_rows):
            if is_lowest(i, j, heightmap):
                lowest.append(heightmap[j][i])
    print(int(sum(lowest) + len(lowest)))


def part_2():
    import numpy as np
    from functools import reduce
    import operator

    def neighbours(i, j, heightmap):
        num_rows, num_cols = heightmap.shape
        res = list()
        if i > 0:
            res.append((i - 1, j))
        if i < num_cols - 1:
            res.append((i + 1, j))
        if j > 0:
            res.append((i, j - 1))
        if j < num_rows - 1:
            res.append((i, j + 1))

        return res

    def is_lowest(i, j, heightmap):
        return all([heightmap[n[1]][n[0]] > heightmap[j][i] for n in neighbours(i, j, heightmap)])

    def size_bassin(i, j, height, bassin_points, heightmap):
        for n in neighbours(i, j, heightmap):
            if n not in bassin_points and heightmap[n[1]][n[0]] > height and heightmap[n[1]][n[0]] < 9:
                bassin_points.add((n[0], n[1]))
                size_bassin(n[0], n[1], heightmap[n[1]][n[0]], bassin_points, heightmap)

    lines = open("input.txt", "r").readlines()
    heightmap = np.array([[int(i) for i in l.strip()] for l in lines])
    lowest = list()
    num_rows, num_cols = heightmap.shape
    for i in range(0, num_cols):
        for j in range(0, num_rows):
            if is_lowest(i, j, heightmap):
                lowest.append((i, j))
    bassin_size = list()
    for l in lowest:
        bassin_points = {(l[0], l[1])}
        size_bassin(l[0], l[1], heightmap[l[1]][l[0]], bassin_points, heightmap)
        bassin_size.append(len(bassin_points))
    bassin_size.sort()
    print(reduce(operator.mul, bassin_size[-1:-4:-1]))


part_1()
part_2()
