from typing import List, Dict, Set
import itertools


def decode_record_line(line: str):
    damaged_status, groups = line.strip().split(' ')
    unknown = set()
    damaged = set()
    for i in range(len(damaged_status)):
        if damaged_status[i] == '?':
            unknown.add(i)
        elif damaged_status[i] == '#':
            damaged.add(i)

    return damaged, unknown, [int(g) for g in groups.split(',')]


def decode_unfold_record_line(line: str):
    damaged_status, groups = line.strip().split(' ')
    unknown = set()
    damaged = set()
    unfolded_damaged_status = '?'.join([damaged_status for _ in range(5)])
    for i in range(len(unfolded_damaged_status)):
        if unfolded_damaged_status[i] == '?':
            unknown.add(i)
        elif unfolded_damaged_status[i] == '#':
            damaged.add(i)

    return damaged, unknown, [int(g) for _ in range(5) for g in groups.split(',')]


def get_arrangements_number(record: (Set[int], Set[int], List[int])):
    def is_valid(permutation: List[int], record: (Set[int], Set[int], List[int])):
        group = list()
        cumulator = 0
        max_index = max(max(record[0], default=0), max(record[1], default=0))
        for i in range(max_index + 1):
            if i not in record[0] and i not in permutation:
                if cumulator != 0:
                    group.append(cumulator)
                    cumulator = 0
            else:
                cumulator = cumulator + 1
            if i == max_index and cumulator != 0:
                group.append(cumulator)
        return group == record[2]

    print(record)
    arrangements = list(itertools.combinations(record[1], sum(record[2]) - len(record[0])))

    return sum([is_valid(a, record) for a in arrangements])


def part_1():
    records = [decode_record_line(line) for line in open("input.txt", "r").readlines()]
    print(sum([get_arrangements_number(r) for r in records]))


def part_2():
    records = [decode_unfold_record_line(line) for line in open("input.txt", "r").readlines()]
    print(sum([get_arrangements_number(r) for r in records]))


# part_1()
part_2()
