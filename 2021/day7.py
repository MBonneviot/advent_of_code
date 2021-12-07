def part_1():
    def fuel_used(pos, h_positions):
        return sum([abs(pos - i) for i in h_positions])

    lines = open("input.txt", "r").readlines()
    h_positions = [int(i) for i in lines[0].split(',')]

    max_pos = max(h_positions)
    result = [fuel_used(p, h_positions) for p in range(0, max_pos)]
    print(min(result))


def part_2():
    def fuel_used(pos, h_positions):
        return sum([int(abs(pos - i)*(abs(pos - i) + 1)/2) for i in h_positions])

    lines = open("input.txt", "r").readlines()
    h_positions = [int(i) for i in lines[0].split(',')]

    max_pos = max(h_positions)
    result = [fuel_used(p, h_positions) for p in range(0, max_pos)]
    print(min(result))

#part_1()
part_2()
