def part_1():
    def count_easy(line):
        easy_len = {2, 4, 3, 7}
        return sum([int(len(w) in easy_len) for w in line])

    lines = [l.split() for l in open("input.txt", "r").readlines()]
    print(sum([count_easy(l[11:]) for l in lines]))


def par_2():
    from bitarray import bitarray
    from math import pow

    def to_bitarray(word):
        encoded_word = bitarray('0000000')
        for c in word:
            encoded_word[ord(c) - ord('a')] = 1
        return encoded_word

    def decode_line(uniques, code):
        mapping = dict()
        for value in uniques:
            # 1
            if value.count() == 2:
                mapping[1] = value
            # 4
            if value.count() == 4:
                mapping[4] = value
            # 7
            if value.count() == 3:
                mapping[7] = value
            # 8
            if value.count() == 7:
                mapping[8] = value

        for value in uniques:
            # 0, 6 9
            if value.count() == 6:
                if value | mapping[1] == mapping[8]:
                    mapping[6] = value
                elif value | mapping[4] == mapping[8]:
                    mapping[0] = value
                else:
                    mapping[9] = value
            # 2, 3, 5
            if value.count() == 5:
                if value | mapping[4] == mapping[8]:
                    mapping[2] = value
                elif value | mapping[1] == value:
                    mapping[3] = value
                else:
                    mapping[5] = value

        decoder = {str(m[1]): m[0] for m in mapping.items()}
        return int(sum([decoder[code[i]] * pow(10, 3 - i) for i in range(0, 4)]))

    lines = [l.split() for l in open("input.txt", "r").readlines()]
    unique_and_codes = [([to_bitarray(c) for c in l[:10]], [str(to_bitarray(c)) for c in l[11:]]) for l in lines]
    print(sum([decode_line(l[0], l[1]) for l in unique_and_codes]))


part_1()
par_2()
