def fold_y(y, point):
    if point[1] > y:
        return point[0], 2 * y - point[1]
    return point


def fold_x(x, point):
    if point[0] > x:
        return 2 * x - point[0], point[1]
    return point


instruction_mapping = {
    'fold along x': fold_x,
    'fold along y': fold_y,
}


def apply_instruction(instruction, points):
    return {instruction_mapping[instruction[0]](instruction[1], p) for p in points}


def parse():
    points = set()
    instructions = list()
    is_point = True
    for l in [l.strip() for l in open("input.txt", "r").readlines()]:
        if not l:
            is_point = False
            continue
        if is_point:
            point = l.split(',')
            points.add((int(point[0]), int(point[1])))
        else:
            instruction = l.split('=')
            instructions.append((instruction[0], int(instruction[1])))

    return points, instructions


def part_1():
    points, instructions = parse()
    print(len(apply_instruction(instructions[0], points)))


def part_2():
    points, instructions = parse()
    for instruction in instructions:
        points = apply_instruction(instruction, points)

    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])

    for y in range(0, max_y + 1):
        print(''.join(['#' if (x, y) in points else '_' for x in range(0, max_x + 1)]))


part_1()
part_2()
