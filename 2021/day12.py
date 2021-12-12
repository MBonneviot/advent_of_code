def part_1():
    from collections import defaultdict

    def generate_connection(a, b):
        if a == 'start' or b == 'end':
            return [(a, b)]
        if b == 'start' or a == 'end':
            return [(b, a)]
        return [(a, b), (b, a)]

    def explore(node, explored_small_cave, current_path, complete_paths):
        for c in connections[node]:
            if c in explored_small_cave:
                continue

            new_path = current_path.copy()
            new_path.append(c)
            if c == 'end':
                complete_paths.append(new_path)
            elif c.islower():
                new_explored_small_cave = explored_small_cave.copy()
                new_explored_small_cave.add(c)
                explore(c, new_explored_small_cave, new_path, complete_paths)
            else:
                explore(c, explored_small_cave, new_path, complete_paths)

    connections = defaultdict(set)
    for l in open("input.txt", "r").readlines():
        for w in generate_connection(*l.strip().split('-')):
            connections[w[0]].add(w[1])

    complete_paths = list()
    explore('start', set(), ['start'], complete_paths)
    print(len(complete_paths))


def par_2():
    from collections import defaultdict

    def generate_connection(a, b):
        if a == 'start' or b == 'end':
            return [(a, b)]
        if b == 'start' or a == 'end':
            return [(b, a)]
        return [(a, b), (b, a)]

    def explore(node, twice_small_cave, explored_small_cave, current_path, complete_paths):
        for c in connections[node]:
            if c in explored_small_cave and twice_small_cave:
                continue

            new_path = current_path.copy()
            new_path.append(c)
            if c == 'end':
                complete_paths.append(new_path)
            elif c.islower():
                new_explored_small_cave = explored_small_cave.copy()
                new_explored_small_cave.add(c)
                new_twice_small_cave = twice_small_cave or len(new_explored_small_cave) == len(explored_small_cave)
                explore(c, new_twice_small_cave, new_explored_small_cave, new_path, complete_paths)
            else:
                explore(c, twice_small_cave, explored_small_cave, new_path, complete_paths)

    connections = defaultdict(set)
    for l in open("input.txt", "r").readlines():
        for w in generate_connection(*l.strip().split('-')):
            connections[w[0]].add(w[1])

    complete_paths = list()
    explore('start', False, set(), ['start'], complete_paths)
    print(len(complete_paths))


part_1()
par_2()
