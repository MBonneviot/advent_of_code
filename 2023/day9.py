from typing import List, Dict, Set


def part_1():
    def compute_prediction(history: List[int]):
        if all([h == 0 for h in history]):
            return 0

        diff = [history[i] - history[i - 1] for i in range(1, len(history))]
        return history[-1] + compute_prediction(diff)

    sensor_histories = [list(map(lambda c: int(c), line.strip().split(' '))) for line in
                        open("input.txt", "r").readlines()]

    predictions = [compute_prediction(h) for h in sensor_histories]
    print(sum(predictions))


def part_2():
    def compute_prediction(history: List[int]):
        if all([h == 0 for h in history]):
            return 0

        diff = [history[i] - history[i - 1] for i in range(1, len(history))]
        return history[0] - compute_prediction(diff)

    sensor_histories = [list(map(lambda c: int(c), line.strip().split(' '))) for line in
                        open("input.txt", "r").readlines()]

    predictions = [compute_prediction(h) for h in sensor_histories]
    print(sum(predictions))


part_1()
part_2()
