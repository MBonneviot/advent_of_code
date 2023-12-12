from typing import List, Dict, Set
import itertools


def decode_input():
    image = [list(line.strip()) for line in open("input.txt", "r").readlines()]

    galaxies = list()
    for j in range(len(image)):
        for i in range(len(image[j])):
            if image[j][i] == '#':
                galaxies.append((i, j))
    x_expanded = set(range(len(image[0]))).difference({g[0] for g in galaxies})
    y_expanded = set(range(len(image))).difference({g[1] for g in galaxies})
    return galaxies, x_expanded, y_expanded


def shortest_distance(lhs: (int, int), rhs: (int, int), x_expanded: Set[int], y_expanded: Set[int],
                      expanded_factor: int):
    x_dist = y_dist = 0
    for x in range(min(rhs[0], lhs[0]) + 1, max(rhs[0], lhs[0]) + 1):
        x_dist = x_dist + expanded_factor if x in x_expanded else x_dist + 1

    for y in range(min(rhs[1], lhs[1]) + 1, max(rhs[1], lhs[1]) + 1):
        y_dist = y_dist + expanded_factor if y in y_expanded else y_dist + 1
    return x_dist + y_dist


def part_1():
    galaxies, x_expanded, y_expanded = decode_input()
    pairs = list(itertools.combinations(galaxies, 2))
    print(sum([shortest_distance(p[0], p[1], x_expanded, y_expanded, 2) for p in pairs]))


def part_2():
    galaxies, x_expanded, y_expanded = decode_input()
    pairs = list(itertools.combinations(galaxies, 2))
    print(sum([shortest_distance(p[0], p[1], x_expanded, y_expanded, 1000000) for p in pairs]))

part_1()
part_2()
