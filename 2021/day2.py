def part_1():
    file = open("sonarInput.txt", "r")
    cmd = {
        'forward': lambda h, d, v: (h + v, d),
        'down': lambda h, d, v: (h, d + v),
        'up': lambda h, d, v: (h, d - v)
    }

    pos = (0, 0, 0)
    for line in file:
        instr, value = line.split()
        pos = cmd[instr](pos[0], pos[1], int(value))

    print(pos[0] * pos[1])


def part_2():
    file = open("sonarInput.txt", "r")
    cmd = {
        'forward': lambda h, d, a, v: (h + v, d + a * v, a),
        'down': lambda h, d, a, v: (h, d, a + v),
        'up': lambda h, d, a, v: (h, d, a - v)
    }

    pos = (0, 0, 0)
    for line in file:
        instr, value = line.split()
        pos = cmd[instr](pos[0], pos[1], pos[2], int(value))

    print(pos[0] * pos[1])


part_1()
part_2()
