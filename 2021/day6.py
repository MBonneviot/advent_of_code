def part_1():
    def after_a_day(age):
        if age == 0:
            return [6, 8]
        else:
            return [age - 1]

    lines = open("input.txt", "r").readlines()

    nb_days = 80
    state = [int(i) for i in lines[0].split(',')]
    for a in range(0, nb_days):
        state = [ages for a in state for ages in after_a_day(a)]
        print(state)

    print(len(state))


def part_2():
    from collections import Counter

    def counter_after_a_day(state):
        new_state = dict()
        for counter in state.items():
            age = counter[0]
            nb = counter[1]
            if age == 0:
                new_state[8] = nb
                new_state[6] = new_state.get(6, 0) + nb
            else:
                new_state[age-1] = new_state.get(age-1, 0) + nb
        return new_state

    lines = open("input.txt", "r").readlines()

    nb_days = 256
    state = dict(Counter([int(i) for i in lines[0].split(',')]))
    for d in range(0, nb_days):
        state = counter_after_a_day(state)
        print(state)

    print(sum(state.values()))


part_1()
part_2()
