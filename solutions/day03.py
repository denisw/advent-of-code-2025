"""
Day 3: Lobby
https://adventofcode.com/2025/day/3
"""

INPUT = "inputs/day03.txt"


def read_input():
    with open(INPUT) as f:
        for line in f:
            yield line.strip()


def find_largest_achievable_joltage(battery_bank: str, batteries_to_enable: int):
    candidates = list(battery_bank)
    selected_batteries = []

    for i in range(1, batteries_to_enable + 1):
        min_remaining_candidates = batteries_to_enable - i
        candidates_for_next_battery = candidates[: -min_remaining_candidates or None]

        next_battery = max(candidates_for_next_battery)
        next_battery_index = candidates.index(next_battery)

        selected_batteries.append(next_battery)
        del candidates[: next_battery_index + 1]

    return int("".join(selected_batteries))


def part1():
    return sum(
        find_largest_achievable_joltage(bank, batteries_to_enable=2)
        for bank in read_input()
    )


def part2():
    return sum(
        find_largest_achievable_joltage(bank, batteries_to_enable=12)
        for bank in read_input()
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
