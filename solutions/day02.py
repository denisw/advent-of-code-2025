"""
Day 2: Gift Shop
https://adventofcode.com/2025/day/2
"""

INPUT = "inputs/day02.txt"


def read_input():
    def parse_range(range):
        first, last = range.split("-")
        return (int(first), int(last))

    with open(INPUT) as f:
        line = f.readline()
        ranges = line.split(",")
        return [parse_range(range) for range in ranges]


def count_invalid_product_ids(ranges, is_invalid):
    return sum(
        product_id
        for first, last in ranges
        for product_id in range(first, last + 1)
        if is_invalid(product_id)
    )


def part1():
    def same_digits_repeated_once(product_id):
        digits = str(product_id)
        midpoint = len(digits) // 2
        return digits[:midpoint] == digits[midpoint:]

    return count_invalid_product_ids(
        ranges=read_input(), is_invalid=same_digits_repeated_once
    )


def part2():
    def same_digits_repeated_at_least_once(product_id):
        digits = str(product_id)
        for count in range(2, len(digits) + 1):
            sequence = digits[: len(digits) // count]
            if digits == sequence * count:
                return True
        return False

    return count_invalid_product_ids(
        ranges=read_input(),
        is_invalid=same_digits_repeated_at_least_once,
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
