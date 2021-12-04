def part_1():
    import numpy as np

    def board_wins(board, draw):
        return (5 in [len(list(filter(lambda x: x in draw, board[i, :]))) for i in range(0, 5)] or
                5 in [len(list(filter(lambda x: x in draw, board[:, i]))) for i in range(0, 5)])

    lines = open("input.txt", "r").readlines()

    numbers = [int(i) for i in lines[0].split(',')]

    boards_input = lines[2:]
    raw_boards = [[list(map(int, j.split())) for j in boards_input[i:i + 5]] for i in
                  range(0, len(boards_input), 6)]
    boards = [np.array(i) for i in raw_boards]

    for draw_index in range(5, len(numbers)):
        draw = numbers[:draw_index]

        winner = list(filter(lambda b: board_wins(b, draw), boards))
        if winner:
            sum_unmarked = sum(filter(lambda x: x not in draw, np.nditer(winner)))
            print(sum_unmarked)
            last_draw = draw[-1]
            print(last_draw)
            print(sum_unmarked * last_draw)
            break


def part_2():
    import numpy as np

    def board_wins(board, draw):
        return (5 in [len(list(filter(lambda x: x in draw, board[i, :]))) for i in range(0, 5)] or
                5 in [len(list(filter(lambda x: x in draw, board[:, i]))) for i in range(0, 5)])

    lines = open("input.txt", "r").readlines()

    numbers = [int(i) for i in lines[0].split(',')]

    boards_input = lines[2:]
    raw_boards = [[list(map(int, j.split())) for j in boards_input[i:i + 5]] for i in
                  range(0, len(boards_input), 6)]
    boards = [np.array(i) for i in raw_boards]

    previous_winners = set()
    for draw_index in range(5, len(numbers)):
        draw = numbers[:draw_index]

        winners = set()
        for i in range(0, len(boards)):
            if board_wins(boards[i], draw):
                winners.add(i)

        if len(winners) != len(boards):
            previous_winners = winners
        else:
            last_winner = list(set(range(0, len(boards))) - previous_winners)[0]
            sum_unmarked = sum(filter(lambda x: x not in draw, np.nditer(boards[last_winner])))
            print(sum_unmarked)
            last_draw = draw[-1]
            print(last_draw)
            print(sum_unmarked * last_draw)
            break


part_1()
part_2()
