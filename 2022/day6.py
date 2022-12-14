def day6(marker_size):
    def is_marker(values):
        for i in range(0, marker_size):
            for j in range(i + 1, marker_size):
                if values[i] == values[j]:
                    return False
        return True

    def get_marker_position(records):
        for i in range(0, len(records) - marker_size):
            if is_marker(records[i:i + marker_size]):
                return i + marker_size
        return 0

    records = [l.strip() for l in open("input.txt", "r").readlines()][0]
    print(get_marker_position(records))


def part_1():
    day6(4)


def part_2():
    day6(14)


part_1()
part_2()
