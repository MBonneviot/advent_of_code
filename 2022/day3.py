def priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    if 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27


def part_1():
    def split_compartments(rucksack):
        return set(rucksack[:len(rucksack) // 2]), set(rucksack[len(rucksack) // 2:])

    def intersect(left, right):
        return list(filter(lambda i: i in right, left))

    priorities = map(lambda items: sum([priority(i) for i in items]),
                     map(
                         lambda r: intersect(r[0], r[1]),
                         map(
                             lambda l: split_compartments(l.strip()),
                             open("input.txt", "r").readlines()
                         )
                     )
                     )
    print(sum(priorities))


def part_2():
    def split_into_groups(rucksacks):
        return [rucksacks[r:r + 3] for r in range(0, len(rucksacks), 3)]

    def intersect(left, middle, right):
        return next(i for i in left if i in right and i in middle)

    rucksacks = [l.strip() for l in open("input.txt", "r").readlines()]

    badges = [intersect(g[0], g[1], g[2]) for g in split_into_groups(rucksacks)]
    print(sum([priority(b) for b in badges]))


part_1()
part_2()
