from functools import reduce
import operator


def get_version(index, byte_seq):
    return int(byte_seq[index:index + 3], 2)


def get_type_id(index, byte_seq):
    return get_version(index, byte_seq)


def get_literal(index, byte_seq):
    value = ''
    nb_group = 0
    while True:
        value += byte_seq[nb_group * 5 + 1 + index:(nb_group + 1) * 5 + index]
        if byte_seq[nb_group * 5 + index] == '0':
            break
        nb_group += 1
    new_index = index + 5 * (nb_group + 1)
    return int(value, 2), new_index


def get_operator(index, byte_seq, versions, operation):
    length_type_id = byte_seq[index]
    values = list()
    if length_type_id == '0':
        length = int(byte_seq[index + 1: index + 16], 2)
        value, new_index = decode(index + 16, byte_seq, versions)
        values.append(value)
        while new_index < index + 16 + length:
            value, new_index = decode(new_index, byte_seq, versions)
            values.append(value)
        return operation(values), new_index
    if length_type_id == '1':
        nbr_sub_packets = int(byte_seq[index + 1: index + 12], 2)
        new_index = index + 12
        for i in range(0, nbr_sub_packets):
            value, new_index = decode(new_index, byte_seq, versions)
            values.append(value)
        return operation(values), new_index


operations = {
    0: sum,
    1: lambda x: reduce(operator.mul, x),
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0,
}


def decode(index, byte_seq, versions):
    version = get_version(index, byte_seq)
    versions.append(version)

    type_id = get_type_id(index + 3, byte_seq)

    if type_id == 4:
        return get_literal(index + 6, byte_seq)
    else:
        return get_operator(index + 6, byte_seq, versions, operations[type_id])


def part_1():
    line = open("input.txt", "r").readlines()[0].strip()

    byte_seq = ''.join("{:04b}".format(int(letter, 16)) for letter in line)

    versions = list()
    decode(0, byte_seq, versions)
    print(sum(versions))


def part_2():
    line = open("input.txt", "r").readlines()[0].strip()

    byte_seq = ''.join("{:04b}".format(int(letter, 16)) for letter in line)

    versions = list()
    value, index = decode(0, byte_seq, versions)
    print(value)


part_1()
part_2()
