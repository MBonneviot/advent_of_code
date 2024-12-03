from collections import Counter


def to_int(l: list[str]) -> list[int]:
    return [int(c) for c in l]


def part_1():
    (l_1, l_2) = zip(*[list(line.strip().split()) for line in open("input.txt", "r").readlines()])
    distances = [abs(d[0] - d[1]) for d in zip(sorted(to_int(l_1)), sorted(to_int(l_2)))]
    print(sum(distances))


def part_2():
    (l_1, l_2) = list(map(to_int, zip(*[list(line.strip().split()) for line in open("input.txt", "r").readlines()])))
    counter = Counter(l_2)
    similarity_scores = [v * counter.get(v, 0) for v in l_1]
    print(sum(similarity_scores))


part_1()
part_2()
