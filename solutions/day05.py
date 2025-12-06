"""
Day 5: Cafeteria
https://adventofcode.com/2025/day/5
"""

from itertools import takewhile
from operator import attrgetter

INPUT = "inputs/day05.txt"


def read_input():
    with open(INPUT) as f:

        def read_fresh_ingredient_ranges_section():
            return takewhile(lambda line: "-" in line, f)

        def parse_ingredient_id_range(line):
            first, last = line.rstrip().split("-")
            return range(int(first), int(last) + 1)

        def parse_ingredient_id(line):
            return int(line)

        fresh_ingredient_id_ranges = [
            parse_ingredient_id_range(line)
            for line in read_fresh_ingredient_ranges_section()
        ]

        available_ingredient_ids = [
            parse_ingredient_id(line)
            for line in f  # remaining lines
        ]

        return fresh_ingredient_id_ranges, available_ingredient_ids


def part1():
    fresh_ingredient_id_ranges, available_ingredient_ids = read_input()

    return sum(
        1
        for id in available_ingredient_ids
        if any(id in range for range in fresh_ingredient_id_ranges)
    )


def part2():
    fresh_ingredient_id_ranges, _ = read_input()

    def ranges_overlap(a, b):
        return a.start <= b.start < a.stop or b.start <= a.start < b.stop

    def merge_ranges(a, b):
        return range(min(a.start, b.start), max(a.stop, b.stop))

    def merge_all_overlapping_ranges(ranges):
        ranges_sorted_by_start = sorted(ranges, key=attrgetter("start"))
        result = []

        for range in ranges_sorted_by_start:
            previous = result[-1] if len(result) > 0 else None
            if previous and ranges_overlap(range, previous):
                result[-1] = merge_ranges(range, previous)
            else:
                result.append(range)

        return result

    return sum(
        len(range) for range in merge_all_overlapping_ranges(fresh_ingredient_id_ranges)
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
