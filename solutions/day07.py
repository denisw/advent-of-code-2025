"""
Day 7: Laboratories
https://adventofcode.com/2025/day/7
"""

from collections import defaultdict
from functools import cache

INPUT = "inputs/day07.txt"


def read_input():
    with open(INPUT) as f:
        return [line.strip() for line in f.readlines()]


@cache
def simulate_beams():
    rows = read_input()

    initial_beam_column = rows[0].index("S")
    beams = set([initial_beam_column])

    split_count = 0
    path_counts = defaultdict(int, {initial_beam_column: 1})

    for row in rows[1:]:
        next_row_beams = set()

        for column in beams:
            if row[column] == "^":
                # Beam is split
                next_row_beams.add(column - 1)
                next_row_beams.add(column + 1)
                path_counts[column - 1] += path_counts[column]
                path_counts[column + 1] += path_counts[column]
                path_counts[column] = 0
                split_count += 1
            else:
                # Beam continues downwards
                next_row_beams.add(column)

        beams = next_row_beams

    total_path_count = sum(path_counts.values())
    return split_count, total_path_count


def part1():
    split_count, _ = simulate_beams()
    return split_count


def part2():
    _, path_count = simulate_beams()
    return path_count


if __name__ == "__main__":
    print(part1())
    print(part2())
