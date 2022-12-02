def part_1():
    shape_score = {
        'X': 1,  # = A: Rock
        'Y': 2,  # = B: Paper
        'Z': 3  # = C: Scissors
    }

    # score for round[1]
    def score(round):
        if round[0] == 'A':
            if round[1] == 'X':
                return 3 + shape_score[round[1]]  # draw
            if round[1] == 'Y':
                return 6 + shape_score[round[1]]  # won
            if round[1] == 'Z':
                return 0 + shape_score[round[1]]  # lost
        if round[0] == 'B':
            if round[1] == 'Y':
                return 3 + shape_score[round[1]]  # draw
            if round[1] == 'Z':
                return 6 + shape_score[round[1]]  # won
            if round[1] == 'X':
                return 0 + shape_score[round[1]]  # lost
        if round[0] == 'C':
            if round[1] == 'Z':
                return 3 + shape_score[round[1]]  # draw
            if round[1] == 'X':
                return 6 + shape_score[round[1]]  # won
            if round[1] == 'Y':
                return 0 + shape_score[round[1]]  # lost

    print(sum(map(lambda l: score(l.strip().split()), open("input.txt", "r").readlines())))


def part_2():
    shape_score = {
        'A': 1,  # = A: Rock
        'B': 2,  # = B: Paper
        'C': 3  # = C: Scissors
    }

    winner_for = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    draw_for = {
        'A': 'A',
        'B': 'B',
        'C': 'C'
    }

    loser_for = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    decode = {
        'X': loser_for,
        'Y': draw_for,
        'Z': winner_for
    }

    round_end_score_for = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    # score for round[1]
    def score(round):
        return round_end_score_for[round[1]] + shape_score[decode[round[1]][round[0]]]

    print(sum(map(lambda l: score(l.strip().split()), open("input.txt", "r").readlines())))


part_1()
part_2()
