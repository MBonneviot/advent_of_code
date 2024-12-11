def to_int(l: list[str]) -> list[int]:
    return [int(c) for c in l]

def parse() -> list[tuple[int, list[int]]]:
    raw_equations = [list(line.strip().split()) for line in open("input.txt", "r").readlines()]
    return [(int(e[0].split(':')[0]), to_int(e[1:])) for e in raw_equations]


def part_1():
    def is_made_true(test_value: int, current_value: int, numbers: list[int]) -> bool:
        if current_value == test_value and not numbers:
            return True
        if current_value > test_value or not numbers:
            return False

        return (
            is_made_true(test_value, current_value + numbers[0], numbers[1:]) or
            is_made_true(test_value, current_value * numbers[0], numbers[1:])
        )

    equations = parse()
    true_equations = [ e[0] if is_made_true(e[0], e[1][0], e[1][1:]) else 0  for e in equations]
    print(sum(true_equations))

def part_2():
    def concat(left: int, right: int) -> int:
        return int(f'{left}{right}')

    def is_made_true(test_value: int, current_value: int, numbers: list[int]) -> bool:
        if current_value == test_value and not numbers:
            return True
        if current_value > test_value or not numbers:
            return False

        return (
            is_made_true(test_value, current_value + numbers[0], numbers[1:]) or
            is_made_true(test_value, current_value * numbers[0], numbers[1:]) or
            is_made_true(test_value, concat(current_value, numbers[0]), numbers[1:])
        )

    equations = parse()
    true_equations = [ e[0] if is_made_true(e[0], e[1][0], e[1][1:]) else 0  for e in equations]
    print(sum(true_equations))

part_1()
part_2()
