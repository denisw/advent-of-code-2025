"""
Day 4: Printing Department
https://adventofcode.com/2025/day/4
"""

INPUT = "inputs/day04.txt"

type PaperRoll = tuple[int, int]
"""The grid coordinate (row and column) of a paper roll on the floor plan."""


def read_input() -> set[PaperRoll]:
    paper_rolls = set()
    current_row = 0

    with open(INPUT) as f:
        for line in f:
            current_row += 1
            current_column = 0

            for char in line.rstrip():
                current_column += 1
                if char == "@":
                    paper_rolls.add((current_row, current_column))

    return paper_rolls


def count_adjacent_paper_rolls(roll: PaperRoll, all_rolls: set[PaperRoll]) -> int:
    row, column = roll
    return sum(
        1
        for adjacent_position in (
            (row - 1, column - 1),
            (row - 1, column),
            (row - 1, column + 1),
            (row, column - 1),
            (row, column + 1),
            (row + 1, column - 1),
            (row + 1, column),
            (row + 1, column + 1),
        )
        if adjacent_position in all_rolls
    )


def is_paper_roll_accessible(roll: PaperRoll, all_rolls: set[PaperRoll]) -> bool:
    return count_adjacent_paper_rolls(roll, all_rolls) < 4


def find_accessible_paper_rolls(rolls: set[PaperRoll]) -> set[PaperRoll]:
    return {roll for roll in rolls if is_paper_roll_accessible(roll, rolls)}


def part1():
    paper_rolls = read_input()
    return len(find_accessible_paper_rolls(paper_rolls))


def part2():
    paper_rolls = read_input()
    total_rolls_removed = 0

    while True:
        removable_rolls = find_accessible_paper_rolls(paper_rolls)
        if len(removable_rolls) > 0:
            paper_rolls.difference_update(removable_rolls)
            total_rolls_removed += len(removable_rolls)
        else:
            break

    return total_rolls_removed


if __name__ == "__main__":
    print(part1())
    print(part2())
