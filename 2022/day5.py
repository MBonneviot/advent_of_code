from collections import deque


def parse_input():
    inputs = [line.replace('\n', '') for line in open("input.txt", "r").readlines()]

    nbr_stacks = int((len(inputs[0]) + 1) / 4)
    instructions = list()
    stacks = [deque() for _ in range(0, nbr_stacks)]
    for line in inputs:
        if line.startswith('move'):
            instruction = line.split(' ')
            instructions.append((int(instruction[1]), int(instruction[3]), int(instruction[5])))
        if '[' in line:
            items = [line[i + 1] for i in range(0, len(line), 4)]
            for i in range(0, nbr_stacks):
                if items[i] != ' ':
                    stacks[i].append(items[i])
    return instructions, stacks


def part_1():
    def move_item(origin, destination, stacks):
        stacks[destination - 1].appendleft(stacks[origin - 1].popleft())

    instructions, stacks = parse_input()
    for instruction in instructions:
        for _ in range(0, instruction[0]):
            move_item(instruction[1], instruction[2], stacks)

    print(''.join([s[0] for s in stacks]))


def part_2():
    def move_items(quantity, origin, destination, stacks):
        load = [stacks[origin - 1].popleft() for _ in range(0, quantity)]
        load.reverse()
        for item in load:
            stacks[destination - 1].appendleft(item)

    instructions, stacks = parse_input()
    for instruction in instructions:
        move_items(instruction[0], instruction[1], instruction[2], stacks)

    print(''.join([s[0] for s in stacks]))


part_1()
part_2()
