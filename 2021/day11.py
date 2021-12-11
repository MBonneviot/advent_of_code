def part_1():
    import numpy as np

    def neighbours(i, j, energy_map):
        num_rows, num_cols = energy_map.shape
        area = {(x, y) for y in range(max(0, j - 1), min(num_rows, j + 2)) for x in
                range(max(0, i - 1), min(num_cols, i + 2))}
        area.remove((i, j))
        return area

    def update_due_to_flash(flashers, energy_map):
        for flasher in flashers:
            for neighbour in neighbours(flasher[0], flasher[1], energy_map):
                energy_map[neighbour[1], neighbour[0]] += 1

    def get_flash(energy_map, flashers):
        new_flashers = list()
        num_rows, num_cols = energy_map.shape
        for i in range(0, num_cols):
            for j in range(0, num_rows):
                if (i, j) not in flashers and energy_map[j][i] > 9:
                    new_flashers.append((i, j))
                    flashers.add((i, j))

        return new_flashers

    def reset_flasher(x):
        return x if x < 10 else 0

    lines = open("input.txt", "r").readlines()
    energy_map = np.array([[int(i) for i in l.strip()] for l in lines])

    nb_flash = 0
    for step in range(0, 100):
        flashers = set()
        energy_map = np.vectorize(reset_flasher)(energy_map)
        energy_map += 1
        while True:
            new_flashers = get_flash(energy_map, flashers)
            update_due_to_flash(new_flashers, energy_map)
            flashers.union(new_flashers)
            if not len(new_flashers):
                break
        nb_flash += len(flashers)

    print(nb_flash)

def part_2():
    import numpy as np

    def neighbours(i, j, energy_map):
        num_rows, num_cols = energy_map.shape
        area = {(x, y) for y in range(max(0, j - 1), min(num_rows, j + 2)) for x in
                range(max(0, i - 1), min(num_cols, i + 2))}
        area.remove((i, j))
        return area

    def update_due_to_flash(flashers, energy_map):
        for flasher in flashers:
            for neighbour in neighbours(flasher[0], flasher[1], energy_map):
                energy_map[neighbour[1], neighbour[0]] += 1

    def get_flash(energy_map, flashers):
        new_flashers = list()
        num_rows, num_cols = energy_map.shape
        for i in range(0, num_cols):
            for j in range(0, num_rows):
                if (i, j) not in flashers and energy_map[j][i] > 9:
                    new_flashers.append((i, j))
                    flashers.add((i, j))

        return new_flashers

    def reset_flasher(x):
        return x if x < 10 else 0

    lines = open("input.txt", "r").readlines()
    energy_map = np.array([[int(i) for i in l.strip()] for l in lines])

    step = 0
    while True:
        step += 1
        flashers = set()
        energy_map = np.vectorize(reset_flasher)(energy_map)
        energy_map += 1
        while True:
            new_flashers = get_flash(energy_map, flashers)
            update_due_to_flash(new_flashers, energy_map)
            flashers.union(new_flashers)
            if not len(new_flashers):
                break
        if len(flashers) == energy_map.size:
            break
    print(step)


part_1()
part_2()
