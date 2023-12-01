def part_1():
    list_of_numbers = list(
        map(lambda l: list(filter(lambda c: '0' <= c <= '9', l.strip())), open("input.txt", "r").readlines()))
    calibration_values = [int(''.join([l[0], l[-1]])) for l in list_of_numbers]

    print(sum(calibration_values))


def part_2():
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    def get_number(value: str):
        if '0' <= value[0] <= '9':
            return value[0]

        for number in digits.keys():
            if value.startswith(number):
                return digits[number]

        return None

    def get_first_number(value: str):
        for i in range(len(value)):
            number = get_number(value[i::])
            if number:
                return number

    def get_last_number(value: str):
        for i in reversed(range(len(value))):
            number = get_number(value[i::])
            if number:
                return number

    list_of_numbers = list(
        map(lambda l: int(''.join([get_first_number(l), get_last_number(l)])), open("input.txt", "r").readlines()))

    print(sum(list_of_numbers))


part_1()
part_2()
