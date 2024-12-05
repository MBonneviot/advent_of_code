def part_1():
    directions = [
        [1, 0],
        [1, 1],
        [0, 1],
        [-1, 1],
        [-1, 0],
        [-1, -1],
        [0, -1],
        [1, -1],
    ]

    def count_mas_for_dir(i: int, j: int, dir: [int, int], puzzle: [str]) -> bool:
        pattern = 'MAS'
        for p in range(len(pattern)):
            i_cur = i + (p + 1)*dir[0]
            j_cur = j + (p + 1)*dir[1]
            if i_cur < 0 or i_cur >= len(puzzle[0]) or j_cur < 0 or j_cur >= len(puzzle):
                return False
            if puzzle[j_cur][i_cur] != pattern[p]:
                return False
        return True


    def count_mas(i: int, j: int, puzzle: [str]) -> int:
        return sum([count_mas_for_dir(i, j, d, puzzle) for d in directions])

    puzzle = [line.strip() for line in open("input.txt", "r").readlines()]
    counter = 0
    for i in range(len(puzzle[0])):
        for j in range(len(puzzle)):
            if puzzle[j][i] == 'X':
                counter = counter + count_mas(i, j, puzzle)
    print(counter)


def part_2():
    diag_1 = [
        [-1, 1],
        [1, -1]
    ]
    diag_2 = [
        [-1, -1],
        [1, 1]
    ]
    def check_char(i: int, j: int, char: str, puzzle: [str])-> bool:
        if i < 0 or i >= len(puzzle[0]) or j < 0 or j >= len(puzzle):
            return False
        return puzzle[j][i] == char

    def check_diag(i: int, j: int, dir: [[int, int]], puzzle: [str]):
        return (
            (check_char(i + dir[0][0], j + dir[0][1], 'M', puzzle) and check_char(i + dir[1][0], j + dir[1][1], 'S', puzzle)) or
            (check_char(i + dir[0][0], j + dir[0][1], 'S', puzzle) and check_char(i + dir[1][0], j + dir[1][1], 'M', puzzle))
        )

    def count_x_mas(i: int, j: int, puzzle: [str]) -> bool:
        return check_diag(i, j, diag_1, puzzle) and check_diag(i, j, diag_2, puzzle)

    puzzle = [line.strip() for line in open("input.txt", "r").readlines()]
    counter = 0
    for i in range(len(puzzle[0])):
        for j in range(len(puzzle)):
            if puzzle[j][i] == 'A':
                counter = counter + count_x_mas(i, j, puzzle)
    print(counter)


part_1()
part_2()
