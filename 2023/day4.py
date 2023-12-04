from __future__ import annotations
import re
from collections import defaultdict
from typing import List, Dict


def split_with_spaces(value: str):
    return re.split('\s+', value)


def decode_line(line: str):
    game_id_numbers = line.strip().split(':')
    game_id = int(split_with_spaces(game_id_numbers[0].strip())[1])
    winnings_you_have = game_id_numbers[1].strip().split('|')
    winnings = {int(n) for n in split_with_spaces(winnings_you_have[0].strip())}
    you_have = {int(n) for n in split_with_spaces(winnings_you_have[1].strip())}
    return game_id, winnings, you_have


def part_1():
    games = [decode_line(line) for line in open("input.txt", "r").readlines()]

    points = list(
        map(lambda w: pow(2, len(w) - 1), filter(lambda w: w, map(lambda g: g[1].intersection(g[2]), games))))
    print(sum(points))


def part_2():
    games = [decode_line(line) for line in open("input.txt", "r").readlines()]
    wons = list(
        map(lambda g: (g[0], len(g[1])), map(lambda g: (g[0], g[1].intersection(g[2])), games)))

    cards = defaultdict(int)
    for w in wons:
        cards[w[0]] = cards[w[0]] + 1
        for n in range(w[1]):
            cards[w[0] + n + 1] = cards[w[0] + n + 1] + cards[w[0]]

    print(sum(cards.values()))


part_1()
part_2()
