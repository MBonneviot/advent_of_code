from collections import deque
import math


def to_tree(number):
    right = 0
    left = 0
    while True:
        w1 = number.popleft()
        if w1 == '[':
            right = to_tree(number)
        elif w1 == ',':
            left = to_tree(number)
        elif w1 == ']':
            return right, left
        elif w1.isnumeric():
            value = int(w1)
            if number[0].isnumeric():
                w2 = number.popleft()
                value = int(w1 + w2)
            return value


def split(tree):
    if type(tree) is not tuple:
        if tree > 9:
            return True, (math.trunc(tree / 2), math.ceil(tree / 2))
        else:
            return False, tree
    is_l_split, split_tree = split(tree[0])
    if is_l_split:
        return True, (split_tree, tree[1])
    is_r_split, split_tree = split(tree[1])

    if is_r_split:
        return True, (tree[0], split_tree)

    return False, tree


def propagate_left(tree, value):
    if type(tree[0]) is not tuple:
        return True, (tree[0] + value, tree[1])
    is_prop, left_tree = propagate_left(tree[0], value)
    return is_prop, (left_tree, tree[1])


def propagate_right(tree, value):
    if type(tree[1]) is not tuple:
        return True, (tree[0], tree[1] + value)
    is_prop, right_tree = propagate_right(tree[1], value)
    return is_prop, (tree[0], right_tree)


def explode(tree, level):
    if type(tree) is not tuple:
        return False, 0, 0, tree

    if type(tree[0]) is not tuple and type(tree[1]) is not tuple:
        if level >= 4:
            return True, tree[0], tree[1], 0
        return False, 0, 0, tree

    is_l_explode, l, r, exploded_tree = explode(tree[0], level + 1)
    if is_l_explode:
        if type(tree[1]) is not tuple:
            return True, l, 0, (exploded_tree, tree[1] + r)
        is_prop, right_tree = propagate_left(tree[1], r)
        if is_prop:
            return True, l, 0, (exploded_tree, right_tree)
        return True, l, r, (exploded_tree, tree[1])

    is_r_explode, l, r, exploded_tree = explode(tree[1], level + 1)
    if is_r_explode:
        if type(tree[0]) is not tuple:
            return True, 0, r, (tree[0] + l, exploded_tree)
        is_prop, left_tree = propagate_right(tree[0], l)
        if is_prop:
            return True, 0, r, (left_tree, exploded_tree)
        return True, l, r, (tree[0], exploded_tree)

    return False, 0, 0, tree


def reduce(tree):
    current_tree = tree
    while True:
        is_explode, l, r, exploded_tree = explode(current_tree, 0)
        if is_explode:
            current_tree = exploded_tree
        else:
            is_split, split_tree = split(current_tree)
            if is_split:
                current_tree = split_tree
            else:
                return current_tree


def mag(tree):
    left = 3 * (tree[0] if type(tree[0]) is not tuple else mag(tree[0]))
    right = 2 * (tree[1] if type(tree[1]) is not tuple else mag(tree[1]))
    return left + right


def part_1():
    lines = open("input.txt", "r").readlines()
    buffer = to_tree(deque(lines[0].strip()))
    for l in lines[1:]:
        buffer = reduce((buffer, to_tree(deque(l.strip()))))
    print(mag(buffer))


def part_2():
    import itertools
    lines = [to_tree(deque(l.strip())) for l in open("input.txt", "r").readlines()]

    perm = [mag(reduce(t)) for c in list(itertools.combinations(lines, 2)) for t in [(c[0], c[1]), (c[1], c[0])]]
    print(max(perm))


# part_1()
part_2()
