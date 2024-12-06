import collections


def parse() -> [list[list[str]], tuple[int, int]]:
    map = [list(line.strip()) for line in open("input.txt", "r").readlines()]
    for i in range(len(map[0])):
        for j in range(len(map)):
            if map[j][i] == '^':
                return map, (i, j)


def get_new_direction(dirs: collections.deque[tuple[(int, int)]]) -> tuple[int, int]:
    new_dir = dirs.popleft()
    dirs.append(new_dir)
    return new_dir


def build_directions() -> collections.deque[tuple[(int, int)]]:
    return collections.deque([
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ])


def get_new_position(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:
    return pos[0] + dir[0], pos[1] + dir[1]


def inside_map(pos: tuple[int, int], map: list[str]) -> bool:
    return 0 <= pos[0] < len(map[0]) and 0 <= pos[1] < len(map)


def count_x(map: list[str]) -> int:
    counter = 0
    for i in range(len(map[0])):
        for j in range(len(map)):
            if map[j][i] == 'X':
                counter = counter + 1
    return counter


def map_printer(map: list[list[str]]):
    for l in map:
        print(''.join(l))
    print()


def part_1():
    map, pos = parse()
    directions = build_directions()
    dir = get_new_direction(directions)
    while inside_map(pos, map):
        map[pos[1]][pos[0]] = 'X'
        new_pos = get_new_position(pos, dir)
        while inside_map(new_pos, map) and map[new_pos[1]][new_pos[0]] == '#':
            dir = get_new_direction(directions)
            new_pos = get_new_position(pos, dir)
        pos = new_pos

    print(count_x(map))


def part_2():
    def is_obstruction(map: list[list[str]], pos: tuple[int, int]) -> bool:
        visited_positions = set()
        directions = build_directions()
        dir = get_new_direction(directions)
        while inside_map(pos, map):
            if (pos, dir) in visited_positions:
                return True
            visited_positions.add((pos, dir))
            new_pos = get_new_position(pos, dir)
            while inside_map(new_pos, map) and map[new_pos[1]][new_pos[0]] == '#':
                dir = get_new_direction(directions)
                new_pos = get_new_position(pos, dir)
            pos = new_pos
        return False

    map, pos = parse()
    init_pos = pos
    directions = build_directions()
    dir = get_new_direction(directions)
    obstruction_positions = set()
    while inside_map(pos, map):
        new_pos = get_new_position(pos, dir)
        while inside_map(new_pos, map) and map[new_pos[1]][new_pos[0]] == '#':
            dir = get_new_direction(directions)
            new_pos = get_new_position(pos, dir)

        if inside_map(new_pos, map):
            map[new_pos[1]][new_pos[0]] = '#'
            if is_obstruction(map, init_pos):
                obstruction_positions.add(new_pos)
            map[new_pos[1]][new_pos[0]] = '.'
        pos = new_pos

    print(len(obstruction_positions))


part_1()
part_2()
