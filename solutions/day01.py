"""
Day 1: Secret Entrance
https://adventofcode.com/2025/day/1
"""

INPUT = "inputs/day01.txt"


class Dial:
    def __init__(self):
        self.position = 50

    def rotate(self, amount: int):
        self.position = (self.position + amount) % 100


def read_input():
    rotations: list[int] = []
    with open(INPUT) as f:
        for line in f:
            direction = line[0]
            amount = int(line[1:])
            rotations.append(-amount if direction == "L" else amount)
    return rotations


def part1():
    rotations = read_input()
    dial = Dial()
    zero_dial_count = 0

    for rotation in rotations:
        dial.rotate(rotation)
        if dial.position == 0:
            zero_dial_count += 1

    return zero_dial_count


def part2():
    rotations = read_input()
    dial = Dial()
    zero_dial_count = 0

    for rotation in rotations:
        for _ in range(abs(rotation)):
            dial.rotate(1 if rotation > 0 else -1)
            if dial.position == 0:
                zero_dial_count += 1

    return zero_dial_count


if __name__ == "__main__":
    print(part1())
    print(part2())
