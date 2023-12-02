from __future__ import annotations
from functools import reduce


class Grab:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"red:{self.red}|green:{self.green}|blue:{self.blue}"

    def __repr__(self):
        return str(self)

    def maximize(self, other: Grab):
        return Grab(
            red=max(self.red, other.red),
            green=max(self.green, other.green),
            blue=max(self.blue, other.blue)
        )

    def lower(self, other: Grab):
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue

    def power(self):
        return self.red * self.green * self.blue


def decode_grab(grab_str: str):
    cubes = grab_str.strip().split(',')
    grab = Grab(0, 0, 0)
    for c in cubes:
        number = c.strip().split(' ')[0]
        color = c.strip().split(' ')[1]
        if color == 'red':
            grab.red = int(number)
        if color == 'blue':
            grab.blue = int(number)
        if color == 'green':
            grab.green = int(number)
    return grab


def decode_line(line: str):
    game = int(line.split(':', 1)[0].split(' ', 1)[1])
    grabs = line.split(':', 1)[1].split(';')
    return game, [decode_grab(g) for g in grabs]


def part_1():
    games = list(
        map(lambda l: decode_line(l.strip()), open("input.txt", "r").readlines()))

    max_games = [(g[0], reduce(lambda lhs, rhs: lhs.maximize(rhs), g[1])) for g in games]

    bag = Grab(red=12, green=13, blue=14)

    possible_games = list(map(lambda g: g[0], filter(lambda g: g[1].lower(bag), max_games)))

    print(sum(possible_games))


def part_2():
    games = list(
        map(lambda l: decode_line(l.strip()), open("input.txt", "r").readlines()))

    max_games = [(g[0], reduce(lambda lhs, rhs: lhs.maximize(rhs), g[1])) for g in games]

    powers = [g[1].power() for g in max_games]
    print(sum(powers))


part_1()
part_2()
