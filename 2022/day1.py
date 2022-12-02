def part_1():
    file = open("input.txt", "r")
    max_cal = 0
    elve_items = list()
    for line in file:
        if not line.strip():
            max_cal = max(max_cal, sum(elve_items))
            elve_items = list()
        else:
            elve_items.append(int(line.strip()))
    max_cal = max(max_cal, sum(elve_items))

    print(max_cal)


def part_2():
    file = open("input.txt", "r")
    elve_items = list()
    global_elves_calories = list()
    for line in file:
        if not line.strip():
            global_elves_calories.append(sum(elve_items))
            elve_items = list()
        else:
            elve_items.append(int(line.strip()))

    global_elves_calories.append(sum(elve_items))

    global_elves_calories.sort(reverse=True)
    print(global_elves_calories)
    print(global_elves_calories[0] + global_elves_calories[1] + global_elves_calories[2])


part_1()
part_2()
