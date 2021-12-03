def part_1():
    def solution_1():
        import numpy as np

        file = open("input.txt", "r")
        line_length = len(file.readline().strip())
        state = np.zeros(line_length)
        nbLines = 0
        for line in file:
            state = np.add(state, np.array([int(i) for i in line.strip()]))
            nbLines += 1

        gamma = int(''.join([str(int(i > nbLines / 2)) for i in state]), base=2)
        epsilon = int(''.join([str(int(i < nbLines / 2)) for i in state]), base=2)

        print(gamma * epsilon)

    def solution_2():
        def compute_index(lines, index, condition):
            nb_one = sum(line[index] == '1' for line in lines)
            return condition(nb_one, len(lines) - nb_one)

        def to_int(array): return int(''.join(array), base=2)

        lines = open("input.txt", "r").readlines()
        gamma = to_int([compute_index(lines, i, lambda a, b: str(int(a > b))) for i in range(len(lines[0]) - 1)])
        epsilon = to_int([compute_index(lines, i, lambda a, b: str(int(a < b))) for i in range(len(lines[0]) - 1)])
        print(gamma * epsilon)

    solution_1()
    solution_2()


def part_2():
    def compute_index(lines, index, condition):
        nb_one = sum(line[index] == '1' for line in lines)
        return condition(nb_one, len(lines) - nb_one)

    def to_int(array):
        return int(''.join(array), base=2)

    def compute(lines, condition):
        line_length = len(lines[0]) - 1
        filtered_lines = lines
        rating = list()
        for i in range(line_length):
            if len(filtered_lines) == 1:
                rating = filtered_lines[0]
                break
            rating.append(compute_index(filtered_lines, i, condition))
            filtered_lines = list(filter(lambda x: x[:i + 1] == ''.join(rating), filtered_lines))
        return to_int(rating)

    lines = open("input.txt", "r").readlines()

    print(compute(lines, lambda a, b: '1' if a >= b else '0') * compute(lines, lambda a, b: '0' if a >= b else '1'))


part_1()
part_2()
