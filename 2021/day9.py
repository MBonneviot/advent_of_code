def part_1():
    import numpy as np

    def neighbours(i, j, heightmap):
        num_rows, num_cols = heightmap.shape
        res = list()
        if i > 0:
            res.append(heightmap[j][i-1])
        if i < num_cols - 1:
            res.append(heightmap[j][i+1])
        if j > 0:
            res.append(heightmap[j-1][i])
        if i < num_rows - 1:
            res.append(heightmap[j+1][i])

        return res

    def is_lowest(i, j, heightmap):
        return all([ n > heightmap[j][i] for n in neighbours(i, j, heightmap)])


    lines = open("input.txt", "r").readlines()
    heightmap = np.array([[int(i) for i in l.strip()] for l in lines])
    print(heightmap)
    lowest = list()
    num_rows, num_cols = heightmap.shape
    for i in range(0, num_cols):
        for j in range(0, num_rows):
            if is_lowest(i, j, heightmap):
                lowest.append(heightmap[j][i])
    print(lowest)


part_1()
