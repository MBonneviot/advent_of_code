from collections import deque
def parse() -> list[str]:
    return [line.strip() for line in open("input.txt", "r").readlines()]


neighbours_directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

def is_in_map(pos: tuple[int, int], map: list[str]) -> bool:
    return (
            0 <= pos[0] < len(map[0]) and
            0 <= pos[1] < len(map)
    )


def get_neighbours(plot: tuple[int, int]) -> list[tuple[int, int]]:
    return [(plot[0] + nd[0], plot[1] + nd[1]) for nd in neighbours_directions]

def get_plot_value(plot: tuple[int, int], map: list[str]) -> str:
    return map[plot[1]][plot[0]]

def part_1():
    def compute_price(plot: tuple[int, int], visited_plots: set[tuple[int, int]], map: list[str]) -> int:
        to_visit = deque()
        to_visit.append(plot)
        fence = 0
        area = 0
        while to_visit:
            current_plot = to_visit.pop()
            if current_plot in visited_plots:
                continue

            area = area + 1
            visited_plots.add(current_plot)
            neighbours = get_neighbours(current_plot)
            for n in neighbours:
                if not is_in_map(n, map):
                    fence = fence + 1
                elif get_plot_value(n, map) == get_plot_value(current_plot, map):
                    to_visit.append(n)
                else:
                    fence = fence + 1
        return fence * area

    map = parse()
    visited_plots = set()
    total_price = 0
    for i in range(len(map[0])):
        for j in range(len(map)):
            plot = (i, j)
            if plot in visited_plots:
                continue
            total_price = total_price + compute_price(plot, visited_plots, map)

    print(total_price)

#def part_2():



part_1()
#part_2()
