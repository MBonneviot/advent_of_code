def to_int(l: list[str]) -> list[int]:
    return [int(c) for c in l]


def parse() -> list[list[int]]:
    return [to_int(list(line.strip())) for line in open("input.txt", "r").readlines()]


neighbours_directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]


def is_in_map(pos: tuple[int, int], map: list[list[int]]) -> bool:
    return (
            0 <= pos[0] < len(map[0]) and
            0 <= pos[1] < len(map)
    )


def get_neighbors(pos: tuple[int, int], map: list[list[int]]) -> list[tuple[int, int]]:
    neighbors = list()
    for nd in neighbours_directions:
        n_pos = (pos[0] + nd[0], pos[1] + nd[1])
        if is_in_map(n_pos, map):
            neighbors.append(n_pos)
    return neighbors

def part_1():
    def compute_trailheads_score(pos: tuple[int, int], map: list[list[int]]) -> set[tuple[int, int]]:
        if map[pos[1]][pos[0]] == 9:
            return {pos}
        neighbors = get_neighbors(pos, map)
        end_positions = set()
        for n in neighbors:
            if map[n[1]][n[0]] == map[pos[1]][pos[0]] + 1:
                end_positions.update(compute_trailheads_score(n, map))
        return end_positions

    map = parse()

    scores = list()
    for j in range(len(map)):
        for i in range(len(map[0])):
            if map[j][i] == 0:
                scores.append(len(compute_trailheads_score((i, j), map)))

    print(sum(scores))


def part_2():
    def compute_trailheads_rating(pos: tuple[int, int], map: list[list[int]]) -> int:
        if map[pos[1]][pos[0]] == 9:
            return 1
        neighbors = get_neighbors(pos, map)
        rating = 0
        for n in neighbors:
            if map[n[1]][n[0]] == map[pos[1]][pos[0]] + 1:
                 rating = rating + compute_trailheads_rating(n, map)
        return rating

    map = parse()

    ratings = list()
    for j in range(len(map)):
        for i in range(len(map[0])):
            if map[j][i] == 0:
                ratings.append(compute_trailheads_rating((i, j), map))
    print(ratings)
    print(sum(ratings))


#part_1()
part_2()
