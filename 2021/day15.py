import numpy as np


def neighbours(pos, risk_map):
    num_rows, num_cols = risk_map.shape
    res = list()
    if pos[0] > 0:
        res.append((pos[0] - 1, pos[1]))
    if pos[0] < num_cols - 1:
        res.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        res.append((pos[0], pos[1] - 1))
    if pos[1] < num_rows - 1:
        res.append((pos[0], pos[1] + 1))

    return res


def value_for(pos, value_map):
    return value_map[pos[1]][pos[0]]


def distance_to_end(pos, end_pos):
    return end_pos[0] - pos[0] + end_pos[1] - pos[1]


def part_1():
    lines = open("input.txt", "r").readlines()
    risk_map = np.array([[int(i) for i in l.strip()] for l in lines])
    num_rows, num_cols = risk_map.shape
    max_distance = risk_map.sum()

    start = (0, 0)
    end = (num_cols - 1, num_rows - 1)
    distance_array = np.full((num_rows, num_cols), max_distance)
    distance_array[start[1]][start[0]] = 0

    unvisited_pos = set()
    for i in range(0, num_cols):
        for j in range(0, num_rows):
            unvisited_pos.add((i, j))
    while True:
        current_pos = min(unvisited_pos, key=lambda p: distance_array[p[1]][p[0]])
        if current_pos == end:
            break
        unvisited_pos.remove(current_pos)
        current_neighbours = neighbours(current_pos, risk_map)
        for p in current_neighbours:
            if p not in unvisited_pos:
                continue
            distance_array[p[1]][p[0]] = min(value_for(current_pos, distance_array) + value_for(p, risk_map),
                                             value_for(p, distance_array))

    print(value_for(end, distance_array))


def part_2():
    from collections import defaultdict

    import sys
    np.set_printoptions(threshold=sys.maxsize)

    def reset_risk(x):
        nb_ten = int(x / 10)
        return x % 10 + nb_ten

    def remove_from(dictionary, key, value):
        dictionary[key].discard(value)
        if not dictionary[key]:
            dictionary.pop(key)

    lines = open("input.txt", "r").readlines()
    risk_map_initial = np.array([[int(i) for i in l.strip()] for l in lines])
    num_rows_initial, num_cols_initial = risk_map_initial.shape

    replication_factor = 5
    risk_map = np.full((num_rows_initial * replication_factor, num_cols_initial * replication_factor), 0)
    for x in range(0, num_cols_initial * replication_factor):
        for y in range(0, num_rows_initial * replication_factor):
            initial_value = risk_map_initial[y % num_rows_initial][x % num_cols_initial]
            risk_map[y][x] = reset_risk(initial_value + int(x / num_cols_initial) + int(y / num_rows_initial))

    max_distance = risk_map.sum()
    num_rows, num_cols = risk_map.shape
    start = (0, 0)
    end = (num_cols - 1, num_rows - 1)
    distance_array = np.full((num_rows, num_cols), max_distance)
    distance_array[start[1]][start[0]] = 0

    unvisited_pos = defaultdict(set)
    for i in range(0, num_cols):
        for j in range(0, num_rows):
            unvisited_pos[max_distance].add((i, j))
    unvisited_pos[0].add(start)
    remove_from(unvisited_pos, max_distance, start)

    while True:
        min_distance = min(unvisited_pos.keys())
        current_pos = unvisited_pos[min_distance].pop()
        remove_from(unvisited_pos, min_distance, current_pos)

        if current_pos == end:
            break

        current_neighbours = neighbours(current_pos, risk_map)
        for p in current_neighbours:
            current_distance = value_for(p, distance_array)
            if current_distance not in unvisited_pos or p not in unvisited_pos[current_distance]:
                continue
            potential_distance = value_for(current_pos, distance_array) + value_for(p, risk_map)
            if potential_distance < current_distance:
                remove_from(unvisited_pos, current_distance, p)
                unvisited_pos[potential_distance].add(p)
                distance_array[p[1]][p[0]] = potential_distance

    print(value_for(end, distance_array))


part_1()
part_2()
