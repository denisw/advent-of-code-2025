"""
Day 8: Playground
https://adventofcode.com/2025/day/8
"""

from heapq import nlargest, nsmallest
import operator
from functools import reduce
from math import sqrt
from typing import cast

INPUT = "inputs/day08.txt"


type JunctionBox = tuple[int, int, int]
"""The X, Y and Z coordinates of a junction box."""


def read_input() -> list[JunctionBox]:
    with open(INPUT) as f:
        return [
            cast(JunctionBox, tuple(int(coordinate) for coordinate in line.split(",")))
            for line in f.readlines()
        ]


class JunctionBoxNetwork:
    def __init__(self, boxes: list[JunctionBox]):
        self.boxes = boxes
        self._circuits = {index: {box} for index, box in enumerate(boxes)}
        self._box_to_circuit = {box: index for index, box in enumerate(boxes)}

    def box_pairs_ordered_by_distance(self, limit=None):
        pairs = ((a, b) for a in self.boxes for b in self.boxes if a < b)

        def distance(pair):
            x1, y1, z1 = pair[0]
            x2, y2, z2 = pair[1]
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

        return (
            nsmallest(limit, pairs, key=distance)
            if limit
            else sorted(pairs, key=distance)
        )

    def circuits(self):
        return self._circuits.values()

    def connect(self, box1, box2):
        box1_circuit_index = self._box_to_circuit[box1]
        box2_circuit_index = self._box_to_circuit[box2]
        if box1_circuit_index != box2_circuit_index:
            for box in self._circuits[box1_circuit_index]:
                self._circuits[box2_circuit_index].add(box)
                self._box_to_circuit[box] = box2_circuit_index
            del self._circuits[box1_circuit_index]


def part1():
    junction_boxes = read_input()
    network = JunctionBoxNetwork(junction_boxes)

    for box1, box2 in network.box_pairs_ordered_by_distance(limit=1000):
        network.connect(box1, box2)

    largest_circuits = nlargest(3, network.circuits(), key=len)
    return reduce(operator.imul, (len(circuit) for circuit in largest_circuits))


def part2():
    junction_boxes = read_input()
    network = JunctionBoxNetwork(junction_boxes)
    last_connection = None

    for box1, box2 in network.box_pairs_ordered_by_distance():
        network.connect(box1, box2)
        last_connection = (box1, box2)
        if len(network.circuits()) == 1:
            break

    assert last_connection is not None
    (x1, _, _), (x2, _, _) = last_connection

    return x1 * x2


if __name__ == "__main__":
    print(part1())
    print(part2())
