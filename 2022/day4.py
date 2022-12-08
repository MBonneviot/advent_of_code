def part_1():
    def is_right_included_in_left(left, right):
        return right[0] >= left[0] and right[1] <= left[1]

    def is_fully_included(left, right):
        return is_right_included_in_left(left, right) or is_right_included_in_left(right, left)

    assignments = map(lambda pairs: [[int(i) for i in pair.split('-')] for pair in pairs],
                      [line.strip().split(',') for line in open("input.txt", "r").readlines()])

    fully_included = filter(lambda a: is_fully_included(a[0], a[1]), assignments)

    print(len(list(fully_included)))


def part_2():
    def is_right_overlapping_left(left, right):
        return left[1] >= right[0] and left[0] <= right[1]

    def is_overlapping(left, right):
        return is_right_overlapping_left(left, right) or is_right_overlapping_left(right, left)

    assignments = map(lambda pairs: [[int(i) for i in pair.split('-')] for pair in pairs],
                      [line.strip().split(',') for line in open("input.txt", "r").readlines()])

    overlapping = filter(lambda a: is_overlapping(a[0], a[1]), assignments)

    print(len(list(overlapping)))


part_1()
part_2()
