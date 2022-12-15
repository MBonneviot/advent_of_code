def create_tree():
    lines = [l.strip().split() for l in open("input.txt", "r").readlines()]

    # name, total files' size, parent, children
    root_node = ['/', 0, None, list()]

    def go_to_node(node_name, current_node):
        if node_name == '/':
            return root_node

        if node_name == '..':
            return current_node[2]

        return create_node(node_name, current_node)

    def create_node(node_name, current_node):
        existing_node = [n for n in current_node[3] if n[0] == node_name]
        if existing_node:
            return existing_node[0]

        new_node = [node_name, 0, current_node, list()]
        current_node[3].append(new_node)
        return new_node

    def add_file(name, size, current_node):
        current_node[1] = int(size) + current_node[1]

    current_node = root_node
    for line in lines:
        if line[0] == '$':
            if line[1] == 'cd':
                current_node = go_to_node(line[2], current_node)
        else:
            if line[0] == 'dir':
                create_node(line[1], current_node)
            else:
                add_file(line[1], line[0], current_node)

    return root_node


def part_1():
    root_node = create_tree()

    size_limit = 100000

    def get_sum_at_most_limit(current_node):
        children = [get_sum_at_most_limit(n) for n in current_node[3]]
        node_size = sum([c[0] for c in children]) + current_node[1]
        total_size_lower_than_limit = sum([c[1] for c in children])
        if node_size <= size_limit:
            return node_size, total_size_lower_than_limit + node_size
        return node_size, total_size_lower_than_limit

    print(get_sum_at_most_limit(root_node)[1])


def part_2():
    root_node = create_tree()

    total_file_system_size = 70000000
    unused_space_to_reach = 30000000

    def get_node_size(current_node):
        node_size = sum([get_node_size(n) for n in current_node[3]]) + current_node[1]
        return node_size

    current_occupied_space = get_node_size(root_node)

    space_to_free = unused_space_to_reach - (70000000 - current_occupied_space)

    def get_smallest_space_to_free(current_node, smallest_space_to_free):
        children = [get_smallest_space_to_free(n, smallest_space_to_free) for n in current_node[3]]
        node_size = sum([c[0] for c in children]) + current_node[1]
        if node_size >= space_to_free:
            return node_size, min(min([c[1] for c in children], default=smallest_space_to_free), node_size)
        return node_size, smallest_space_to_free

    print(get_smallest_space_to_free(root_node, current_occupied_space)[1])


part_1()
part_2()
