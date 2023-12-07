from __future__ import annotations
from collections import Counter


def part_1():
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    hand_type = [
        ('five_of_a_kind', lambda ordered_hand: len(ordered_hand) == 1),
        ('four_of_a_kind', lambda ordered_hand: len(ordered_hand) == 2 and ordered_hand[0] == 4),
        ('full_house', lambda ordered_hand: len(ordered_hand) == 2 and ordered_hand[0] == 3),
        ('three_of_a_kind', lambda ordered_hand: len(ordered_hand) == 3 and ordered_hand[0] == 3),
        ('two_pair', lambda ordered_hand: len(ordered_hand) == 3 and ordered_hand[0] == 2),
        ('one_pair', lambda ordered_hand: len(ordered_hand) == 4),
        ("high_card", lambda ordered_hand: len(ordered_hand) == 5)
    ]

    hand_type_order = [ht[0] for ht in hand_type]

    def order_hand(hand: str):
        counters = list(Counter(hand).values())
        return sorted(counters, reverse=True)

    def rank_hand_type(hand: str):
        for ht, f in hand_type:
            if f(hand):
                return ht

    def generate_sort_key(value: (str, (str, int))):
        return hand_type_order.index(value[0]), [cards.index(c) for c in value[1][0]]

    hands = list(
        map(lambda t: (t[0], int(t[1])), [line.strip().split(' ') for line in open("input.txt", "r").readlines()]))
    ranked_hand = [(rank_hand_type(order_hand(h[0])), h) for h in hands]
    sorted_game = sorted(ranked_hand, key=generate_sort_key, reverse=True)
    print(sum([(i + 1) * sorted_game[i][1][1] for i in range(0, len(sorted_game))]))


def part_2():
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    hand_type = [
        ('five_of_a_kind', lambda ordered_hand: len(ordered_hand) == 1),
        ('four_of_a_kind', lambda ordered_hand: len(ordered_hand) == 2 and ordered_hand[0] == 4),
        ('full_house', lambda ordered_hand: len(ordered_hand) == 2 and ordered_hand[0] == 3),
        ('three_of_a_kind', lambda ordered_hand: len(ordered_hand) == 3 and ordered_hand[0] == 3),
        ('two_pair', lambda ordered_hand: len(ordered_hand) == 3 and ordered_hand[0] == 2),
        ('one_pair', lambda ordered_hand: len(ordered_hand) == 4),
        ("high_card", lambda ordered_hand: len(ordered_hand) == 5)
    ]

    hand_type_order = [ht[0] for ht in hand_type]

    def order_hand(hand: str):
        counters = Counter(hand)
        joker_count = counters.get('J', 0)
        counters.pop('J', None)
        counter_no_jokers = sorted(list(counters.values()), reverse=True)
        if counter_no_jokers:
            counter_no_jokers[0] = counter_no_jokers[0] + joker_count
            return counter_no_jokers
        else:
            return [joker_count]

    def rank_hand_type(hand: str):
        for ht, f in hand_type:
            if f(hand):
                return ht

    def generate_sort_key(value: (str, (str, int))):
        return hand_type_order.index(value[0]), [cards.index(c) for c in value[1][0]]

    hands = list(
        map(lambda t: (t[0], int(t[1])), [line.strip().split(' ') for line in open("input.txt", "r").readlines()]))
    ranked_hand = [(rank_hand_type(order_hand(h[0])), h) for h in hands]
    sorted_game = sorted(ranked_hand, key=generate_sort_key, reverse=True)
    print(sum([(i + 1) * sorted_game[i][1][1] for i in range(0, len(sorted_game))]))


part_1()
part_2()
