from __future__ import annotations
from functools import reduce
import operator


def part_1():
    def compute_winning_distances(time, best_distance):
        winning_distances = list()
        for i in range(1, time):
            race_remaining_time = time - i
            distance = race_remaining_time * i
            if distance > best_distance:
                winning_distances.append(distance)
        return winning_distances

    # time_races = ((7, 9), (15, 40), (30, 200))
    time_races = ((46, 214), (80, 1177), (78, 1402), (66, 1024))
    print(reduce(operator.mul, [len(compute_winning_distances(t[0], t[1])) for t in time_races]))


def part_2():
    def compute_winning_distances(time, best_distance):
        winning_distances = list()
        for i in range(1, time):
            race_remaining_time = time - i
            distance = race_remaining_time * i
            if distance > best_distance:
                winning_distances.append(distance)
        return winning_distances

    # time_race = (71530, 940200)
    time_race = (46807866, 214117714021024)
    print(len(compute_winning_distances(time_race[0], time_race[1])))


part_1()
part_2()
