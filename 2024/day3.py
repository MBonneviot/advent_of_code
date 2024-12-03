import re


def part_1():
    memory = open("input.txt", "r").readline()
    regex_mul = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
    instructions = regex_mul.findall(memory)
    print(sum([int(p[0]) * int(p[1]) for p in instructions]))


def part_2():
    do = r"do\(\)"
    dont = r"don\'t\(\)"
    mul = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    memory = open("input.txt", "r").readline()
    regex_mul = re.compile(f'{mul}|{do}|{dont}')
    instructions = regex_mul.finditer(memory)
    enabled = True
    sum = 0
    for i in instructions:
        if i.group() == 'do()':
            enabled = True
        elif i.group() == 'don\'t()':
            enabled = False
        elif enabled:
            sum = sum + int(i.group(1)) * int(i.group(2))
    print(sum)


part_1()
part_2()
