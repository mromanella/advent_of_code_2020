"""--- Day 10: Adapter Array ---"""

import pathlib
from typing import List, Set


def read_input() -> List[str]:
    filepath = pathlib.Path(__file__).parent / 'input.txt'
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]

test = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4
]
test_2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3
]


def find_branches(target: int, joltages: List[int]) -> int:
    low = target + 1
    mid = target + 2
    high = target + 3

    viable = {low, mid, high}
    viable = sorted(viable.intersection(joltages))
    new_paths = [target]
    for v in viable:
        new_paths.append(find_branches(v, joltages))
    return new_paths

def part_1(lines: List[str]) -> int:
    diffs = []
    joltages = sorted([int(line) for line in lines])
    j = 0
    max_joltage = joltages[-1] + 3
    joltages.append(max_joltage)
    for joltage in joltages:
        diff = joltage - j
        diffs.append(diff)
        j = joltage
    return diffs.count(1) * diffs.count(3)

def part_2(lines: List[str]) -> int:
    joltages = sorted([int(line) for line in lines])
    max_joltage = joltages[-1] + 3
    joltages.append(max_joltage)
    branches = find_branches(0, joltages)
    return branches

if __name__ == "__main__":
    print(part_1(test_2))
    i = read_input()
    print(part_1(i))
