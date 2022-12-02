shape_score = {
    'X': 1,  # = A: Rock
    'Y': 2,  # = B: Paper
    'Z': 3  # = C: Scissors
}


def score(player1, player2):
    if player1 == 'A':
        if player2 == 'X':
            return 3 + shape_score[player2]  # draw
        if player2 == 'Y':
            return 0 + shape_score[player2]  # lost
        if player2 == 'Z':
            return 6 + shape_score[player2]  # won
    if player1 == 'B':
        if player2 == 'Y':
            return 3 + shape_score[player2]  # draw
        if player2 == 'Z':
            return 0 + shape_score[player2]  # lost
        if player2 == 'X':
            return 6 + shape_score[player2]  # won
    if player1 == 'C':
        if player2 == 'Z':
            return 3 + shape_score[player2]  # draw
        if player2 == 'Z':
            return 0 + shape_score[player2]  # lost
        if player2 == 'X':
            return 6 + shape_score[player2]  # won

def part_1():
    file = open("input.txt", "r")
    for line in file:
        round = line.strip().split()
        print(round)

    print("toto")


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
# part_2()
