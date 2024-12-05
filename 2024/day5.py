def parse():
    file = open("input.txt", "r")
    ordering_rules = dict()
    updates = list()
    processing_order = True
    for line in file.readlines():
        if not line.strip():
            processing_order = False
            continue

        if processing_order:
            order = line.split(r"|")
            left = int(order[0])
            right = int(order[1])
            if left in ordering_rules:
                ordering_rules[left].append(right)
            else:
                ordering_rules[left] = [right]
        else:
            updates.append([int(l) for l in line.split(',')])

    return ordering_rules, updates


def is_update_valid(update: list[int], ordering: dict[int, list[int]]) -> bool:
    processed_data = set()
    for u in update:
        if u in ordering and any([o in processed_data for o in ordering[u]]):
            return False
        processed_data.add(u)
    return True


def part_1():
    ordering_rules, updates = parse()
    middle_page_numbers = [u[int(len(u) / 2)] if is_update_valid(u, ordering_rules) else 0 for u in updates]
    print(sum(middle_page_numbers))


def part_2():
    def fix_one_rule(update: list[int], ordering: dict[int, list[int]]) -> list[int]:
        new_update = list()
        for u in update:
            if u in ordering:
                new_update.append(u)
                for o in ordering[u]:
                    if o in new_update:
                        new_update.remove(o)
                        new_update.append(o)
        return new_update

    def fix_update(update: list[int], ordering: dict[int, list[int]]) -> list[int]:
        if is_update_valid(update, ordering):
            return update

        return fix_update(fix_one_rule(update, ordering), ordering)

    ordering_rules, updates = parse()

    middle_page_numbers = list()
    for update in updates:
        if is_update_valid(update, ordering_rules):
            continue
        fixed_update = fix_update(update, ordering_rules)
        middle_page_numbers.append(fixed_update[int(len(fixed_update) / 2)])

    print(sum(middle_page_numbers))


part_1()
part_2()
