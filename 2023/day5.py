from __future__ import annotations
from collections import defaultdict
from typing import List, Dict

almanac_order = [
    'seed-to-soil map:',
    'soil-to-fertilizer map:',
    'fertilizer-to-water map:',
    'water-to-light map:',
    'light-to-temperature map:',
    'temperature-to-humidity map:',
    'humidity-to-location map:'
]


def decode_almanac():
    seeds = list()
    category = ''
    mapping = defaultdict(list)
    for line in open("input.txt", "r").readlines():
        line_striped = line.strip()
        if not line_striped:
            continue
        if line_striped.startswith('seeds:'):
            seeds = [int(s) for s in line_striped.split(':')[1].strip().split(' ')]
            continue
        if ':' in line_striped:
            category = line_striped
            continue
        destination, source, range_length = line_striped.split(' ')
        mapping[category].append((int(source), int(destination), int(range_length)))
    for m in mapping.values():
        m.sort(key=lambda t: t[0])

    return seeds, mapping


def part_1():
    def corresponds(value: int, category: str, mapping: Dict[str, List[(int, int, int)]]):
        category_mapping: List[(int, int)] = mapping[category]
        for i in range(0, len(category_mapping)):
            current_mapping = category_mapping[i]
            if current_mapping[0] > value:
                continue
            if current_mapping[0] <= value < current_mapping[0] + current_mapping[2]:
                return value - current_mapping[0] + current_mapping[1]
        return value

    seeds, mapping = decode_almanac()
    locations = list()
    for seed in seeds:
        placement = seed
        for category in almanac_order:
            placement = corresponds(placement, category, mapping)
        locations.append(placement)

    print(min(locations))


def part_2():
    def corresponds(value: int, range_seed: int, categories: List[str], mapping: Dict[str, List[(int, int, int)]]):
        if not categories:
            return value
        category_mapping: List[(int, int)] = mapping[categories[0]]
        start = value
        end = value + range_seed
        for i in range(0, len(category_mapping)):
            current_mapping = category_mapping[i]
            if current_mapping[0] >= end:
                continue
            if current_mapping[0] <= start < current_mapping[0] + current_mapping[2]:
                if end <= current_mapping[0] + current_mapping[2]:
                    return corresponds(start - current_mapping[0] + current_mapping[1],
                                       range_seed,
                                       categories[1::],
                                       mapping)
                else:
                    split_range = current_mapping[0] + current_mapping[2] - start
                    return min(
                        corresponds(start - current_mapping[0] + current_mapping[1],
                                    split_range,
                                    categories[1::],
                                    mapping),
                        corresponds(start + split_range,
                                    end - current_mapping[0] - current_mapping[2],
                                    categories,
                                    mapping)
                    )
        return corresponds(value, range_seed, categories[1::], mapping)

    seed_params, mapping = decode_almanac()
    seeds = [(seed_params[i], seed_params[i + 1]) for i in range(0, len(seed_params), 2)]

    locations = list()
    for seed in seeds:
        placement, range_placement = seed
        locations.append(corresponds(placement, range_placement, almanac_order, mapping))
    print(min(locations))


part_1()
part_2()
