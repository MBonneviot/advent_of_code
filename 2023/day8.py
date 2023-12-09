from __future__ import annotations
import re
from itertools import cycle
from typing import List, Dict, Set
from math import lcm

direction = {
    'L': lambda t: t[0],
    'R': lambda t: t[1]
}


def decode_node(line: str):
    return re.findall(f'([0-9A-Z]*) = \(([0-9A-Z]*), ([0-9A-Z]*)\)', line)[0]


def decode_input():
    directions = list()
    nodes = list()
    for line in open("input.txt", "r").readlines():
        if not directions:
            directions = line.strip()
            continue

        if not line.strip():
            continue

        nodes.append(decode_node(line))

    return directions, nodes


def part_1():
    directions, nodes = decode_input()
    network = {t[0]: (t[1], t[2]) for t in nodes}

    current_node = 'AAA'
    all_directions = cycle(directions)
    counter = 0
    while current_node != 'ZZZ':
        current_node = direction[next(all_directions)](network[current_node])
        counter = counter + 1
    print(counter)


def part_2():
    def compute_path(start_node: str, dirs: List[str], net: Dict[str, List[str, str]]):
        counter = 0
        current_node = start_node
        visited_start_nodes = set()
        visited_start_nodes.add(start_node)
        while True:
            for d in dirs:
                current_node = direction[d](net[current_node])
                counter = counter + 1
            if current_node[2] == 'Z':
                return start_node, counter
            if current_node in visited_start_nodes:
                print(f'no end for node {current_node}')
                return start_node, counter
            visited_start_nodes.add(current_node)

    directions, nodes = decode_input()
    network = {t[0]: (t[1], t[2]) for t in nodes}

    all_paths = dict([compute_path(n, directions, network) for n in network])

    current_nodes = list(map(lambda n: n[0], filter(lambda n: n[0][2] == 'A', nodes)))
    nb_iterations_to_z = [all_paths[n] for n in current_nodes]
    print(lcm(*nb_iterations_to_z))


part_1()
part_2()
