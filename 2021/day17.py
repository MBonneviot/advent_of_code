import re


def next_step(state):
    x, y, vx, vy = state
    return x + vx, y + vy, vx - 1 if vx > 0 else vx + 1 if vx < 0 else 0, vy - 1


def target_reached(state, target):
    x, y, vx, vy = state
    min_x, max_x, min_y, max_y = target
    return (x >= min(min_x, max_x) and
            x <= max(min_x, max_x) and
            y >= min(min_y, max_y) and
            y <= max(min_y, max_y))


def target_missed(state, target):
    x, y, vx, vy = state
    min_x, max_x, min_y, max_y = target
    x_reached = x > max(min_x, max_x) if vx >= 0 else x < min(min_x, max_x)
    y_reached = y < min(min_y, max_y)
    return x_reached or y_reached


def part_1():
    line = open("input.txt", "r").readlines()[0].strip()
    m = re.search(r'target area: x=([-]?\d+)\.\.([-]?\d+), y=([-]?\d+)\.\.([-]?\d+)', line)
    target = [int(i) for i in [m.group(1), m.group(2), m.group(3), m.group(4)]]

    min_x, max_x, min_y, max_y = target
    range_x_max = max(abs(min_x), abs(max_x))
    range_y_max = max(abs(min_y), abs(max_y))

    max_highs = list()
    for i in range(0, range_x_max):
        for j in range(-range_y_max, range_y_max):
            state = (0, 0, i, j)
            max_high = 0
            while True:
                max_high = max(max_high, state[1])
                if target_missed(state, target):
                    break
                if target_reached(state, target):
                    max_highs.append(max_high)
                    break
                state = next_step(state)

    print(max(max_highs))


def part_2():
    line = open("input.txt", "r").readlines()[0].strip()
    m = re.search(r'target area: x=([-]?\d+)\.\.([-]?\d+), y=([-]?\d+)\.\.([-]?\d+)', line)
    target = [int(i) for i in [m.group(1), m.group(2), m.group(3), m.group(4)]]

    min_x, max_x, min_y, max_y = target
    range_x_max = max(abs(min_x), abs(max_x)) + 1
    range_y_max = max(abs(min_y), abs(max_y)) + 1

    nbr_sol = list()
    for i in range(0, range_x_max):
        for j in range(-range_y_max, range_y_max):
            state = (0, 0, i, j)
            while True:
                if target_missed(state, target):
                    break
                if target_reached(state, target):
                    nbr_sol.append((i, j))
                    break
                state = next_step(state)

    print(len(nbr_sol))


part_1()
part_2()
