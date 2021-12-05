def part_1():
    from collections import Counter

    def point_parser(point):
        return [int(p) for p in point.split(',')]

    def line_parser(line):
        values = line.split()
        return [point_parser(values[0]), point_parser(values[-1])]

    def vector_to_points(vector):
        if vector[0][0] == vector[1][0]:
            start = min(vector[0][1], vector[1][1])
            end = max(vector[0][1], vector[1][1]) + 1
            return [(vector[0][0], i) for i in range(start, end)]
        elif vector[0][1] == vector[1][1]:
            start = min(vector[0][0], vector[1][0])
            end = max(vector[0][0], vector[1][0]) + 1
            return [(i, vector[0][1]) for i in range(start, end)]
        else:
            return list()

    lines = open("input.txt", "r").readlines()

    vectors = [line_parser(l) for l in lines]
    filtered_vectors = list(filter(lambda v: v[0][0] == v[1][0] or v[0][1] == v[1][1], vectors))
    points = [p for v in filtered_vectors for p in vector_to_points(v)]
    counters = list(filter(lambda x: x > 1, Counter(points).values()))
    print(len(counters))


def part_2():
    from collections import Counter

    def point_parser(point):
        return [int(p) for p in point.split(',')]

    def line_parser(line):
        values = line.split()
        return [point_parser(values[0]), point_parser(values[-1])]

    def vector_to_points(vector):
        if vector[0][0] == vector[1][0]:
            start = min(vector[0][1], vector[1][1])
            end = max(vector[0][1], vector[1][1]) + 1
            return [(vector[0][0], i) for i in range(start, end)]
        elif vector[0][1] == vector[1][1]:
            start = min(vector[0][0], vector[1][0])
            end = max(vector[0][0], vector[1][0]) + 1
            return [(i, vector[0][1]) for i in range(start, end)]
        else:
            step_h = 1 if vector[0][0] < vector[1][0] else -1
            step_v = 1 if vector[0][1] < vector[1][1] else -1
            return [(vector[0][0] + i * step_h, vector[0][1] + i * step_v) for i in
                    range(0, abs(vector[0][1] - vector[1][1]) + 1)]

    lines = open("input.txt", "r").readlines()

    vectors = [line_parser(l) for l in lines]
    points = [p for v in vectors for p in vector_to_points(v)]
    counters = list(filter(lambda x: x > 1, Counter(points).values()))
    print(len(counters))


part_1()
part_2()
