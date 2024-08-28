def read_patterns() -> list[list[str]]:
    patterns = []
    buffer = []
    for line in open("input.txt", "r").readlines():
        stripped_line = line.strip()
        if not stripped_line:
            patterns.append(buffer)
            buffer = []
        else:
            buffer.append(stripped_line)
    patterns.append(buffer)
    return patterns


def rotate(pattern: list[str]) -> list[str]:
    return list(zip(*pattern))[::-1]


def part_1():
    def columns_equals(pattern: list[str], c1: int, c2: int) -> bool:
        for j in range(0, len(pattern)):
            if pattern[j][c1] != pattern[j][c2]:
                return False
        return True

    def get_vertical_reflection_axis(pattern: list[str]) -> int:
        for i in range(0, len(pattern[0]) - 1):
            test = [columns_equals(pattern, i - k, i + k + 1) for k in range(0, min(i + 1, len(pattern[0]) - i - 1))]
            if all(test):
                return i + 1
        return 0

    def get_reflection_score(pattern: list[str]) -> int:
        v_score = get_vertical_reflection_axis(pattern)
        if v_score == 0:
            return get_vertical_reflection_axis(rotate(pattern)) * 100
        return v_score

    patterns = read_patterns()
    scores = [get_reflection_score(p) for p in patterns]
    print(sum(scores))


def part_2():
    def columns_differences(pattern: list[str], c1: int, c2: int) -> int:
        return sum([0 if pattern[j][c1] == pattern[j][c2] else 1 for j in range(0, len(pattern))])

    def get_vertical_reflection_axis(pattern: list[str]) -> int:
        for i in range(0, len(pattern[0]) - 1):
            differences = [columns_differences(pattern, i - k, i + k + 1) for k in
                           range(0, min(i + 1, len(pattern[0]) - i - 1))]
            if sum(differences) == 1:
                return i + 1
        return 0

    def get_reflection_score(pattern: list[str]) -> int:
        v_score = get_vertical_reflection_axis(pattern)
        if v_score == 0:
            return get_vertical_reflection_axis(rotate(pattern)) * 100
        return v_score

    patterns = read_patterns()
    scores = [get_reflection_score(p) for p in patterns]
    print(sum(scores))


part_1()
part_2()
