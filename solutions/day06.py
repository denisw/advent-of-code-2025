"""
Day 6: Trash Compactor
https://adventofcode.com/2025/day/6
"""

import operator
from dataclasses import dataclass
from functools import reduce
from itertools import takewhile

INPUT = "inputs/day06.txt"


def rotate(rows_or_columns: list[str]) -> list[str]:
    longest = max(rows_or_columns, key=len)
    return [
        "".join(x[i] if i < len(x) else " " for x in rows_or_columns)
        for i in range(len(longest))
    ]


@dataclass
class Problem:
    columns: list[str]

    @property
    def operator(self):
        match self.columns[0][-1]:
            case "+":
                return operator.add
            case "*":
                return operator.imul


def read_input():
    with open(INPUT) as f:
        rows = [line.rstrip("\n") for line in f if line.strip() != ""]
        columns = rotate(rows)

        problems = []
        while problem_columns := list(takewhile(lambda c: c.strip() != "", columns)):
            problems.append(Problem(problem_columns))
            del columns[: len(problem_columns) + 1]

        return problems


def part1():
    def solve_problem(problem):
        operand_rows = list(rotate(problem.columns))[:-1]
        operands = (int(op) for op in operand_rows)
        return reduce(problem.operator, operands)

    return sum(solve_problem(problem) for problem in read_input())


def part2():
    def solve_problem(problem):
        operands = (int(column[:-1]) for column in problem.columns)
        return reduce(problem.operator, operands)

    return sum(solve_problem(problem) for problem in read_input())


if __name__ == "__main__":
    print(part1())
    print(part2())
