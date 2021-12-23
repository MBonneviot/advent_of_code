from collections import deque
from collections import Counter
from functools import lru_cache

from functools import reduce
import itertools

player_1 = (4, 0)
player_2 = (8, 0)


def new_position(cur_pos, dice_score):
    new_calc_pos = (cur_pos + dice_score) % 10
    return new_calc_pos if new_calc_pos > 0 else 10


def part_1():
    def deterministic_dice():
        deterministic_dice.nbr_dice += 1
        new_cale_dice = deterministic_dice.nbr_dice % 100
        return new_cale_dice if new_cale_dice > 0 else 100

    deterministic_dice.nbr_dice = 0

    players = deque([player_1, player_2])

    while all([p[1] < 1000 for p in players]):
        moves = sum([deterministic_dice() for i in range(0, 3)])
        pos, score = players.popleft()
        n_pos = new_position(pos, moves)
        players.append((n_pos, n_pos + score))

    print(deterministic_dice.nbr_dice * min([p[1] for p in players]))


def part_2():
    dice_combinations = list(Counter(list([sum(p) for p in itertools.product([1, 2, 3], repeat=3)])).items())

    def multiply_score(score, coef):
        return score[0] * coef, score[1] * coef

    @lru_cache(maxsize=None)
    def run_player(players, dice, index):
        pos, score = players[index]
        n_pos = new_position(pos, dice)
        if index == 0:
            return (n_pos, n_pos + score), players[1]
        return players[0], (n_pos, n_pos + score)

    @lru_cache(maxsize=None)
    def compute_scores(players, index):
        other_index = (index + 1) % 2
        if players[other_index][1] >= 21:
            return (1, 0) if other_index == 0 else (0, 1)

        new_run = [(dice[1], run_player(players, dice[0], index)) for dice in dice_combinations]
        count = [multiply_score(compute_scores(r[1], other_index), r[0]) for r in new_run]

        return reduce(lambda t1, t2: (t1[0] + t2[0], t1[1] + t2[1]), count)

    scores = compute_scores((player_1, player_2), 0)
    print(max(scores[0], scores[1]))


part_1()
part_2()
