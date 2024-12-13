from collections import defaultdict

def to_int(l: list[str]) -> list[int]:
    return [int(c) for c in l]

def parse() -> list[str]:
    return to_int(open("input.txt", "r").readline().strip().split())


def part_1():
    def blink(alignment: list[int]) -> list[int]:
        new_alignment = list()
        for a in alignment:
            if a == 0:
                new_alignment.append(1)
            elif len(str(a)) % 2 == 0:
                value = str(a)
                left = value[:int(len(value)/2)]
                right = value[int(len(value)/2):]
                new_alignment.append(int(left))
                new_alignment.append(int(right))
            else:
                new_alignment.append(a * 2024)
        return new_alignment

    stones = parse()
    for i in range(25):
        stones = blink(stones)
    print(len(stones))


def part_2():
    def update_stone(number: int) -> list[int]:
        if number == 0:
            return [1]
        str_number = str(number)
        if len(str_number) % 2 == 0:
            left = str_number[:int(len(str_number) / 2)]
            right = str_number[int(len(str_number) / 2):]
            return [int(left), int(right)]
        return [number * 2024]

    def blink(alignment: dict[list[int]]) -> dict[list[int]]:
        new_alignment = defaultdict(int)
        for stone, mult in alignment.items():
            for new_stones in update_stone(stone):
                new_alignment[new_stones] += mult
        return new_alignment

    stones = defaultdict(int)
    for s in  parse():
        stones[s] += 1

    for i in range(75):
        stones = blink(stones)
    print(sum(stones.values()))

part_1()
part_2()
