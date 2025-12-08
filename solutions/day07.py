"""
Day 7: Laboratories
https://adventofcode.com/2025/day/7
"""

from collections import deque
from typing import NamedTuple

INPUT = "inputs/day07.txt"


class Location(NamedTuple):
    row: int
    column: int


def read_input():
    with open(INPUT) as f:
        return [line.strip() for line in f.readlines()]


def part1():
    start_row, *rows = read_input()

    start_column = start_row.index("S")
    beam_columns = set([start_column])
    split_count = 0

    for row in rows:
        new_beam_columns = set()

        for column in beam_columns:
            if row[column] == "^":
                # Beam is split
                split_count += 1
                new_beam_columns.add(column - 1)
                new_beam_columns.add(column + 1)
            else:
                # Beam continues downwards
                new_beam_columns.add(column)

        beam_columns = new_beam_columns

    return split_count


def part2():
    pass  # TODO


if __name__ == "__main__":
    print(part1())
    print(part2())
