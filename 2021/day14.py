def part_1():
    from collections import Counter

    lines = open("input.txt", "r").readlines()
    template = lines[0].strip()
    pair_insertions = {l.strip().split()[0]: l.strip().split()[2] for l in lines[2:]}

    for step in range(0, 10):
        new_template = ''
        for i in range(0, len(template)):
            pair = template[i:i + 2]
            if pair in pair_insertions.keys():
                new_template = new_template + pair[0] + pair_insertions[pair]
            else:
                new_template = new_template + pair[0]
        template = new_template

    counter = Counter(template)
    min_count = min(counter.values())
    max_count = max(counter.values())
    print(max_count - min_count)


def part_2():
    from collections import Counter

    lines = open("input.txt", "r").readlines()
    template = lines[0].strip()
    pair_insertions = {l.strip().split()[0]: l.strip().split()[2] for l in lines[2:]}

    template_counter = Counter([template[i:i + 2] for i in range(0, len(template) - 1)])
    for step in range(0, 40):
        new_template_counter = dict()
        for pair in template_counter.items():
            if pair[0] in pair_insertions.keys():
                new_template_counter[pair[0][0] + pair_insertions[pair[0]]] = new_template_counter.get(
                    pair[0][0] + pair_insertions[pair[0]], 0) + pair[1]
                new_template_counter[pair_insertions[pair[0]] + pair[0][1]] = new_template_counter.get(
                    pair_insertions[pair[0]] + pair[0][1], 0) + pair[1]
            else:
                new_template_counter[pair[0]] = new_template_counter.get(pair[0], 0) + pair[1]
        template_counter = new_template_counter

    counter = {template[-1]: 1}
    for k in template_counter.items():
        counter[k[0][0]] = counter.get(k[0][0], 0) + k[1]

    min_count = min(counter.values())
    max_count = max(counter.values())
    print(max_count - min_count)


part_1()
part_2()
