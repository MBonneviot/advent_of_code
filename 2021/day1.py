def part_1():
    file = open("input.txt", "r")
    previous_depth = 0
    nbr_increase = -1
    for line in file:
        depth = int(line)
        if depth > previous_depth:
            nbr_increase += 1
        previous_depth = depth

    print(nbr_increase)


def part_2():
    from collections import deque
    file = open("input.txt", "r")
    previous_depths = deque(maxlen=3)
    nbr_increase = -3
    for line in file:
        previous_depth = sum(previous_depths)
        previous_depths.append(int(line))
        depth = sum(previous_depths)
        if depth > previous_depth:
            nbr_increase += 1

    print(nbr_increase)


part_1()
part_2()
