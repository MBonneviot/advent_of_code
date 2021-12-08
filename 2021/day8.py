def part_1():
    def count_easy(line):
        easy_len = {2, 4, 3, 7}
        return sum([int(len(w) in easy_len) for w in line])

    lines = [l.split() for l in open("input.txt", "r").readlines()]
    print(sum([count_easy(l[11:]) for l in lines]))


def par_2():
    def decode_line(line, to_decode):
        easy_len = {2, 4, 3, 7}
        easy_digits = list(filter(lambda w: len(w) in easy_len, line))
        mapping = {(1 if len(d) == 2 else 4 if len(d) == 4 else 7 if len(d) == 3 else 8): d for d in easy_digits}

        nine_list = list(filter(lambda w: len(w.intersection(mapping[7].union(mapping[4]))) == len(
            mapping[7].union(mapping[4])) and w not in mapping.values(), line))
        if nine_list:
            mapping[9] = nine_list[0]

        six_list = list(
            filter(lambda w: mapping[1].union(w) == mapping[8] and w not in mapping.values() and len(w) == 6, line))
        if six_list:
            mapping[6] = six_list[0]

        zero_list = list(
            filter(lambda w: mapping[4].union(w) == mapping[8] and w not in mapping.values() and len(w) == 6, line))
        if zero_list:
            mapping[0] = zero_list[0]

        five_list = list(
            filter(lambda w: len(mapping[6].intersection(w)) == 5 and w not in mapping.values() and len(w) == 5, line))
        if five_list:
            mapping[5] = five_list[0]

        three_list = list(
            filter(lambda w: mapping[4].union(w) == mapping[9] and w not in mapping.values(), line))
        if three_list:
            mapping[3] = three_list[0]

        two_list = list(
            filter(lambda w: len(mapping[3].intersection(w)) == 4 and w not in mapping.values() and len(w) == 5, line))
        if two_list:
            mapping[2] = two_list[0]

        decoder = {''.join(sorted(i[1])): i[0] for i in mapping.items()}
        code = decoder[to_decode[0]]*1000 + decoder[to_decode[1]]*100 + decoder[to_decode[2]]*10 + decoder[to_decode[3]]
        return code

    lines = [l.split() for l in open("input.txt", "r").readlines()]
    processed_line = [list(map(lambda w: set(w), filter(lambda w: w != '|', l))) for l in lines]
    print(sum([decode_line(l, [''.join(sorted(i)) for i in l[10:]]) for l in processed_line]))


part_1()
par_2()
