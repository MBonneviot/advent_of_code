def part_1():
    from collections import deque

    matching_chars = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    scores = {
        '': 0,
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def invalid_char(line):
        buffer = deque(line.popleft())
        while line:
            char = line.popleft()
            # chunk opening
            if char in matching_chars.keys():
                buffer.append(char)
            # chunk close
            elif char == matching_chars.get(buffer[-1]):
                buffer.pop()
            # invalid
            else:
                return char
        return ''

    lines = [deque(l.strip()) for l in open("input.txt", "r").readlines()]
    invalid_chars = [invalid_char(l) for l in lines]
    print(sum([scores[c] for c in invalid_chars]))


def part_2():
    from collections import deque

    matching_chars = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    scores = {
        '': 0,
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def analyse_line(line):
        buffer = deque(line.popleft())
        while line:
            char = line.popleft()
            # chunk opening
            if char in matching_chars.keys():
                buffer.append(char)
            # chunk close
            elif char == matching_chars.get(buffer[-1]):
                buffer.pop()
            # invalid
            else:
                return char, ''
        return '', [matching_chars[buffer.pop()] for i in range(0, len(buffer))]

    def score(seed, line):
        if line:
            return score(5 * seed + scores[line[0]], line[1:])
        return seed

    lines = [deque(l.strip()) for l in open("input.txt", "r").readlines()]
    analysed_lines = [analyse_line(l) for l in lines]

    incomplete_lines = list(map(lambda x: score(0, x[1]), filter(lambda x: x[1], analysed_lines)))
    incomplete_lines.sort()
    print(incomplete_lines[int(len(incomplete_lines) / 2)])


part_1()
part_2()
