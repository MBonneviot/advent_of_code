from collections import deque


def parse() -> list[str]:
    return [line.strip() for line in open("input.txt", "r").readlines()]


neighbours_directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
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


def part_2():
    def compute_area(plot: tuple[int, int], visited_plots: set[tuple[int, int]], map: list[str]) -> int:
        to_visit = deque()
        to_visit.append(plot)
        area = 0
        while to_visit:
            current_plot = to_visit.pop()
            if current_plot in visited_plots:
                continue

            area = area + 1
            visited_plots.add(current_plot)
            neighbours = get_neighbours(current_plot)
            for n in neighbours:
                if is_in_map(n, map) and get_plot_value(n, map) == get_plot_value(current_plot, map):
                    to_visit.append(n)
        return area

    def get_next_index(dir: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
        cur_dir_index = neighbours_directions.index(dir)
        if cur_dir_index < len(neighbours_directions) - 1:
            return neighbours_directions[cur_dir_index + 1], neighbours_directions[cur_dir_index], \
            neighbours_directions[
                cur_dir_index - 1]
        return neighbours_directions[0], neighbours_directions[cur_dir_index], neighbours_directions[cur_dir_index - 1]

    def get_next_plot_direction(plot: tuple[int, int], dir: tuple[int, int], map: list[str]) -> tuple[
        tuple[int, int], tuple[int, int]]:
        left, straight, right = get_next_index(dir)
        next_straight_plot = (plot[0] + straight[0], plot[1] + straight[1])
        if not is_in_map(next_straight_plot, map):
            return plot, right

        left_straight_plot = (plot[0] + left[0], plot[1] + left[1])
        if is_in_map(left_straight_plot, map) and get_plot_value(left_straight_plot, map) == get_plot_value(plot, map):
            return left_straight_plot, left

        if get_plot_value(next_straight_plot, map) == get_plot_value(plot, map):
            return next_straight_plot, straight

        right_straight_plot = (plot[0] + right[0], plot[1] + right[1])
        if is_in_map(right_straight_plot, map) and get_plot_value(right_straight_plot, map) == get_plot_value(plot,
                                                                                                              map):
            return right_straight_plot, right

        return plot, right

    def compute_borders(plot: tuple[int, int], map: list[str]) -> int:
        initial_plot = plot
        initial_dir = neighbours_directions[1]

        current_plot = initial_plot
        current_direction = initial_dir
        border_count = 0
        while border_count == 0 or not (current_plot == initial_plot and current_direction == initial_dir):
            new_plot, new_dir = get_next_plot_direction(current_plot, current_direction, map)
            if new_dir != current_direction:
                border_count = border_count + 1
            current_plot = new_plot
            current_direction = new_dir

        return border_count


    def compute_price(plot: tuple[int, int], visited_plots: set[tuple[int, int]], map: list[str]) -> int:
        area = compute_area(plot, visited_plots, map)
        borders = compute_borders(plot, map)
        return borders * area

    map = parse()
    print(compute_borders((2, 1), map))

    visited_plots = set()
    total_price = 0
    for j in range(len(map)):
        for i in range(len(map[0])):
            plot = (i, j)
            if plot in visited_plots:
                continue
            print(f'{plot} - {get_plot_value(plot, map)}')
            total_price = total_price + compute_price(plot, visited_plots, map)

    print(total_price)


#part_1()
part_2()
