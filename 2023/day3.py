from __future__ import annotations
from typing import List, Dict


def get_neighbours(i: int, j: int, engine: List[List[str]]):
    neighbours = list()
    for i_ in range(max(i - 1, 0), min(i + 2, len(engine[j]))):
        for j_ in range(max(j - 1, 0), min(j + 2, len(engine))):
            if i != i_ or j != j_:
                neighbours.append((i_, j_))
    return neighbours


def is_digit(value: str):
    return '0' <= value <= '9'


def is_symbol(value: str):
    return not is_digit(value) and value != '.'


def is_star(value: str):
    return value == '*'


def get_number(i: int, j: int, engine: List[List[str]]):
    start = end = i
    while start - 1 >= 0 and is_digit(engine[j][start - 1]):
        start = start - 1
    while end + 1 < len(engine[j]) and is_digit(engine[j][end + 1]):
        end = end + 1
    return int(''.join(engine[j][start:end + 1])), end + 1


def part_1():
    engine = [list(line.strip()) for line in open("input.txt", "r").readlines()]
    j = 0
    engine_parts = list()
    while j < len(engine):
        i = 0
        while i < len(engine[j]):
            if is_digit(engine[j][i]):
                if any(is_symbol(engine[n[1]][n[0]]) for n in get_neighbours(i, j, engine)):
                    part = get_number(i, j, engine)
                    engine_parts.append(part[0])
                    i = part[1]
                    continue
            i = i + 1
        j = j + 1

    print(sum(engine_parts))


def part_2():
    engine = [list(line.strip()) for line in open("input.txt", "r").readlines()]
    gears: Dict[(int, int), List[int]] = dict()
    j = 0
    while j < len(engine):
        i = 0
        while i < len(engine[j]):
            if is_digit(engine[j][i]):
                stars = list(filter(lambda n: is_star(engine[n[1]][n[0]]), get_neighbours(i, j, engine)))
                part = get_number(i, j, engine)
                for s in stars:
                    if gears.get(s):
                        gears[s].append(part[0])
                    else:
                        gears[s] = [part[0]]
                if stars:
                    i = part[1]
                    continue
            i = i + 1
        j = j + 1

    print(sum(map(lambda n: n[0] * n[1], filter(lambda g: len(g) == 2, gears.values()))))


part_1()
part_2()
