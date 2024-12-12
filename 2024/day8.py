import math

def parse() -> list[str]:
    return [line.strip() for line in open("input.txt", "r").readlines()]

def is_in_map(antenna: tuple[int, int], map: list[str]) -> bool:
    return(
        0 <= antenna[0] < len(map[0]) and
        0 <= antenna[1] < len(map)
    )

def part_1():
    map = parse()

    def symetric_from(a: tuple[int, int], b: tuple[int, int]):
        return 2 * a[0] - b[0], 2 * a[1] - b[1]

    def get_anti_nodes(antenna: tuple[int, int], frequency: str ,antennas: dict[str, list[tuple[int, int]]], map: list[str]) -> list[tuple[int, int]]:
        same_frequency_antennas = antennas.get(frequency, [])
        anti_nodes = list()
        for a in same_frequency_antennas:
            anti_nodes.append(symetric_from(antenna, a))
            anti_nodes.append(symetric_from(a, antenna))
        return list(filter(lambda a: is_in_map(a, map), anti_nodes))

    antennas = dict()
    anti_nodes = set()
    for i in range(len(map[0])):
        for j in range(len(map)):
            if map[j][i] == '.':
                continue
            frequency = map[j][i]
            for an in get_anti_nodes((i, j), frequency, antennas, map):
                anti_nodes.add(an)

            if frequency in antennas:
                antennas[frequency].append((i, j))
            else:
                antennas[frequency] = [(i, j)]


    print(len(anti_nodes))


def part_2():
    map = parse()

    def line_from(a: tuple[int, int], b: tuple[int, int], map: list[str]):
        delta_x = a[0] - b[0]
        delta_y = a[1] - b[1]
        divisor = math.gcd(abs(delta_x), abs(delta_y))
        anti_nodes = list()
        steps = [-1, 1]
        for s in steps:
            step = s
            node = a
            while is_in_map(node, map):
                anti_nodes.append(node)
                node = node[0] + int(step * delta_x/divisor), node[1] + int(step * delta_y/divisor)
        return anti_nodes

    def get_anti_nodes(antenna: tuple[int, int], frequency: str ,antennas: dict[str, list[tuple[int, int]]], map: list[str]) -> list[tuple[int, int]]:
        same_frequency_antennas = antennas.get(frequency, [])
        anti_nodes = list()
        for a in same_frequency_antennas:
            anti_nodes = anti_nodes + line_from(antenna, a, map)

        return anti_nodes

    antennas = dict()
    anti_nodes = set()
    for i in range(len(map[0])):
        for j in range(len(map)):
            if map[j][i] == '.':
                continue
            frequency = map[j][i]
            for an in get_anti_nodes((i, j), frequency, antennas, map):
                anti_nodes.add(an)

            if frequency in antennas:
                antennas[frequency].append((i, j))
            else:
                antennas[frequency] = [(i, j)]


    print(len(anti_nodes))

part_1()
part_2()
