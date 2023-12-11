from typing import List, Dict, Set

tiles_connections = {
    '|': lambda tile: [(tile.x, tile.y + 1), (tile.x, tile.y - 1)],
    '-': lambda tile: [(tile.x + 1, tile.y), (tile.x - 1, tile.y)],
    'L': lambda tile: [(tile.x, tile.y - 1), (tile.x + 1, tile.y)],
    'J': lambda tile: [(tile.x, tile.y - 1), (tile.x - 1, tile.y)],
    '7': lambda tile: [(tile.x, tile.y + 1), (tile.x - 1, tile.y)],
    'F': lambda tile: [(tile.x, tile.y + 1), (tile.x + 1, tile.y)],
    '.': lambda tile: [],
    'S': lambda tile: [(tile.x, tile.y + 1), (tile.x, tile.y - 1), (tile.x + 1, tile.y), (tile.x - 1, tile.y)]
}


class Tile:
    def __init__(self, x: int, y: int, c: str):
        self.x = x
        self.y = y
        self.c = c
        self.is_part_of_the_loop = c == 'S'

    def get_connections(self):
        return tiles_connections[self.c](self)

    def get_start_pipe_type(self, connections):
        for t in tiles_connections.items():
            if t[1](self) == connections:
                return t[0]

    def __str__(self):
        return f'{self.c}: ({self.x}, {self.y})'

    def __repr__(self):
        return self.c


def get_neighbours(i, j, plan: List[List[Tile]]):
    return [
        (max(0, i - 1), j),
        (min(len(plan[j]) - 1, i + 1), j),
        (i, max(0, j - 1)),
        (i, min(len(plan) - 1, j + 1))
    ]


def get_diagram():
    diagram = list()
    starting_position = (0, 0)
    line_number = 0
    for line in open("input.txt", "r").readlines():
        striped_line = line.strip()
        tiles_line = list()
        for i in range(len(striped_line)):
            if striped_line[i] == 'S':
                starting_position = (i, line_number)
            tiles_line.append(Tile(i, line_number, striped_line[i]))
        diagram.append(tiles_line)
        line_number = line_number + 1

    after_start_position = list(filter(lambda p: starting_position in diagram[p[1]][p[0]].get_connections(),
                                       diagram[starting_position[1]][starting_position[0]].get_connections()))

    diagram[starting_position[1]][starting_position[0]].c = diagram[starting_position[1]][
        starting_position[0]].get_start_pipe_type(after_start_position)

    return starting_position, after_start_position, diagram


def part_1():
    starting_position, after_start_position, diagram = get_diagram()

    previous_position = starting_position
    position = after_start_position[0]
    path_size = 1
    while (position[0], position[1]) != starting_position:
        connections = diagram[position[1]][position[0]].get_connections()
        new_position = connections[1] if previous_position == connections[0] else connections[0]
        previous_position = position
        position = new_position
        path_size = path_size + 1

    print(int(path_size / 2))


def part_2():
    def get_next_pipe_of_the_loop(index: int, line: List[Tile]):
        nb_area = 0
        from_top = True
        for i in range(index, len(line)):
            if line[i].is_part_of_the_loop and line[i].c == '|':
                return nb_area, i + 1, True
            if line[i].is_part_of_the_loop and line[i].c == '-':
                continue
            if line[i].is_part_of_the_loop and line[i].c == 'L':
                from_top = True
                continue
            if line[i].is_part_of_the_loop and line[i].c == 'F':
                from_top = False
                continue
            if line[i].is_part_of_the_loop and line[i].c == '7':
                return nb_area, i + 1, from_top
            if line[i].is_part_of_the_loop and line[i].c == 'J':
                return nb_area, i + 1, not from_top
            if line[i].is_part_of_the_loop and nb_area > 0:
                return nb_area, i, True
            if line[i].is_part_of_the_loop:
                continue
            nb_area = nb_area + 1
        return None

    starting_position, after_start_position, diagram = get_diagram()

    previous_position = starting_position
    position = after_start_position[0]
    while (position[0], position[1]) != starting_position:
        diagram[position[1]][position[0]].is_part_of_the_loop = True
        connections = diagram[position[1]][position[0]].get_connections()
        new_position = connections[1] if previous_position == connections[0] else connections[0]
        previous_position = position
        position = new_position

    area = 0
    for line in diagram:
        index = 0
        is_contained = False
        while index < len(diagram[0]):
            advance = get_next_pipe_of_the_loop(index, line)
            if advance is None:
                break
            if is_contained:
                area = area + advance[0]
            index = advance[1]
            if advance[2]:
                is_contained = not is_contained
    print(area)


part_1()
part_2()
