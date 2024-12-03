def to_int(l: list[str]) -> list[int]:
    return [int(c) for c in l]


def is_safe(levels: list[int]) -> bool:
    if len(levels) < 2:
        return True

    diff = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    abs_diff = [abs(d) for d in diff]
    sum_positive = sum([1 if d > 0 else 0 for d in diff])
    return max(abs_diff) <= 3 and min(abs_diff) >= 1 and (sum_positive == len(levels) - 1 or sum_positive == 0)


def part_1():
    reports = [to_int(l) for l in [line.strip().split() for line in open("input.txt", "r").readlines()]]
    valid_reports = [is_safe(r) for r in reports]
    print(sum(valid_reports))


def part_2():
    def is_report_safe_without_index(omitted_index: int, levels: list[int]) -> bool:
        partial_levels = levels[0:omitted_index] + levels[omitted_index + 1:len(levels)]
        return is_safe(partial_levels)

    def is_report_safe(levels: list[int]) -> bool:
        if is_safe(levels):
            return True

        for i in range(len(levels)):
            if is_report_safe_without_index(i, levels):
                return True

        return False

    reports = [to_int(l) for l in [line.strip().split() for line in open("input.txt", "r").readlines()]]
    valid_reports = [is_report_safe(r) for r in reports]
    print(sum(valid_reports))


part_1()
part_2()
